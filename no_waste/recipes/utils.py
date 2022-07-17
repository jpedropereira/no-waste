from pygoogletranslation import Translator

def get_translation(text):
    """This method translates English to Portuguese"""
    translator = Translator()
    translation = translator.translate(text=text, src="en", dest="pt").text

    return translation
