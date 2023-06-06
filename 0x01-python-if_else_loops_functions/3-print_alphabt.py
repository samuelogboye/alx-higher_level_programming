#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if chr(letter) == 'q' or chr(letter) == 'e':
        continue
    print("{}".format(chr(letter)), end="")
