#!/usr/bin/python
# Number letter counts
# https://projecteuler.net/problem=17
# Sum of letters when all numbers from one
# to one thousand are written out.

import time

number_list = list(range(1,1001))

number_words_digits = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
                       6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
number_words_teens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', \
                      14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', \
                      17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
number_words_tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', \
                     5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', \
                     9: 'Ninety' }

def number_to_word(integer):
    string = ''
    while integer > 0:
        if integer >= 1000:
            thousands = integer / 1000
            string = string + number_words_digits[thousands] + " Thousand "
            integer = integer - (thousands * 1000)
        elif integer >= 100:
            hundreds = integer / 100
            string = string + number_words_digits[hundreds] + " hundred "
            if integer % 100 != 0:
                string = string + "and "
            integer = integer - (hundreds * 100)
        elif 100 > integer >= 20:
            number = integer / 10
            string = string + number_words_tens[number] + " "
            integer = integer - (number * 10)
        elif 20 > integer > 10:
            string = string + number_words_teens[integer]
            break
        elif 10 >= integer > 0:
            string = string + number_words_digits[integer]
            break
    string = string.capitalize()
    return string

number_of_letters = lambda x: len(number_to_word(x).replace(" ", ""))



start = time.time()
result = 0
for number in number_list: result += number_of_letters(number)
elapsed = time.time() - start
 
print("Result %s found in %s seconds" % (result, elapsed))
