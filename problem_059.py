#!/usr/bin/env python3
import re
import time


def blurb():
    print("""
            Each character on a computer is assigned a unique code and the
            preferred standard is ASCII (American Standard Code for Information
            Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
            lowercase k = 107.

            A modern encryption method is to take a text file, convert the bytes
            to ASCII, then XOR each byte with a given value, taken from a secret
            key. The advantage with the XOR function is that using the same
            encryption key on the cipher text, restores the plain text; for
            example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

            For unbreakable encryption, the key is the same length as the plain
            text message, and the key is made up of random bytes. The user would
            keep the encrypted message and the encryption key in different
            locations, and without both "halves", it is impossible to decrypt
            the message.

            Unfortunately, this method is impractical for most users, so the
            modified method is to use a password as a key. If the password is
            shorter than the message, which is likely, the key is repeated
            cyclically throughout the message. The balance for this method is
            using a sufficiently long password key for security, but short
            enough to be memorable.

            Your task has been made easy, as the encryption key consists of
            three lower case characters. Using cipher.txt (right click and 'Save
            Link/Target As...'), a file containing the encrypted ASCII codes,
            and the knowledge that the plain text must contain common English
            words, decrypt the message and find the sum of the ASCII values in
            the original text.
    """)


def get_possible_keys(cipher_text):
    '''
    Create list of all possible 3 letter keys
    '''
    possible_keys = []
    for lettera in range(97, 123):
        for letterb in range(97, 123):
            for letterc in range(97, 123):
                possible_keys.append([lettera, letterb, letterc])
    return possible_keys


def uncipher_text(text, cipher):
    unciphered_text = []
    for position, letter in enumerate(text):
        unciphered_text.append(chr(cipher[position % 3] ^ letter))
    return ''.join(unciphered_text)


def find_encryption_key(cipher_text):
    '''
    Given a list of common 3+ letterwords, loop over possible keys and count
    their occurrences, create a results dictionary to log all these results,
    return the key which produces the highest number of occurrences of
    common_words in the unciphered text
    '''
    common_words = ['the',
                    'and',
                    'that',
                    'have',
                    'for',
                    'not',
                    'with',
                    'you',
                    'this',
                    'but',
                    'his',
                    'from',
                    'they',
                    'say',
                    'she',
                    'will',
                    'one']
    possible_keys = get_possible_keys(cipher_text)
    results = {}
    for key in possible_keys:
        unciphered_string =  uncipher_text(cipher_text, key)
        for word in common_words:
            count = 0
            for find in re.finditer(word, unciphered_string):
                count += 1
            if count > 10:
                results[''.join([chr(x) for x in key])] = count
    most_possible_keys = {v: k for k, v in results.items()}
    return most_possible_keys[max(most_possible_keys.keys())]


def problem_059():
    with open('problem_059_cipher.txt', 'r') as f:
        cipher_file = f.read()
    cipher_text = [int(x) for x in cipher_file.split(',')]
    cipher_key = find_encryption_key(cipher_text)
    print('The encryption key is: %s' % cipher_key)
    unciphered_string = uncipher_text(cipher_text, [ord(x) for x in cipher_key])
    return sum([ord(x) for x in unciphered_string])


def main():
    blurb()
    start = time.time()
    RESULT = problem_059()
    end   = time.time() - start
    print("Result: %s"      % RESULT)
    print("Completed in %s" % end)


if __name__ == '__main__':
    main()
