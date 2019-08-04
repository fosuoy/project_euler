#!/usr/bin/env python3
import time


def problem_output(func, *args):
    def wrapper(*args):
        blurb()
        start = time.time()
        result = func(*args)
        time_to_end = time.time() - start
        print(f"Result: {result}")
        print(f"Completed in {time_to_end}")

    return wrapper


def blurb():
    print(
        """
    blurb
    """
    )


@problem_output
def problem():
    return 0


def main():
    problem()


if __name__ == "__main__":
    main()
