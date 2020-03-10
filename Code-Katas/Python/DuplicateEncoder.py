# Convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string
# or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

# import os
# os.system('clear')

def duplicate_encode(word):

    word = word.lower()
    answer = ''

    for i in word:

        occurance = word.count(i)

        if occurance == 1:
            answer += '('

        else:
            answer += ')'

    print( answer )
    return answer


# duplicate_encode("din") # "((("
# duplicate_encode("recede") # "()()()"
# duplicate_encode("Success") # ")())())","should ignore case"
# duplicate_encode("(( @") # "))(("