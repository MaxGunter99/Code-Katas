# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, 
# the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once 
# (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string

def is_pangram(s):

    alphabet = {
        'a': False,
        'b': False,
        'c': False,
        'd': False,
        'e': False,
        'f': False,
        'g': False,
        'h': False,
        'i': False,
        'j': False,
        'k': False,
        'l': False,
        'm': False,
        'n': False,
        'o': False,
        'p': False,
        'q': False,
        'r': False,
        's': False,
        't': False,
        'u': False,
        'v': False,
        'w': False,
        'x': False,
        'y': False,
        'z': False,
    }

    string = s.lower()

    for i in string:
        
        if i in alphabet and alphabet[i] is False:
            alphabet[i] = True

    if False in alphabet.values():
        print( 'False' )
        return False

    else:
        print( 'True' )
        return True

is_pangram("The quick, brown fox jumps over the lazy dog!") # True
# is_pangram( 'abcdefghij' ) # False