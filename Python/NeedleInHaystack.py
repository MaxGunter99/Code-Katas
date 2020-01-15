# Write a function findNeedle() that takes an array full of junk but containing one "needle"
import os

os.system( 'clear' )

haystack_1 = [ '3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False ]
haystack_2 = ['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'];
haystack_3 = [1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54];

def findNeedle ( stack ):

    for i in range( len( stack ) ):
        
        if stack[i] is 'needle':
            print( f'found the needle at position {i}' )
            return f'found the needle at position {i}'

findNeedle(haystack_1), 'found the needle at position 3'
findNeedle(haystack_2), 'found the needle at position 5' 
findNeedle(haystack_3), 'found the needle at position 30'