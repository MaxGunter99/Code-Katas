
# Using Regex, return the numbers from a string.

import re
def returnNumbers( string , solution ):
    
    answer = ''.join( re.findall( "[0-9]" , string ) )

    if answer == solution:
        print( 'Pass' )
    else:
        print( 'Fail' )

returnNumbers( '' , '' )
returnNumbers( 'aBc' , '' )
returnNumbers( '123abc' , '123')
returnNumbers( '123abc456' , '123456')
returnNumbers( '1aA2bBb3sklajlak093874nk2j3nkj5b3kf98sd8f23n4289y' , '1230938742353988234289')