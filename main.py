# File: main.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.llms import OpenAI
from langchain.memory import ConversationEntityMemory
from langchain.agents import Tool, initialize_agent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from api_wrappers import GoogleSearchAPIWrapper, OpenAQAPIWrapper, NOAAAPIWrapper, GBIFAPIWrapper
from models import UserProfile, LearningPath
from utils import generate_response, create_visualization
from database import SessionLocal, engine
import models

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize language model
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize memory
memory = ConversationEntityMemory(llm=llm)

# Initialize API wrappers
search = GoogleSearchAPIWrapper()
openaq = OpenAQAPIWrapper()
noaa = NOAAAPIWrapper()
gbif = GBIFAPIWrapper()

# Define tools
tools = [
    Tool(
        name="Google Search",
        func=search.run,
        description="Useful for general information on environmental topics"
    ),
    Tool(
        name="Air Quality Data",
        func=openaq.run,
        description="Provides real-time air quality data for locations worldwide"
    ),
    Tool(
        name="Climate Data",
        func=noaa.run,
        description="Offers historical and forecasted climate data"
    ),
    Tool(
        name="Biodiversity Information",
        func=gbif.run,
        description="Provides data on species occurrences and distributions"
    )
]

# Initialize agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Define prompt template for dynamic content generation
template = """
Given the user's age {age} and interest level {interest_level},
generate an engaging explanation about {topic} in environmental science.
"""

prompt = PromptTemplate(
    input_variables=["age", "interest_level", "topic"],
    template=template
)

content_chain = LLMChain(llm=llm, prompt=prompt)

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.post("/chat")
async def chat(user_input: str, user_id: int):
    db = SessionLocal()
    user = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    
    # Generate response
    response = generate_response(agent, memory, user_input, user)
    
    # Update user's learning path
    learning_path = db.query(LearningPath).filter(LearningPath.user_id == user_id).first()
    learning_path.update_progress(user_input, response)
    
    db.commit()
    db.close()
    
    return {"response": response}

@app.post("/generate_content")
async def generate_content(topic: str, user_id: int):
    db = SessionLocal()
    user = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    
    content = content_chain.run(age=user.age, interest_level=user.interest_level, topic=topic)
    
    db.close()
    
    return {"content": content}

@app.get("/visualize_data")
async def visualize_data(data_type: str, location: str):
    if data_type == "air_quality":
        data = openaq.get_data(location)
    elif data_type == "climate":
        data = noaa.get_data(location)
    elif data_type == "biodiversity":
        data = gbif.get_data(location)
    else:
        return {"error": "Invalid data type"}
    
    visualization = create_visualization(data, data_type)
    
    return {"visualization": visualization}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
