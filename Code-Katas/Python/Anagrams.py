
# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters

def anagrams(word, words):

    print( word )
    bank = {}
    answer = []

    for i in word:
        if i not in bank.keys():
            bank[i] = word.count(i)


    for i in range( len( words ) ):
        count = 0

        for x in range( len( words[i] ) ):

            if words[i][x] not in bank.keys():
                pass

            elif words[i].count(words[i][x]) == bank[words[i][x]]:
                count += 1

        if count == len( words[i] ):
            answer.append( words[i] )
            
    print( answer )
    return answer

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) # ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) # ['carer', 'racer']