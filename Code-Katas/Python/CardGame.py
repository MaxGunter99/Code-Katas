# Card Game Simulator

# EGYPTION RAT-SCREW

# RULES:

# the deck is distributed between all players
# nobody sees their cards
# everyone puts down the card at the top of their deck one by one

# they try to find matches, if they find a match and slap the deck then they get whats on the table
# Doubles [ 2 , 2 ]
# sandwiches [ k , 1 , k ]

# if someone places a face card [ A , J , Q , K ] 
# the next person has to place a certain amount of cards down-
# A = 1
# J = 2
# Q = 3
# K = 4

# if they do not put a face card down, the person who placed the fact card gets the deck

import random
import os

os.system( 'clear' )

# This is the original ( sorted ) deck of cards
sortedCards = [ 
    2 , 2 , 2 , 2 , 
    3 , 3 , 3 , 3 ,
    4 , 4 , 4 , 4 ,
    5 , 5 , 5 , 5 ,
    6 , 6 , 6 , 6 ,
    7 , 7 , 7 , 7 ,
    8 , 8 , 8 , 8 ,
    9 , 9 , 9 , 9 ,
    10 , 10 , 10 , 10 ,
    'ACE' , 'ACE' , 'ACE' , 'ACE' ,
    'JACK' , 'JACK' , 'JACK' , 'JACK' ,
    'QUEEN' , 'QUEEN' , 'QUEEN' , 'QUEEN' ,
    'KING' , 'KING' , 'KING' , 'KING'
]

faceCards = { 'KING':4 , 'QUEEN':3 , 'JACK':2 , 'ACE':1 }

# --------- Shuffle The Deck ---------

playableDeck = [ 0 ] * len( sortedCards )
unavailableSpots = []

for i in range( len( sortedCards ) ):

    current = sortedCards[i]
    index = random.randint(0 , len( sortedCards ) - 1 )

    if index in unavailableSpots:

        while index in unavailableSpots:
            index = random.randint(0 , len( sortedCards ) - 1 )

    unavailableSpots.append( index )
    playableDeck[ index ] = current

# Shuffled Deck!
# print( playableDeck )

# Hand out cards to amount of players
numberOfPlayers = input( 'How many people are playing?\n' )
numberOfPlayers = int( numberOfPlayers )

# Setting up players with cards and what is on the table
players = {}
table = []

for i in range( numberOfPlayers ):

    players[ i ] = []

count = 0

for i in playableDeck:

    if count == numberOfPlayers:
        count = 0
    
    players[ count ].append( i )
    count = count + 1

# game will be a while loop
playing = True
count = 0
moves = 0
faceCard = False

# --------- Start Game ---------

f = open("CardGame.txt", "w")
f.write( '--------- Start Game ---------\n' )
f.write( f'Playing: {numberOfPlayers}\n\n' )

while playing == True:

    # current player and the card they will put down
    currentPlayer = players[ count ]

    # if a player has the full deck
    if len( currentPlayer ) == len( sortedCards ):

        f.write( f'\nPlayer: {count} Wins!\n' )
        f.write( f'All moves in game: {moves}\n' )
        f.write( f'Player {count} has: {players[count]}\n' )

        playing = False
        break

    # if a player has cards
    if len( currentPlayer ) >= 1:

        currentPlayersCard = currentPlayer[0]

        # if someone placed a face card
        if faceCard == True:

            f.write( f'\nPlayer: {count} is faced with a FACE CARD:\n' )
            f.write( f'{table[ len( table ) - 1 ]} ( Value: {faceCards[ table[ len( table ) - 1 ] ]} cards )\n' )

            # player sets down certain amount of cards, if they have a face card, they continue, else the previous person gets all the cards
            f.write( 'They place:\n' )

            playerPutsDown = faceCards[ table[ len( table ) - 1 ] ]

            # player sets down said amount of cards
            for i in range( playerPutsDown ):

                moves += 1

                if len( currentPlayer ) != 0:

                    f.write( f'{currentPlayer[0]}\n' )

                    table.append( currentPlayer[0] )
                    currentPlayer.pop( 0 )

                    if table[ len( table ) - 1 ] in faceCards:
                        break

            # if the player sets a face card down, they get to continue
            if table[ len( table ) - 1 ] in faceCards:

                f.write( f'Player {count} passes!\n' )

            # if they don't have a face card then the previous player gets all the cards
            else:

                f.write( f'Player {count} had no face cards.\n' )
                
                if count == 0:

                    for i in table:
                        players[ numberOfPlayers - 1 ].append( i )

                else:

                    for i in table:
                        players[ count - 1 ].append( i )

                moves += 1
                table = []
                faceCard = False

            f.write( '\n' )

        # if there are 0 or 1 card in the stack, place one down and check for face cards
        elif len( table ) <= 1:

            moves += 1
            f.write( f'Player {count} places a {currentPlayersCard}\n' )

            # player puts down a card
            table.append( currentPlayersCard )
            currentPlayer.pop( 0 )

            # check for face cards
            if len( table ) != 0:
                if table[ len( table ) - 1 ] in faceCards:
                    faceCard = True
                    pass

        else:

            # check for face cards
            if table[ len( table ) - 1 ] in faceCards:
                faceCard = True

            else:

                f.write( f'Player {count} places a {currentPlayersCard}\n' )

                # placing a card
                table.append( currentPlayersCard )
                currentPlayer.pop( 0 )
                moves += 1

                # check for Doubles
                if len( table ) >= 2:
                    if table[ len( table ) - 1 ] == table[ len( table ) - 2 ]:

                        f.write( '\nDOUBLES:\n' )
                        
                        # the person who has the fastest reflexes ( random ) gets all the cards
                        playerWhoSlapped = random.randint( 0 , numberOfPlayers - 1 )

                        f.write( f'Player: { playerWhoSlapped } SLAPPED FIRST, they get: { table }\n' )

                        for i in table:
                            players[ playerWhoSlapped ].append( i )

                        table = []
                        moves += 1

                # check for Sandwiches
                elif len( table ) >= 3:
                    if table[ len( table ) - 1 ] == table[ len( table ) - 3 ]:

                        f.write( '\nSANDWICHES\n' )
                    
                        # the person who has the fastest reflexes ( random ) gets all the cards
                        playerWhoSlapped = random.randint( 0 , numberOfPlayers - 1 )
                        
                        f.write( f'Player: { playerWhoSlapped } SLAPPED FIRST, they get: { table }\n' )

                        for i in table:
                            players[ playerWhoSlapped ].append( i )

                        table = []
                        moves += 1

    # rotate to next player or begin again
    if count == numberOfPlayers - 1:
        count = 0

    else:   
        count = count + 1

f.close()