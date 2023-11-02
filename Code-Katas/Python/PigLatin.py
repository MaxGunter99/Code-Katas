
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):

    # SOLUTION 1:
    # my_arr = []
    # for i in text.split(" "):
    #     if i[0] not in "0987654321!@#$?/><,.%^&*()_-+=":
    #         my_word = i[1:] + i[0] + "ay"
    #     else:
    #         my_word = i[0]
    #     my_arr.append( my_word )
    # return_value = " ".join(my_arr)
    # return return_value

    # SOLUTION 2:
    return " ".join(
        [ i[1:] + i[0] + "ay" if i[0] not in "0987654321!@#$?/><,.%^&*()_-+=" else i[0] for i in text.split(" ") ]
    )

    # others used isalpha rather than the special character string

pig_it( "Hello World !" )
