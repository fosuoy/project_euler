#!/usr/bin/env python3
import time

def blurb():
  print("""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

  """)

def main():
  blurb()

  start = time.time()

  count               = 3
  fibonacci_sequence  = [1, 1, 2]
  target_digits       = 1000

  while len( str( fibonacci_sequence[2] ) ) < target_digits:
    fibonacci_sequence[0], fibonacci_sequence[1] = fibonacci_sequence[2], fibonacci_sequence[0]
    fibonacci_sequence[2] = fibonacci_sequence[1] + fibonacci_sequence[2]
    count += 1

  result = count

  end   = time.time() - start
  print("Result: %s" % result)
  print("Completed in %s" % end)

if __name__ == '__main__':
  main()
