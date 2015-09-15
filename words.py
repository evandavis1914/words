import random
import subprocess
import time

import assets
from color import Colorize


def get_input(prompt):
    return input(prompt).upper()
    # with ReadChar() as rc:
    #     char = rc.upper()
    #     if char in ['\x03']:
    #         sys.exit()
    #     return char


def check_input(guess, word):
    pressed_phrase = get_phrase('pressed').format(guess)
    voice = get_random_voice()
    say_phrase(pressed_phrase, voice)
    if guess == word:
        color = 'FG_BOLD_GREEN'
        text = '\n{}\n'.format(assets.OK)
        print(Colorize.colorize(color, text))
        say_phrase(get_phrase('correct'), voice)
        return True
    else:
        color = 'FG_BOLD_RED'
        text = '\n{}\n'.format(assets.X)
        print(Colorize.colorize(color, text))
        say_phrase(get_phrase('wrong'), voice)
        return False


def get_random_color():
    return random.choice(list(Colorize.colors.keys()))


def get_word():
    return random.choice(list(assets.BLOCKS.keys()))


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


def display_word(word):
    color = get_random_color()
    # TODO # implement word format of individual letters)
    # text = '\n{}\n'.format(# implement word format of individual letters)
    print(Colorize.colorize(color, text))


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
