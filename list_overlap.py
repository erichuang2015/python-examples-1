#!/usr/bin/env python3
# this program finds common numbers from two list and prints those number
import random

def common():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(f"{a}")
    print(f"{b}")
    c = []
    for x in a:
       if x in b:
           if x not in c:
               c.append(x)
    print(c)

if __name__ == '__main__':
    common()
