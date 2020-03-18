# given a string of text (possibly with punctuation and line-breaks), 
# returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# Matches should be case-insensitive, and the words in the result should be lowercased.

import re

def top_3_words(text):
    dict = {}
    text = re.sub(r"[^a-zA-Z0-9']+", ' ', text)
    split = text.split(' ')


    for i in split:

        current = i.lower()

        if current == ' ' or current == '' or current == "'" or current == "''" or current == "'''":
            None

        else:
            if current in dict:
                dict[current] += 1

            else:
                dict[current] = 1

    if dict == {}:
        print( 'Empty' )
        return []

    else: 

        answer = []

        for x in dict:
            answer.append( [ x , dict[x] ] )

        for x in range( len( answer ) ):
            current = answer[x]
            currentValue = answer[x][1]
            prev = answer[x - 1]
            prevValue = answer[x - 1][1]

            if currentValue > prevValue:
                answer.pop( x )
                index = x

                while currentValue >= answer[index - 1][1]:

                    if index == 0:
                        break

                    else:
                        index -= 1

                answer.insert( index, current )

        formatted = []
        for x in answer[:3]:
            formatted.append( x[0] )

        print( formatted )
        return formatted


top_3_words("a a a  b  c c  d d d d  e e e e e") # ["e", "d", "a"]
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e") # ["e", "ddd", "aa"]
# top_3_words("  //wont won't won't "), # ["won't", "wont"]
# top_3_words("  , e   .. ") # ["e"]
# top_3_words("  ...  ") # []
# top_3_words("  '  ") # []
# top_3_words("  '''  ") # []
# top_3_words("""In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.""") 
# ["a", "of", "on"]
# top_3_words( "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e" )
# top_3_words("gQxALiVV?/lSdGZ !-,PZaNgWVklQ?,_oAOXWD-:__PZaNgWVklQ-// iyr.;oAOXWD/_oAOXWD ,!PZaNgWVklQ :;;;kwrr/oAOXWD-!lSdGZ/ -epaHMO!:!;oAOXWD;;..?PZaNgWVklQ-:/?PZaNgWVklQ ! iyr,:lqqOlkdevD -,;_kwrr-,oAOXWD;PZaNgWVklQ-/.PZaNgWVklQ_!  oAOXWD!_.PZaNgWVklQ;iyr,?,:oAOXWD!::gQxALiVV;.!..gQxALiVV::!epaHMO :iyr.iyr!,iyr,---gQxALiVV;_,-gQxALiVV!!; PZaNgWVklQ,?;?;epaHMO;. _epaHMO?.;iyr!;??.epaHMO.gQxALiVV?., oAOXWD-gQxALiVV_,!epaHMO-:.PZaNgWVklQ!/!lqqOlkdevD._epaHMO.- ,epaHMO/.;;-iyr_gQxALiVV_??oAOXWD!oAOXWD;,?/,lqqOlkdevD ?epaHMO!!!YYy'ec?_iyr ..:gQxALiVV:;.PZaNgWVklQ?;.;h'pnz!!!!nLQ,;..gQxALiVV__!!lSdGZ-,/,lSdGZ-gQxALiVV.-.!lqqOlkdevD:,iyr . :!PZaNgWVklQ,:oAOXWD--. iyr! ;gQxALiVV. kwrr!;;kwrr?,iyr,-?gQxALiVV :iyr; lSdGZ;,PZaNgWVklQ?:;!_lqqOlkdevD ; lSdGZ:-;,:gQxALiVV;,; !lqqOlkdevD;!!_lqqOlkdevD_. oAOXWD__oAOXWD?;,gQxALiVV:/epaHMO?PZaNgWVklQ:?/_:lSdGZ//.- iyr;_oAOXWD/!?,epaHMO!;.:PZaNgWVklQ..?.PZaNgWVklQ?:;?epaHMO?,iyr/-,,gQxALiVV/!_-epaHMO -/-/gQxALiVV,!/-!iyr-:epaHMO ;/;:nLQ/PZaNgWVklQ?,/!oAOXWD_:__iyr;.:!;iyr--_ :PZaNgWVklQ!/:-lSdGZ:gQxALiVV__;_iyr -PZaNgWVklQ,! iyr!gQxALiVV,:oAOXWD_;? /epaHMO__YYy'ec:?_oAOXWD gQxALiVV,?oAOXWD,;epaHMO  /PZaNgWVklQ !/:oAOXWD.!_PZaNgWVklQ?!.gQxALiVV, :--iyr-_oAOXWD?PZaNgWVklQ:gQxALiVV_!?/epaHMO! :?oAOXWD/_--iyr.,;,lSdGZ? ?:.lSdGZ-_epaHMO,_!PZaNgWVklQ-_-._kwrr:_  ;gQxALiVV;;_,:PZaNgWVklQ-!-  oAOXWD: !-?gQxALiVV_?;;iyr-gQxALiVV;-?-iyr --gQxALiVV; ?,epaHMO-!gQxALiVV/!,lSdGZ: kwrr?., epaHMO kwrr;_?,gQxALiVV;:!_/oAOXWD?.nLQ._?!.YYy'ec,iyr/!oAOXWD//-lqqOlkdevD/.oAOXWD_.gQxALiVV :://lSdGZ,,,kwrr ;!lqqOlkdevD_lqqOlkdevD:.PZaNgWVklQ //:iyr,.,;!lSdGZ_,PZaNgWVklQ:;oAOXWD:!iyr_- /epaHMO-!:/kwrr-_!-;lqqOlkdevD, lSdGZ/  iyr,epaHMO-,?,oAOXWD,_-/lSdGZ!;-/.kwrr-oAOXWD ?_oAOXWD.!:epaHMO-;.?/iyr-!:?epaHMO;.;_iyr- /lqqOlkdevD:;./PZaNgWVklQ?;:gQxALiVV;lSdGZ:kwrr,! ;-PZaNgWVklQ, _ ?lqqOlkdevD:_!:PZaNgWVklQ! /")