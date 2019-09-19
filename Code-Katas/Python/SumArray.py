# Add every item from an array

def sum (numbers):

    count = [0]

    for i in range( len( numbers ) ):

        count.append( numbers[i] + count[i] )


    print( count[ len( count ) - 1 ] )
    return count[ len( count ) - 1 ] 

sum([]), '0'
sum([1, 5.2, 4, 0, -1]) , '9.2'