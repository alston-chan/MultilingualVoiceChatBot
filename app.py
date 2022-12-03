import gradio as gr

import sys
import os

from modules.transcribe_speech import transcribe_speech
from modules.romanize_text import romanize_text
from modules.translate_text import translate_text
from modules.generate_text import generate_text
from modules.synthesize_text import synthesize_text

import whisper
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)


def chat(input_audio, target_language):

    transcribed_input = transcribe_speech(
        input_audio, target_language, whisper_model)

    romanized_input = romanize_text(transcribed_input)
    translated_input = translate_text(transcribed_input, "en")

    bot_text_output = generate_text(
        godel_model, godel_tokenizer, '', '', translated_input, 0.9, 8, 64)
    bot_translated_text_output = translate_text(bot_text_output, "zh")

    audio_output_path = synthesize_text(bot_translated_text_output)

    return transcribed_input, romanized_input, translated_input, bot_translated_text_output, bot_text_output, audio_output_path


def system_setup():
    sys.stdout.reconfigure(encoding='utf-8')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys/language-learner-chatbot.json'


def create_app():
    with gr.Blocks() as app:
        with gr.Group():

            target_language = gr.Dropdown(
                ["Cantonese"], label="Target Language", show_label=True)

            with gr.Box():
                with gr.Row().style(equal_height=True):
                    input_audio = gr.Audio(
                        label="Input Audio",
                        show_label=True,
                        source="microphone",
                        type="filepath"
                    )

                    btn = gr.Button("Transcribe")

            text = gr.Textbox(
                label="Transcribed Input Text", show_label=True, elem_id="result-textarea")

            text_romanization = gr.Textbox(
                label="Romanized Input Text", show_label=True, elem_id="result-romanization-textarea")

            text_translation = gr.Textbox(
                label="Translated Input Text", show_label=True, elem_id="result-translation-textarea"
            )

            bot_translated_response_text = gr.Textbox(
                label="Bot Language Response", show_label=True, elemid='bot-language-response-textarea')

            bot_response_text = gr.Textbox(
                label="Bot Response", show_label=True, elemid="bot-response-textarea")

            bot_response_audio = gr.Audio(type="filepath",
                                          label="Bot Response Audio", show_label=True, elemid="bot-response-audio-audioarea")

            btn.click(chat, inputs=[
                input_audio, target_language], outputs=[text, text_romanization, text_translation, bot_translated_response_text, bot_response_text, bot_response_audio])
    return app


if __name__ == "__main__":

    system_setup()

    # Load Models
    godel_tokenizer = AutoTokenizer.from_pretrained(
        "microsoft/GODEL-v1_1-base-seq2seq")
    godel_model = AutoModelForSeq2SeqLM.from_pretrained(
        "microsoft/GODEL-v1_1-base-seq2seq")
    whisper_model = whisper.load_model("small")

    app = create_app()
    app.launch(share=True)
