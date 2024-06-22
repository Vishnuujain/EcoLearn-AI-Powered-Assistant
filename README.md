
# EcoLearn: AI-Powered Environmental Education Assistant

## Table of Contents
- [Project Aim](#project-aim)
- [Core Ideas](#core-ideas)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

## Project Aim

EcoLearn is an innovative project that aims to revolutionize environmental education by harnessing the power of artificial intelligence and real-time data. Our mission is to make learning about environmental science and sustainability:

- **Engaging**: Through interactive, AI-driven conversations and real-world data visualizations.
- **Personalized**: By adapting content to each user's knowledge level, interests, and learning pace.
- **Accessible**: To a wide range of users, from students to lifelong learners, regardless of their background or location.
- **Practical**: By focusing on real-world applications and project-based learning.

By combining cutting-edge AI technology with comprehensive environmental data, EcoLearn strives to create an educational experience that not only informs but also inspires action towards a more sustainable future.

## Core Ideas

EcoLearn is built on several fundamental concepts that drive its development and functionality:

1. **AI-Driven Personalization**: 
   - Utilizes advanced language models to understand user queries and generate tailored responses.
   - Adapts content difficulty and depth based on the user's demonstrated knowledge and learning progress.
   - Creates personalized learning paths that evolve with the user's interests and goals.

2. **Real-Time Environmental Data Integration**: 
   - Connects to various environmental APIs to provide up-to-date information on air quality, climate patterns, and biodiversity.
   - Transforms raw data into meaningful insights and learning opportunities.
   - Allows users to explore current environmental trends and issues as they happen.

3. **Interactive Learning Experience**: 
   - Combines conversational AI with data visualization to create an immersive educational environment.
   - Incorporates gamification elements to increase engagement and motivation.
   - Provides hands-on, project-based learning opportunities to apply knowledge in practical scenarios.

4. **Holistic Approach to Environmental Education**: 
   - Covers a wide range of environmental topics, from climate change and biodiversity to sustainable living and clean energy.
   - Emphasizes the interconnectedness of environmental systems and human activities.
   - Encourages critical thinking and systems-level understanding of environmental issues.

## Key Features

EcoLearn offers a rich set of features designed to enhance the learning experience:

1. **Personalized Learning Paths**: 
   - Adaptive content delivery based on user profile and progress.
   - Customized recommendations for topics and resources.
   - Progress tracking and performance analytics.

2. **Interactive Data Visualizations**: 
   - Dynamic charts and graphs illustrating environmental trends.
   - Interactive maps for exploring geographical data.
   - Real-time data updates for current environmental conditions.

3. **Real-time Environmental Data Integration**: 
   - Air Quality Index (AQI) data from OpenAQ API.
   - Climate data from NOAA Climate Data Online API.
   - Biodiversity information from GBIF (Global Biodiversity Information Facility) API.

4. **Gamification Elements**: 
   - Quizzes and challenges to test and reinforce knowledge.
   - Achievement badges and rewards for completing learning milestones.
   - Leaderboards to encourage friendly competition among users.

5. **Multilingual Support**: 
   - Content available in multiple languages to reach a global audience.
   - Automatic language detection and translation features.

6. **Accessibility Features**: 
   - Text-to-speech functionality for audio learning.
   - Speech-to-text capabilities for hands-free interaction.
   - High-contrast mode and customizable text sizes for improved readability.

7. **Environmental News Curator**: 
   - Aggregates and summarizes recent environmental news from reliable sources.
   - Personalized news feed based on user interests and learning topics.

8. **Carbon Footprint Calculator**: 
   - Estimates personal or household carbon footprint based on user input.
   - Provides personalized suggestions for reducing environmental impact.
   - Tracks progress over time and sets reduction goals.

9. **Virtual Field Trips** (Coming Soon): 
   - Immersive, 360-degree virtual tours of various ecosystems and environmental sites.
   - Interactive elements to explore and learn about different environments.

10. **Expert Connection** (Coming Soon): 
    - Live Q&A sessions with environmental scientists and experts.
    - Scheduled webinars on specific environmental topics.

## Technology Stack

EcoLearn is built using a modern and robust technology stack:

- **Backend**: Python 3.9+ with FastAPI framework
- **AI Model**: Anthropic's Language Model
- **Database**: SQLAlchemy with SQLite (easily scalable to PostgreSQL)
- **API Integrations**: OpenAQ, NOAA, GBIF
- **Data Visualization**: Plotly
- **Containerization**: Docker
- **Version Control**: Git

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/ecolearn.git
   cd ecolearn
   ```

2. Create and activate a virtual environment:
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```shell
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_CSE_ID=your_google_cse_id
   NOAA_API_KEY=your_noaa_api_key
   ```
   Replace `your_*_api_key` with your actual API keys.

## EcoLearn Pipeline and System Architecture

![EcoLearn Pipeline](https://raw.githubusercontent.com/Vishnuujain/EcoLearn-AI-Powered-Environmental-Education-Assistant/main/images/ecolearn_pipeline.svg)

## Usage
### Running the Application

1. Start the FastAPI server:
   ```shell
   uvicorn main:app --reload
   ```

2. Open your web browser and navigate to `http://localhost:8000/docs` to access the Swagger UI, where you can interact with the API endpoints.

### API Endpoints

1. Chat Interface:
   ```shell
   POST /chat
   {
     "user_input": "Tell me about climate change",
     "user_id": 1
   }
   ```

2. Generate Educational Content:
   ```shell
   POST /generate_content
   {
     "topic": "Renewable Energy",
     "user_id": 1
   }
   ```

3. Visualize Environmental Data:
   ```shell
   GET /visualize_data?data_type=air_quality&location=New York
   ```

For more detailed API documentation, refer to the Swagger UI when the server is running.

## Project Structure

```shell
ecolearn/
│
├── main.py              # Main application file
├── api_wrappers.py      # API wrapper classes
├── models.py            # Database models
├── utils.py             # Utility functions
├── database.py          # Database configuration
├── requirements.txt     # Project dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation
```

## Contributing

We welcome contributions to EcoLearn! If you're interested in helping, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Create a pull request

Please make sure to update tests as appropriate and adhere to the code style guidelines. For major changes, please open an issue first to discuss what you would like to change.

See the [CONTRIBUTING.md](CONTRIBUTING.md) file for more detailed information on our contribution process.

## Roadmap

We have exciting plans for the future of EcoLearn:

- [ ] Implement user authentication and profile management
- [ ] Develop a front-end interface for easier interaction
- [ ] Integrate more environmental data sources
- [ ] Implement the virtual field trips feature
- [ ] Set up expert Q&A sessions
- [ ] Expand multilingual support
- [ ] Develop mobile applications for iOS and Android
- [ ] Implement a recommendation system for personalized learning resources
- [ ] Create an educator dashboard for classroom management

We're always open to suggestions and contributions from the community to make EcoLearn even better!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feedback, or would like to collaborate, please don't hesitate to reach out:

- **Email**: vishnu_j@mt.iitr.ac.in

You can also open an issue on GitHub for bug reports or feature requests.

---

Join us in our mission to empower environmental education through AI. Together, we can create a more sustainable future! 🌍🤖📚
```
