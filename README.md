# Conversational Agent with Anthropic Language Model and Google Search

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This repository contains a Python script that implements a conversational agent using the Anthropic language model and Google Search API. The agent is capable of engaging in interactive conversations with users, providing informative and relevant responses based on the user's input.

## Features

- Utilizes the Anthropic language model for generating human-like responses
- Integrates with the Google Search API to retrieve relevant information
- Maintains conversation context using a memory buffer
- Provides a user-friendly interface powered by Gradio for easy interaction

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Required dependencies installed (`langchain`, `gradio`, `python-dotenv`)
- Anthropic API key
- Google Search API key and Custom Search Engine ID

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/conversational-agent.git
   ```

2. Navigate to the project directory:

   ```shell
   cd conversational-agent
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your API keys and IDs:

   ```
   ANTHROPIC_API_KEY=your-anthropic-api-key
   GOOGLE_API_KEY=your-google-api-key
   GOOGLE_CSE_ID=your-google-cse-id
   ```

## Usage

1. Run the script:

   ```shell
   python conversational_agent.py
   ```

2. Access the Gradio interface by opening the provided URL in a web browser.

3. Type your message or question in the input box and click "Submit" to get a response from the agent.

4. Continue the conversation by entering subsequent messages.


## Demo Video Link: https://www.loom.com/share/147f5656f9194b4e8ed1477804ee1009


## Customization

- You can customize the agent's behavior by modifying the `tools` list in the script. Add or remove tools based on your requirements.

- Adjust the `temperature` parameter in the `ChatAnthropic` initialization to control the randomness and creativity of the generated responses. Lower values make the responses more deterministic, while higher values introduce more randomness.

- Modify the `description` parameter in the `gr.Interface` initialization to provide a different description for the user interface.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This script utilizes the [Langchain](https://github.com/hwchase17/langchain) library for integrating the Anthropic language model and Google Search API.
- The user interface is powered by [Gradio](https://gradio.app/), which provides a simple way to create interactive demos.
