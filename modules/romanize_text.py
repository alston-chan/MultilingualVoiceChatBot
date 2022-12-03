import re
import pycantonese
#from xpinyin import Pinyin


def romanize_text(input_text):
    cantonese_segments = pycantonese.characters_to_jyutping(input_text)
    cantonese_sentence = ""
    for segment in cantonese_segments:
        if (segment[1] == None):
            cantonese_sentence += segment[0]
        else:
            cantonese_sentence += segment[1]
    cantonese_sentence_spaced = re.sub(
        "[A-Za-z]+", lambda ele: " " + ele[0], cantonese_sentence)
    return cantonese_sentence_spaced
