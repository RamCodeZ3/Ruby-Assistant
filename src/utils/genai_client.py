from google import genai
from google.genai import types
import os
import pyttsx3

PATH = os.path.abspath('media/answer.txt')

class GenaiClient:
    def __init__(self):
        self.API_KEY = os.getenv('GEMINI_API_KEY')
        self.instruction = "your name is Ruby and you are a assistant"
        
    def generate_response(self, content):
        client = genai.Client(api_key=self.API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            config=types.GenerateContentConfig(
                system_instruction=self.instruction
            ),
            contents=f'{content}'
        )
        
        self.generate_voice(response.text)
    
    def generate_voice(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
