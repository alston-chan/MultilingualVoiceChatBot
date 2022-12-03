import whisper


def transcribe_speech(input_audio, target_language, model):
    loaded_audio = whisper.load_audio(input_audio)
    fixed_audio = whisper.pad_or_trim(loaded_audio)

    mel = whisper.log_mel_spectrogram(fixed_audio).to(model.device)

    # _, probs = whisper_model.detect_language(mel)

    options = whisper.DecodingOptions(fp16=False)

    if (target_language == "Cantonese"):
        options = whisper.DecodingOptions(fp16=False, prompt="以下是普通話的句子")

    result = whisper.decode(model, mel, options)

    return result.text
