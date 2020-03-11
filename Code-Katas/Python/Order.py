# Your task is to sort a given string. 
# Each word in the string will contain a single number. 
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(sentence):

    if sentence == '':
        print('Empty')
        return ''

    else:
        sentence = sentence.split(' ')
        answer = ''
        count = 1
        index = 0

        while len( sentence ):
            index = 0

            for i in sentence:

                if str( count ) in i:

                    print( i )

                    if len(answer) == 0:
                        answer += i
                        sentence.pop( index )
                    else:
                        answer += ( ' '+ i )
                        sentence.pop( index )

                print( i )
                index += 1

            count += 1
            print( sentence )

        print( 'Answer:' , answer )
        return answer

# order("") # ""
order("is2 Thi1s T4est 3a") # "Thi1s is2 3a T4est"
# order("4of Fo1r pe6ople g3ood th5e the2") # "Fo1r the2 g3ood 4of th5e pe6ople"