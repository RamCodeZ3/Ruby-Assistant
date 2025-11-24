import speech_recognition as sr
import re 
import shutil
from dotenv import load_dotenv
import os
from utils.genai_client import GenaiClient

load_dotenv()
genai = GenaiClient()

class CommandVoice:
    def __init__(self):
        self.r = sr.Recognizer()
        self.text = None
        self.listenVoice()

    def listenVoice(self):
         with sr.Microphone() as source:
            print('Puedes hablar')
            while True:
                print('-------------------')
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)

                try:
                    self.text = self.r.recognize_google(
                        audio,
                        language="es-ES"
                    )
                    
                    print(self.text)
                    if self.text == 'cerrar': 
                        break
                    
                    elif 'rubí' in self.text.lower():
                        genai.classify_prompts(self.text)
                    
                    elif self.text.startswith('Open') or self.text.startswith('open'):
                        file_name = re.sub("open ", "", self.text.lower())
                        self.open_file(file_name)
  
                except sr.UnknownValueError:
                     print("No se entendio el audio")
                
                except Exception as e:
                    print('Hubo un error: ', e)
    
    def open_file(self, name):
         for key, value in os.environ.items():
             if name.upper() == key:
                 os.startfile(value)
                 
             if name == 'all':
                for key, value in os.environ.items():
                 os.startfile(value)
    
         file_path = shutil.which(name)

         if file_path:
            print(file_path)
            os.startfile(file_path)
         else: print('No se encontro la ruta del archivo')