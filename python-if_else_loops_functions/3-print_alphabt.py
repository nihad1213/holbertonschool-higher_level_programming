#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != '1' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end='')
