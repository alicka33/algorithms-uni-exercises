import sys

DICT_LETTERS = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
}


def check_chart(letter):
    return letter <= 'Z' and letter >= 'A' or letter == ' '


def good_line(line):
    line_good = ''
    line = line.upper()
    for letter in line:
        if check_chart(letter):
            line_good += letter
    return line_good


def open_file(file_name):
    with open(file_name) as f:
        return f.readlines()


def translate_to_morse(file_name):
    translate_file = []
    lines = open_file(file_name)
    for line in lines:
        line_in_morse = ''
        line = good_line(line)
        words = line.split()
        for word in words:
            for letter in word:
                line_in_morse += DICT_LETTERS[letter]+' '
            line_in_morse += '/ '
        translate_file.append(line_in_morse)
    return translate_file


def show_translation(translate_file):
    for line_in_morse in translate_file:
        print(line_in_morse[:-2])


def main():
    file_name = sys.argv[1]
    translate_file = translate_to_morse(file_name)
    show_translation(translate_file)


if __name__ == "__main__":
    main()
