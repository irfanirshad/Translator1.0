from translate import *
import sys

print("""\

 _____ _     _ _   _           _____                   _       _               __   _____
/  ___| |   (_) | | |         |_   _|                 | |     | |             /  | |  _  |
\ `--.| |__  _| |_| |_ _   _    | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __  `| | | |/' |
 `--. \ '_ \| | __| __| | | |   | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|  | | |  /| |
/\__/ / | | | | |_| |_| |_| |   | | | | (_| | | | \__ \ | (_| | || (_) | |    _| |_\ |_/ /
\____/|_| |_|_|\__|\__|\__, |   \_/_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|    \___(_)___/
                        __/ |
                       |___/

 \n \n """)


print(" Welcome to Shitty Translator 1.0!  \n")

print(" Type the language of the word or sentence you wish to translate to or from English \n ")

input

Translating = True

while Translating:
    lang = input(" Type any language \n ")
    word = input(
        "Type any word or sentence of the above mentioned language to be translated to " + str(lang) + " \n ")

    translator = Translator(to_lang=lang)
    translate = translator.translate(word)
    print(translate)

    stop = input(" Do you wish to translate again? Y/n ")
    if stop == 'y' or "Y":
        Translating
    else:
        Translating = False
        exit()
