# RUN WITH: python code-katas/python/ReverseString.py

# Given a string, return the string reversed

# regex
import re

def reverseString ( string ):

    x = len( string )

    word = ''

    while x > 0:
        x = x - 1
        if re.match( r"^[A-Za-z]+$" , string[x] ):
            word = word + string[x]

    print( word )
    return word


reverseString( 'HelloWorld!!!' )
reverseString( 'AbCd3F' )