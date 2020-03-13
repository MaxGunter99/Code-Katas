# 4 kyu
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
# The range includes all integers in the interval including both endpoints. 
# It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")

def solution(args):

    answer = []
    recent = int()
    bank = []

    for i in args:

        if len( answer ) == 0:
            answer.append(i)

        else:

            if i == recent + 1:
                bank.append( i )

            else:

                if len( bank ) >= 2:
                    answer[ len( answer ) - 1 ] = str( answer[ len( answer ) - 1 ] ) + '-' + str( bank[ len( bank ) - 1 ] )
                    bank = []
                    answer.append(i)
                else:

                    if len( bank ) == 1:
                        answer.append( bank[0] )
                        bank = []
                    answer.append(i)

        recent = i

    if len( bank ) >= 2:
        answer[ len( answer ) - 1 ] = str( answer[ len( answer ) - 1 ] ) + '-' + str( bank[ len( bank ) - 1 ] )
    if len( bank ) == 1:
        answer.append( bank[0] )

    y = ''  
    for x in range( len( answer ) ):

        if x < len( answer ) - 1:
            y += str( answer[x] ) + ','
        else:
            y += str( answer[x] )

    print( y )
    return str(y)




# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) # '-6,-3-1,3-5,7-11,14,15,17-20'
# solution([-3,-2,-1,2,10,15,16,18,19,20]) # '-3--1,2,10,15,16,18-20'
# solution( [-68, -66, -63, -61, -60, -57, -54, -51, -49, -47, -46, -45, -44, -43, -41, -40, -37, -36, -35, -32, -29, -28, -26, -25, -24, -21, -20, -18, -17] ) # '-68,-66,-63,-61,-60,-57,-54,-51,-49,-47--43,-41,-40,-37--35,-32,-29,-28,-26--24,-21,-20,-18,-17'
# solution( [1,2,3,4,5,6,7,8,9 , 15,16 , 20] ) # 1-9,15,16,20

# solution( [-65, -62, -59, -57, -54, -53, -52, -49, -48, -45, -42, -40, -38, -37, -34, -33, -32, -30, -28, -27, -25, -24, -22, -21] ) # '-65,-62,-59,-57,-54--52,-49,-48,-45,-42,-40,-38,-37,-34--32,-30,-28,-27,-25,-24,-22,-21'

solution([-67, -66, -63, -62, -61, -60, -59, -58, -57, -56, -53, -52, -51, -49, -48])
# '-67,-66,-63--56,-53--51,-49,-48'