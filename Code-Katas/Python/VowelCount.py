# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    return sum( [ 1 if letter in "aeiou" else 0 for letter in sentence ] )
    

assert get_count("x", 0)
assert get_count("a", 1)
assert get_count("allllllllllllllli", 2)