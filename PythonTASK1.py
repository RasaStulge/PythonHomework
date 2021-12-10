# TASK1
# Write a program that will convert the sequence of numbers entered by the user into text, e.g .:
# 112 -> "one one two"
# 9973 -> "nine nine seven three"
# Hint: you need the input () function, a dictionary and a loop
from typing import List


numbers = {0: 'zero', 1: 'one',
          2: 'two', 3: 'three',
          4: 'four', 5: 'five',
          5: 'six', 7: 'seven',
          8: 'eight', 9: 'nine'
          }


def num_to_text(num):
    answer_text = 0
    for text in num.lower():
        answer_text += number[text]
    return answer_text


if __name__ == '__main__':
    while True:
        my_text = input('Give a word: ').strip()
        number = num_to_text(my_text)
        print(f'Text {my_text} is converted {number} value')
        shall_continue = input('Do you want to continue ([y]/n])?: ')
        if shall_continue.lower() != 'y':
            break
