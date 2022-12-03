from google.cloud import translate_v2 as translate


def translate_text(input_text, target_language):

    translate_client = translate.Client()

    translation = translate_client.translate(
        input_text, target_language=target_language)  # ru

    print(u"Text: {}".format(input_text))
    print(u"Translation: {}".format(translation["translatedText"]))

    return translation["translatedText"]
