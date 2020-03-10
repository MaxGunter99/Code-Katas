# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# For 4 or more names, the number in and 2 others simply increases.
import os
os.system('clear')
print('\n')

def likes(names):

    if ( len( names ) == 0 ):

        phrase = 'no one'
        end = 'likes this'

    elif ( len( names ) == 1 ):
            
        phrase = names[0]
        end = 'likes this'

    elif ( len( names ) == 2 ):
            
        phrase = f"{names[0]} and {names[1]}"
        end = 'like this'

    elif ( len( names ) == 3 ):
            
        phrase = f"{names[0]}, {names[1]} and {names[2]}"
        end = 'like this'

    elif ( len( names ) >= 4 ): 
            
        phrase = f"{names[0]}, {names[1]} and {len(names) - 2} others"
        end = 'like this'

    answer = phrase + " " + end
    print( answer )
    return answer



# likes([]) 
# 'no one likes this'

# likes(['Peter']) 
# 'Peter likes this'

# likes(['Jacob', 'Alex']) 
# 'Jacob and Alex like this'

likes(['Max', 'John', 'Mark']) 
# 'Max, John and Mark like this'

# likes(['Alex', 'Jacob', 'Mark', 'Max']) 
# 'Alex, Jacob and 2 others like this'