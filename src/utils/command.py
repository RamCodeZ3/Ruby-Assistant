import speech_recognition as sr
import re 
import shutil
import json
from dotenv import load_dotenv
import os
from utils.genai_client import GenaiClient


load_dotenv()
genai = GenaiClient()
HOME = os.path.expanduser("~")
# path for config/paths.json at the repo's src/config directory
PATHS_JSON = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'paths.json'))


class CommandVoice:
    def __init__(self):
        self.r = sr.Recognizer()
        self.r.pause_threshold = 1.0
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
                    
                    print(self.text) # debug
                    
                    if 'rubí' in self.text.lower():
                        genai.classify_prompts(self.text)
                    
                    elif self.text.startswith('Open') or self.text.startswith('open'):
                        file_name = re.sub("open ", "", self.text.lower())
                        self.open_file(file_name)
  
                except sr.UnknownValueError:
                     print("No se entendio el audio")
                
                except Exception as e:
                    print('Hubo un error: ', e)
    
    def open_file(self, name):
         
         def ensure_paths_json_exists():
             config_dir = os.path.dirname(PATHS_JSON)
             try:
                 if not os.path.exists(config_dir):
                     os.makedirs(config_dir, exist_ok=True)
                 if not os.path.exists(PATHS_JSON):
                     with open(PATHS_JSON, 'w', encoding='utf-8') as f:
                         json.dump({}, f, indent=2, ensure_ascii=False)
             except Exception as e:
                 print('No se pudo crear config/paths.json:', e)

         ensure_paths_json_exists()

         data = {}
         try:
             with open(PATHS_JSON, 'r', encoding='utf-8') as f:
                 data = json.load(f)
         except Exception as e:
             print('Error leyendo el json de rutas:', e)

         # lookup by key (case-insensitive mapping via upper)
         key = name.upper()
         if key in data:
             try:
                 os.startfile(data[key])
                 return
             except Exception as e:
                 print('No se pudo abrir la ruta desde json:', e)

         # fallback: search in PATH
         file_path = shutil.which(name)
         if file_path:
            print(file_path)
            os.startfile(file_path)
            return

         print('No se encontro la ruta del archivo')
