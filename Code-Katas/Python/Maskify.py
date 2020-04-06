# return masked string
def maskify(cc):

    if len( cc ) >= 4:
        print( '#' * len( cc[:len(cc) - 4] ) + cc[-4:] )
        return '#' * len( cc[:len(cc) - 4] ) + cc[-4:]
    else:
        print( cc ) 
        return cc

maskify( "123" ) # "123"
maskify( "Skippy" ) # "##ippy"
maskify("Nananananananananananananananana Batman!") # "####################################man!"