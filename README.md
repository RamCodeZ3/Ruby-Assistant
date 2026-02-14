# 🎙️ Ruby Assistant

**Ruby Assistant** es un asistente de voz desarrollado en **Python** como proyecto de práctica.  
Permite ejecutar programas mediante comandos de voz y responder preguntas utilizando **Gemini 2.5 Flash (GenAI)**.

Ruby puede:

- 🎤 Escuchar comandos por voz
- 🤖 Clasificar si el mensaje es una **pregunta** o una **orden**
- 🗣️ Responder preguntas mediante voz (Text-to-Speech)
- 💻 Convertir órdenes en comandos válidos de **Windows 10/11**
- 🔐 Bloquear comandos peligrosos automáticamente

---

## 🚀 Características

- ✅ Reconocimiento de voz con `speech_recognition`
- ✅ Clasificación inteligente con **Gemini 2.5 Flash**
- ✅ Conversión segura de órdenes a comandos Windows
- ✅ Protección contra acciones destructivas
- ✅ Respuesta hablada usando `pyttsx3`
- ✅ Configuración de rutas personalizadas mediante `paths.json`

---

## 🧠 ¿Cómo funciona?

1. El asistente escucha continuamente.
2. Si detecta la palabra clave **"Rubí"**, envía el texto a Gemini.
3. Gemini clasifica el mensaje como:
   - `question` → Ruby responde con voz.
   - `instruction` → Ruby lo convierte en un comando Windows seguro.
4. Si la orden es peligrosa, responde con:
   ```
   Impossible
   ```
   y muestra una notificación.

---

## 📂 Estructura del proyecto

```
📦 Ruby-Assistant
┃
┣ 📂 src
┃ ┣ 📂 config
┃ ┃ ┗ paths.json        # Rutas personalizadas
┃ ┣ 📂 utils
┃ ┃ ┣ command.py        # Lógica principal de voz
┃ ┃ ┣ genai_client.py   # Conexión con Gemini
┃ ┃ ┣ notify.py         # Notificaciones
┃ ┣ main.py             # Punto de entrada
┃
┣ 📜 .env
┣ 📜 .env.example
┣ 📜 requirements.txt
┣ 📜 README.md
┗ 📜 LICENSE
```

---

## 🔐 Seguridad

Ruby está diseñada para:

- ❌ No ejecutar comandos peligrosos
- ❌ No modificar archivos del sistema
- ❌ No acceder a carpetas críticas como:
  - System32
  - Windows
  - Program Files
  - Drivers
  - Registro de Windows

Si detecta una acción riesgosa, responde únicamente:

```
Impossible
```

---

## ⚙️ Variables de entorno

Crea un archivo `.env`:

```env
GEMINI_API_KEY=
```

---

## ▶️ Instalación

### 1️⃣ Clonar repositorio
```bash
git clone https://github.com/tuusuario/ruby-assistant.git
cd ruby-assistant
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar
```bash
python src/main.py
```

---

## 🗣️ Ejemplos de uso

🎤 "Rubí, ¿qué es inteligencia artificial?"  
➡ Ruby responde con voz.

🎤 "Rubí, crea una carpeta llamada proyectos"  
➡ Ruby genera el comando Windows correspondiente.

🎤 "Open chrome"  
➡ Abre Google Chrome si está en el PATH.

---

## 🛠️ Tecnologías usadas

- 🐍 Python
- 🎤 speech_recognition
- 🤖 Google Gemini 2.5 Flash (GenAI)
- 🗣️ pyttsx3 (Text-to-Speech)
- 📢 Sistema de notificaciones
- 💻 Windows 10 / 11

---

## 📌 Nota

Este proyecto fue creado como práctica para integrar:

- Inteligencia Artificial
- Reconocimiento de voz
- Automatización de sistema
- Seguridad en generación de comandos

---

## 📝 Licencia

MIT License
