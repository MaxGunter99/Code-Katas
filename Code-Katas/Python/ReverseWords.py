# RUN WITH: python code-katas/python/ReverseWord.py

# Given a string, return the string reversed

def reverseWords( text ):

    if text and not isinstance( text, str ):
        return text

    returnValue = None

    splitString = text.split( " " )
    # print( splitString )

    for index in range( len( splitString ) ):

        setWord = splitString[ index ]

        reversedWord = setWord[::-1]
        # print( reversedWord )
        
        if not returnValue:
            returnValue = ""

        optionalSpace = ""
        if len( splitString ) > 1 and index + 1 < len( splitString ):
            optionalSpace = " "

        returnValue += f"{reversedWord}{optionalSpace}"
        

    print( f"|{returnValue}|" )
    return returnValue


# reverseWords( 'This is an example!' )
# reverseWords( 'double  spaces' )
reverseWords( 'a b c d' )