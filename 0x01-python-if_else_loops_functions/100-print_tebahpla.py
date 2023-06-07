#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(i)}" if i % 2 == 0 else f"{chr(i).upper()}", end="")
