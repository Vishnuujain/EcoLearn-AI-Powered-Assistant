#pip install google-api-python-client

import os
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatAnthropic
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent
import gradio as gr 

from dotenv import load_dotenv
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")


search = GoogleSearchAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful when you need to answer questions about current events"
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatAnthropic(anthropic_api_key=ANTHROPIC_API_KEY, temperature=0)
agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description",
                               verbose=True, memory=memory)
agent_chain.run(input="what is langchain?")
