
# Using Regex, return the numbers from a string.

import re
def returnLetters( string , solution ):

    answer = ''.join( re.findall( "[a-zA-z]" , string ) )

    if answer == solution:
        print( 'Pass' )
    else:
        print( 'Fail' )

returnLetters( '' , '')
returnLetters( '123' , '')
returnLetters( '123abc' , 'abc')
returnLetters( '123aBc456' , 'aBc')
returnLetters( '1aA2bBb3sklajlak093874nk2j3nkj5b3kf98sd8f23n4289y' , 'aAbBbsklajlaknkjnkjbkfsdfny')