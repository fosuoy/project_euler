#!/usr/bin/env python3
import time

def blurb():
    print("""
    blurb
    """)

def main():
    blurb()
    start = time.time()
    RESULT = ""
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
