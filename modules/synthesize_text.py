from google.cloud import texttospeech


def synthesize_text(input_text):
    client = texttospeech.TextToSpeechClient()
    input = texttospeech.SynthesisInput(text=input_text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        # language_code="en-US",
        language_code="yue-HK",
        # name="en-US-Wavenet-J",
        name="yue-HK-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        request={"input": input, "voice": voice,
                 "audio_config": audio_config}
    )
    # The response's audio_content is binary.
    with open("audio/output.mp3", "wb") as out:
        out.write(response.audio_content)

    print('Audio content written to file "audio/output.mp3"')
    return "audio/output.mp3"
