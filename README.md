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
1. Clone the Repository
   git clone https://github.com/YourGitHubUsername/Jarvis-AI-Assistant.git         
   cd Jarvis-AI-Assistant

















