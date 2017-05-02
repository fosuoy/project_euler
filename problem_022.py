#!/usr/bin/env python3
# Names Scores
# Solution to problem 22
# https://projecteuler.net/problem=22

from time import time

def blurb():
  print("""
  Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

  For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

  What is the total of all the name scores in the file?
  """)


def get_alphabetical_value(letter):
  alphabet = {'a': 1,  \
              'b': 2,  \
              'c': 3,  \
              'd': 4,  \
              'e': 5,  \
              'f': 6,  \
              'g': 7,  \
              'h': 8,  \
              'i': 9,  \
              'j': 10, \
              'k': 11, \
              'l': 12, \
              'm': 13, \
              'n': 14, \
              'o': 15, \
              'p': 16, \
              'q': 17, \
              'r': 18, \
              's': 19, \
              't': 20, \
              'u': 21, \
              'v': 22, \
              'w': 23, \
              'x': 24, \
              'y': 25, \
              'z': 26, \
             }
  FIND = letter.lower()
  return alphabet[FIND]

def main():
  start_time = time()

  blurb()

  TEXT_FILE_NAME = "problem_022_names.txt"
  COUNT = 0

  NAMES     = open(TEXT_FILE_NAME, "r").read()
  NAME_LIST = NAMES.strip('"').split('","')
  NAME_LIST.sort()
  NAME_SCORES = []

  for NAME in NAME_LIST:
    COUNT += 1
    SUM_OF_LETTERS = 0
    for letter in NAME:
      SUM_OF_LETTERS += get_alphabetical_value(letter)
    NAME_SCORES.append(SUM_OF_LETTERS * COUNT)
  end_time = str(time() - start_time)
  print("Sum of names as per rules: " + str(sum(NAME_SCORES)))
  print("Time taken: " + str(end_time) + " s")


if __name__ == '__main__':
  main()
