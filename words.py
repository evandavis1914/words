import random
import subprocess
import time

import assets
import vocabulary
from color import Colorize


def get_input(prompt):
    return input(prompt).lower()


def check_input(guess, word):
    voice = get_random_voice()
    if guess == word:
        color = 'FG_BOLD_GREEN'
        text = '\n{}\n'.format(assets.OK)
        print(Colorize.colorize(color, text))
        say_phrase(get_phrase('correct'), voice)
        say_correct_spelling(word, voice)
        return True
    else:
        color = 'FG_BOLD_RED'
        text = '\n{}\n'.format(assets.X)
        print(Colorize.colorize(color, text))
        say_phrase(get_phrase('wrong'), voice)
        return False


def say_correct_spelling(word, voice):
    phrase = '{} is spelled {}.'.format(word, ' '.join(list(word)))
    voice = get_random_voice()
    say_phrase(phrase, voice)


def get_random_color():
    return random.choice(list(Colorize.colors.keys()))


def get_phrase(key):
    return random.choice(assets.PHRASES[key])


def get_random_voice():
    return random.choice(assets.VOICES)


def say_phrase(sentence, voice):
    cmd = "say -v '{}' '{}'".format(voice, sentence)
    execute_shell_command(cmd)


def say_word(word):
    phrase = get_phrase('word').format(word)
    voice = get_random_voice()
    say_phrase(phrase, voice)


def execute_shell_command(cmd):
    subprocess.call(cmd, shell=True)


def get_letters_from_assets(word):
    spelling = []
    for letter in word.upper():
        x = assets.BLOCKS[letter]
        spelling.append(x)
    return spelling


def display_word(word):
    letters = get_letters_from_assets(word)
    color = get_random_color()
    text = ''
    for pos in range(6):
        for letter in letters:
            text += '{}'.format(letter[pos])
        text += '\n'
    print(Colorize.colorize(color, text))


def get_word():
    return random.choice(vocabulary.WORDS).lower()


def prompt():
    return '\nEnter the word :>>> '


def interact(word):
    execute_shell_command('clear')
    display_word(word)
    say_word(word)


def main():
    print(get_phrase('exit'))
    time.sleep(3)
    while True:
        word = get_word()
        interact(word)
        correct = False
        while not correct:
            guess = get_input(prompt())
            correct = check_input(guess, word)
            if not correct:
                interact(word)


if __name__ == '__main__':
    main()
