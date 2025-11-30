from google import genai
from google.genai import types
import os
import pyttsx3
from utils.notify import generate_notification


HOME = os.path.expanduser("~")

class GenaiClient:
    def __init__(self):
        self.API_KEY = os.getenv('GEMINI_API_KEY')
        self.instruction = "your name is Ruby and you are a assistant"
        self.instruction_comand = """
            You must convert any instruction I provide into a valid Windows command.
            The command should perform safe actions such as shutting down the PC,
            copying files, moving files, or creating folders.

            If the instruction attempts to perform any harmful, dangerous, or destructive action — 
            such as modifying, deleting, or accessing critical system files or directories 
            (e.g., System32, Windows folders, Program Files, drivers, registry files) —
            you must NOT execute it.

            Instead, you must respond with a single word only: "Impossible".

            Never generate harmful commands. Never attempt to bypass safety.
            Never include backticks (`) or quotes around the command. 
            Return only the raw Windows command.
            The path of create files in dir: {HOME}/Documents.
        """

    def classify_prompts(self, text):
        propts= f"""
            Classify this request as a question or instruction: {text}. 
            Your answer will only be a word: question or instruction
        """
        client = genai.Client(api_key=self.API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=propts
        )
        
        if response.text.lower() == 'question':
            self.generate_response(text)
        
        elif response.text.lower() == 'instruction':
            self.generate_command(text)
    
    
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
    
    def generate_command(self, content):
        client = genai.Client(api_key=self.API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            config=types.GenerateContentConfig(
                system_instruction=self.instruction_comand
            ),
            contents=f'{content}'
        )
        if response.text == 'Impossible':
            generate_notification('Error', 'La ultima orden no se puede ejecutar.')
        
        else: 
            os.system(response.text)
    
    def generate_voice(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
