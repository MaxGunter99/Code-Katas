
def mix(s1, s2):


    print( s1 , s2 )

    one = {}
    two = {}
    shared = {}

    for x , y in zip( s1 , s2 ):

        if x.islower():
            if x not in one:
                one[ x ] = 0
            else:
                one[ x ] += 1

        if y.islower():
            if y not in two:
                two[ y ] = 0
            else:
                two[ y ] += 1

    

    # print( one )
    # print( two )

            

mix("Are they here", "yes, they are here") # "2:eeeee/2:yy/=:hh/=:rr"
# mix("looping is fun but dangerous", "less dangerous than coding") # "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
# mix(" In many languages", " there's a pair of functions") # "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
# mix("Lords of the Fallen", "gameuklt") # "1:ee/1:ll/1:oo"
# mix("codewars", "codewars") # ""
# mix("A generation must confront the looming ", "codewarrs") # "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"