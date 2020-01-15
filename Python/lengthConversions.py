import os
os.system( 'clear' )

def conversions( ):

    done = 0;

    while ( done != 1 ):

        x = input("Please select A: Feet to meters. || B: Meters to feet ").lower()

        if ( x == 'a' ):

            y = float(input("Please enter feet: " ))

            meters = int(y) / 3.2808

            print( f'{int(y)} Feet = { meters } Meters' )

            stop = input("would you like to complete another conversion? ( Y / N ) " ).lower()

            print( stop )

            if ( stop == 'n' ):
                break
            else:
                continue

        elif ( x == 'b' ):

            y = float(input("please enter meters: "))

            print( int(y) )

            feet = int(y) * 3.28084

            print( f'{int(y)} Meters = { feet } Feet' )

            stop = input("would you like to complete another conversion? ( Y / N ) " ).lower()

            if ( stop == 'n' ):
                break
            else:
                continue

        else:
            print( 'Please enter a valid input.' )


conversions()