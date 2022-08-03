__morse_text__ = {
    '': " ",
    ' ': "",
    '.-': "a",
    '-...':"b",
    '-.-.':"c",
    '-..':"d",
    '.':"e",
    '..-.':"f",
    '--.':"g",
    '....':"h",
    '..':"i",
    '.---':"j",
    '-.-':"k",
    '.-..':"l",
    '--':"m",
    '-.':"n",
    '---':"o",
    '.--.':"p",
    '--.-':"q",
    '.-.':"r",
    '...':"s",
    '-':"t",
    '..-':"u",
    '...-':"v",
    '.--':"w",
    '-..-':"x",
    '-.--':"y",
    '--..':"z",
    '..--..':"?",
    '..--.':"!",
    '-----':"0",
    '.----':"1",
    '..---':"2",
    '...--':"3",
    '....-':"4",
    '.....':"5",
    '-....':"6",
    '--...':"7",
    '---..':"8",
    '----.':"9",
    '---...':":",
    '.-.-.-':".",
    '--..--':",",
    '-...-':"=",
    '-....-':"-"
}

__text_morse__ = {
    "a":'.-',
    "b":'-...',
    "c":'-.-.',
    "d":'-..',
    "e":'.',
    "f":'..-.',
    "g":'--.',
    "h":'....',
    "i":'..',
    "j":'.---',
    "k":'-.-',
    "l":'.-..',
    "m":'--',
    "n":'-.',
    "o":'---',
    "p":'.--.',
    "q":'--.-',
    "r":'.-.',
    "s":'...',
    "t":'-',
    "u":'..-',
    "v":'...-',
    "w":'.--',
    "x":'-..-',
    "y":'-.--',
    "z":'--..',
    ' ':'',
    '.':'.-.-.-',
    '-':'-....-',
    '!':'..--.'

}

def translate_character_morse(morse):
    return __morse_text__[morse]
    
def translate_string_morse(morse_string):
    morse_characters = morse_string.replace('/', "").split(' ')
    string = ""
    for morse in morse_characters:
        character = translate_character_morse(morse)
        string = f"{string}{character}"
    return string

def translate_character_text(text):
    return __text_morse__[text.lower()]

def translate_string_text(text_string):
    return_string = ""
    for text in text_string:
        return_string = f"{return_string}{translate_character_text(text)} "
    return return_string

def is_string_morse(string):
    list = ''.join(set(string.replace(' ','')))

    if len(list) == 2:
        if list[0] == '-':
            if list[1] == '.':
                return True
        elif list[0] == '.':
            if list[1] == '-':
                return True
        else:
            return False
    else:
        return False

def translate_string(string):
    if is_string_morse(string):
        return translate_string_morse(string)
    else:
        return translate_string_text(string)
