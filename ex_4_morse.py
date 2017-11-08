def translate_to_morse(str):
    """
    Translate the word str to morse
    :param str: the word you want to translate
    :return: the translated word
    """

    code = {
        'A': '.-', 'B': '-..', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
    }

    translated_word = ''
    for letter in str:
        if letter.upper() in code:
            translated_word += code[letter.upper()] + '/'

    print(translated_word)


translate_to_morse('SOS')
