# JARVIS - AI VOICE ASSISTANT
JARVIS is a terminal-based AI voice assistant built using Python and their modules that performs smart tasks like weather updates, news, music control, and system automation via voice commands.
This project showcases advanced voice recognition, system automation, and integration with external APIs, demonstrating proficiency in Python development and AI application.
It integrates APIs (Groq, Weather, News) and OS-level features to act as your personal assistant directly from the command line.

## Features
- Security Feature: Includes a basic password lock for initial access. of Jarvis.
- Voice-Activated Control: Initiate interaction by simply saying "Jarvis."
- System Commands:               
            - Volume Control: Adjust volume up or down.            
            - Brightness Control: Increase or decrease screen brightness.          
            - Power Management: Shut down, restart, log out, or put the computer to sleep.       
- Application Launcher: Open commonly used applications such as Notepad, VS Code, Word, Chrome, and many others with voice commands.
- Media Playback Control: Play/pause, skip to the next, or go back to the previous song using universal media key simulations. 
- Web Browse: Open popular websites (like Google, YouTube, Github, etc.) directly through voice. 
- YouTube Music Integration: Search and play specific songs on YouTube Music. 
- Date and Time: Get the current date and time in IST (Indian Standard Time). 
- Real-time News Updates: Fetch and read the top 3 headlines from around the world using the News API. 
- Live Weather Information: Get current weather details (temperature, description, humidity, wind speed) for any specified city using the OpenWeatherMap API. 
- Conversational AI: Engage in natural language conversations powered by the Groq API (utilizing the LLaMA 4 model) with built-in conversation memory for context.

## Technologies Used
- Python 3.12.6 : The core programming language.                                                
- pyttsx3 : Offline Text-to-Speech (TTS) engine for Jarvis's voice output.                                    
- Speech_Recognition : For converting spoken language into text using Google Speech Recognition.                                    
- pycaw : Windows-specific audio device control for volume management.                         
- screen_brightness_control : For adjusting screen brightness.                         
- pyautogui : Automates keyboard and mouse interactions, used for media controls.                         
- requests : For making HTTP requests to external APIs (News API, OpenWeatherMap API).                                     
- webbrowser : To open URLs in the default web browser.                                     
- pytz : For accurate timezone handling (specifically IST).                                     
- python-dotenv : To manage environment variables securely (API keys).                                     
- Groq API : Powers the conversational AI, utilizing the LLaMA 4 model for intelligent responses.                                    
- os, sys, subprocess, re, datetime : Standard Python libraries for system interaction, process management, string manipulation, and date/time operations.                                     

## Setup and Installation
Follow these steps to get Jarvis up and running on your local machine:-                
* ### 1. Clone the Repository                                    
    Start by cloning the Jarvis AI Assistant repository to your local machine:                                    
    ```bash                                                
    git clone [https://github.com/YourGitHubUsername/Jarvis-AI-Assistant.git](https://github.com/YourGitHubUsername/Jarvis-AI-Assistant.git)
    cd Jarvis-AI-Assistant
    ```
* ### 2. Create a Virtual Environment (Recommended)
    It's highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.                        
    ```bash
    python -m venv .venv
    ```
    Activate the virtual environment:
    * **On Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
* ### 3. Install Dependencies
    Once your virtual environment is active, install all the necessary Python libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
* ### 4. Obtain API Keys
    Jarvis integrates with several external services. To enable all features, you'll need to obtain API keys for the following and store them securely:
    * **Groq API Key**: For conversational AI.
        1.  Visit [Groq](https://groq.com/) and sign up for an account.
        2.  Navigate to your API Keys section and generate a new key.
    * **OpenWeatherMap API Key**: For real-time weather information.
        1.  Go to [OpenWeatherMap](https://openweathermap.com/api) and create a free account.
        2.  Find your API key in your account dashboard.
    * **News API Key**: For fetching news headlines.
        1.  Head over to [News API](https://newsapi.org/) and sign up.
        2.  Obtain your API key from your developer account.
* ### 5. Configure Environment Variables
    Create a file named `.env` in the root directory of your `Jarvis-AI-Assistant` project (the same folder where `main.py` is located). Add your newly obtained API keys to this file in the following format:
    ```dotenv
    GROQ_API_KEY="your_groq_api_key_here"
    WEATHER_API_KEY="your_openweathermap_api_key_here"
    NEWS_API_KEY="your_news_api_key_here"
    ```
    **Important**: The `.env` file is included in the `.gitignore` to prevent your sensitive API keys from being accidentally committed to your public repository. **Never share your `.env` file.**

## How to Run
Once you've completed the setup and installation steps, follow these instructions to launch and interact with Jarvis:
* ### 1. Activate Your Virtual Environment
    It's crucial to ensure your virtual environment is active before running the assistant. If you closed your terminal or opened a new one, reactivate it using the appropriate command:
    * **On Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
* ### 2. Start the Assistant
    Navigate to the root directory of your project (where `main.py` is located) and execute the main script:
    ```bash
    python main.py
    ```
* ### 3. Initializing Jarvis
    Upon launching, Jarvis will:
    * Perform an initial setup and say "Initializing Jarvis...".
    * If a password lock is enabled (configurable in `security.py`), it will prompt you for the password first.
    * Once initialized, Jarvis will start listening for its wake word(Jarvis).
* ### 4. Interacting with Jarvis
    To begin interacting:
    * **Say "Jarvis"**: This is the wake word that activates the assistant. Jarvis will respond with "Ya" and "How may I help you?".
    * **Give a Command**: After the prompt, speak your command clearly. For example:
        * "Open Google"
        * "Play music[music_name] on Youtube Music"
        * "What's the weather in London?"
        * "Tell me the news"
        * "What is the future of a Data Scientist?" (if using the AI for general queries)
    * **To Exit**: Say "exit" or "stop" at any point to terminate the program.













