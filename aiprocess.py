from groq import Groq
import os
from dotenv import load_dotenv

# Chat with AI using Groq API (LLaMA 4 model) 
conversation_memory = []         # Stores recent convertsation history
def aiprocess(command):
    try:
        # Add role and tone to Assistant
        messages = [{"role": "system", "content": "You are a helpful assistant named Jarvis."}]
        
        # Add last 5 messages to maintain context
        for q, a in conversation_memory[-5:]:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        messages.append({"role": "user", "content": command})       # User's current question
        load_dotenv()
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        # Call Groq API
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=messages
        )

        reply = completion.choices[0].message.content
        conversation_memory.append((command, reply))   # Save to memory
        return reply

    except Exception as e:
        print("AI API Error:", e)
        return "Sorry, I couldn't process your request at the moment."