# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".


def disemvowel(string):

    vowels = { 'a', 'e', 'i' , 'o', 'u' , 'A', 'E', 'I', 'O', 'U' }
    newString = ''

    for i in string:

        if ( i in vowels ):
            None
        else:
            newString += i

    print( newString )
    return newString

disemvowel("This website is for losers LOL!") 
# "Ths wbst s fr lsrs LL!"