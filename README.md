# MultilingualVoiceChatBot
Learn a new language with our multilingual voice chatbot!

## Recommended Use of Virtual Environments

Use virtual environments to manage packages so you don't break local machine versions:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Useful commands listed for convenience: 

- ### Installing venv (virtual environment)
  `python3 -m pip install --user virtualenv`

- ### Creating and Activating venv 
  `python3 -m venv env_name` \
  `source env_name/bin/activate`

- ### Installing in virtual env using requirements.txt 
  `python3 -m pip install -r requirements.txt`

## Download and Install

pip:
 - Run `pip install -r requirements.txt`
 - Or manually install packages in `requirements.txt`
 - Or skip if using virtual enviornments

Google Cloud Setup:

 1. Enable API: https://cloud.google.com/translate
 2. Enable API: https://cloud.google.com/text-to-speech
 3. Authenticate: Download private key JSON from service account and move to `keys/language-learner-chatbot.json`

## Modules

Transcribe Speech: 
 - https://github.com/openai/whisper 
 - Run `choco install ffmpeg` for Windows or `brew install ffmpeg` for MacOS

Romanize Text:
 - https://github.com/jacksonllee/pycantonese
 - https://github.com/lxneng/xpinyin

Translate Text:
 - https://github.com/googleapis/python-translate

Generate Text:
 - https://github.com/microsoft/GODEL

Synthesize Text:
 - https://github.com/googleapis/python-texttospeech
