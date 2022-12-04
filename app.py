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

    return transcribed_input, romanized_input, translated_input


def respond(translated_input):
    bot_text_output = generate_text(
        godel_model, godel_tokenizer, '', '', translated_input, 0.9, 8, 64)

    bot_translated_text_output = translate_text(bot_text_output, "zh-TW")
    bot_romanized_text_output = romanize_text(bot_translated_text_output)

    audio_output_path = synthesize_text(bot_translated_text_output)

    return bot_translated_text_output, bot_romanized_text_output, bot_text_output, audio_output_path


def system_setup():
    sys.stdout.reconfigure(encoding='utf-8')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys/language-learner-chatbot.json'


def create_app():
    with gr.Blocks() as app:
        with gr.Group():

            target_language = gr.Dropdown(
                ["Cantonese"], label="Target Language", show_label=True)

            with gr.Row().style(equal_height=True):
                with gr.Box():
                    with gr.Column():
                        user_input_audio = gr.Audio(
                            label="User Input Audio", show_label=True, source="microphone", type="filepath")

                        transcribe_button = gr.Button("Transcribe")

                        user_transcribed_text = gr.Textbox(
                            label="User Transcribed Text", show_label=True)

                        user_romanized_text = gr.Textbox(
                            label="User Romanized Text", show_label=True)

                        user_translated_text = gr.Textbox(
                            label="User Translated Text", show_label=True)
                with gr.Box():
                    with gr.Column():
                        bot_output_audio = gr.Audio(
                            label="Bot Output Audio", show_label=True, type="filepath")

                        generate_response_button = gr.Button(
                            "Generate Response")

                        bot_transcribed_text = gr.Textbox(
                            label="Bot Transcribed Text", show_label=True)

                        bot_romanized_text = gr.Textbox(
                            label="Bot Romanized Text", show_label=True)

                        bot_translated_text = gr.Textbox(
                            label="Bot Translated Text", show_label=True)

            transcribe_button.click(chat,
                                    inputs=[user_input_audio, target_language],
                                    outputs=[user_transcribed_text, user_romanized_text, user_translated_text])

            generate_response_button.click(respond,
                                           inputs=[user_translated_text],
                                           outputs=[bot_transcribed_text, bot_romanized_text, bot_translated_text, bot_output_audio])
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
