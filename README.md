## Build your Own ChatGPT Bot with Internet Access and Memory using LangChain and Gradio integrated with Google custom search API and Anthropic API.

Conversational Agent with Anthropic Language Model and Google Search
This repository contains a Python script that implements a conversational agent using the Anthropic language model and Google Search API. The agent is capable of engaging in interactive conversations with users, providing informative and relevant responses based on the user's input.
Features

Utilizes the Anthropic language model for generating human-like responses
Integrates with the Google Search API to retrieve relevant information
Maintains conversation context using a memory buffer
Provides a user-friendly interface powered by Gradio for easy interaction

Prerequisites
Before running the script, make sure you have the following:

Python 3.x installed
Required dependencies installed (langchain, gradio, python-dotenv)
Anthropic API key
Google Search API key and Custom Search Engine ID

Installation

Clone the repository:
Copy codegit clone https://github.com/your-username/conversational-agent.git

Install the required dependencies:
Copy codepip install langchain gradio python-dotenv

Create a .env file in the project directory and add your API keys and IDs:
Copy codeANTHROPIC_API_KEY=your-anthropic-api-key
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CSE_ID=your-google-cse-id


Usage

Run the script:
Copy codepython conversational_agent.py

Access the Gradio interface by opening the provided URL in a web browser.
Type your message or question in the input box and click "Submit" to get a response from the agent.
Continue the conversation by entering subsequent messages.

Customization

You can customize the agent's behavior by modifying the tools list in the script. Add or remove tools based on your requirements.
Adjust the temperature parameter in the ChatAnthropic initialization to control the randomness and creativity of the generated responses. Lower values make the responses more deterministic, while higher values introduce more randomness.
Modify the description parameter in the gr.Interface initialization to provide a different description for the user interface.
