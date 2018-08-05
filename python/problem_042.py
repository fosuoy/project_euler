#!/usr/bin/env python3
import time

def blurb():
    print("""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
    """)

def get_word_list(file_name):
    '''
    Santize the word list if words are just one long string
    '''
    remove_dble_quote = lambda x: x.replace('"', '')
    with open(file_name, 'r') as f:
        words = f.read()
    words = words.split('","')
    len_words = len(words) - 1
    words[0] = remove_dble_quote(words[0])
    words[len_words] = remove_dble_quote(words[len_words])
    return words

def get_letter_dict():
    n = 1
    letter_dict = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letter_dict[letter] = n
        n += 1
    return letter_dict

def find_triangle_words(file_name):
    '''
    First get a sanitized list of words
    Then get a list of triangle numbers
    Finally go through the list of words calculating their sum and checking if
    they appear in the list of triangle numbers
    '''
    triangle_number = lambda x: 0.5 * x * (x + 1)
    words = get_word_list(file_name)
    longest_word = max(words, key=len)
    longest_word_length = len(longest_word)
    upper_bound = longest_word_length * 26
    triangle_numbers = [triangle_number(x) for x in range(1,upper_bound)]
    letter_dict = get_letter_dict()

    result_sum = 0
    result_words = []
    for word in words:
        word_sum = 0
        for letter in word:
            word_sum += letter_dict[letter]
        if word_sum in triangle_numbers:
            result_sum += 1
            result_words.append(word)
    print("Triangle words:")
    print(result_words)
    return result_sum

def main():
    blurb()
    start = time.time()
    RESULT = find_triangle_words('problem_042_words.txt')
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)

if __name__ == '__main__':
    main()
