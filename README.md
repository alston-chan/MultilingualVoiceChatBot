# MultilingualVoiceChatBot
Learn a new language with our multilingual voice chatbot!

## Download and Install

pip:
 - Run `pip install -r requirements.txt`
 - Or manually install packages in `requirements.txt`

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
