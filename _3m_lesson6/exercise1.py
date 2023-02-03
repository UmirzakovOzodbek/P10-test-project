from translate import Translator

translator = Translator(to_lang="uz")
translation = translator.translate("This is a pen.")

print(translation)
