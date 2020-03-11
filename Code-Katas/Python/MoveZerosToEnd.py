# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):

    if 0 in array:

        answer = []
        zeros = []

        for i in range( len( array ) ):

            if type( array[i] ) is int or type( array[i] ) is float :

                # Number
                if int( array[i] ) is not 0:
                    answer.append( array[i] )

                else:
                    zeros.append( 0 )

            else:
                # Other
                answer.append( array[i] )

        for i in zeros:
            answer.append( 0 )

        print( answer ) 
        return answer

    else:

        print( array )
        return array

# move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) 
# [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  

# move_zeros([1,2,0,1,0,1,0,3,0,1]) 
# [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])

# move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) 
# [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

# move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) 
# ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

# move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) 
# ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]

# move_zeros([0,1,None,2,False,1,0]) 
# [1,None,2,False,1,0,0]

# move_zeros(["a","b"]) 
# ["a","b"] 

# move_zeros(["a"]) 
# ["a"]

# move_zeros([0,0]) 
# [0,0]

# move_zeros([0]) 
# [0]

# move_zeros([False]) 
# [False]

# move_zeros([]) 
# []