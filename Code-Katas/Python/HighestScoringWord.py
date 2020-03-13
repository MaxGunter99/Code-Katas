# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

def high(x):

    highest = 0
    word = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    splitUp = x.split( ' ' )
    
    for i in splitUp:
        
        wordSum = 0

        for x in i:

            wordSum += alphabet.index(x) + 1

        # check if number is higher than count or highest
        if wordSum > highest:
            print(i , wordSum)
            word = i
            highest = wordSum

    print( word )
    return word

# high('man i need a taxi up to ubud') # 'taxi'
# high('what time are we climbing up the volcano') # 'volcano'
# high('take me to semynak') # 'semynak'
# high( 'emjw ahql oyzodijju ftzar tmed otjnbp chdpqlsyp afztd rkit irxd rzl diftdwlvr badcrc fhwkzzqcaw nuksuv rcrbx yjrwfwnml pjijr' ) # fhwkzzqcaw