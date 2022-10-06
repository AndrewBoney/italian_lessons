import gtts, os, IPython

def save_text_mp3(text: str, loc: str, lang: str = "it"): gtts.gTTS(text, lang = "it").save(loc)    

def say_word(word: str, loc: str = "saved_words", lang: str = "it"):
    os.makedirs(loc, exist_ok = True)
    gtts.gTTS(word, lang = "it").save(f"{loc}/{word}.mp3")
    display(word, IPython.display.Audio(f"{loc}/{word}.mp3"))