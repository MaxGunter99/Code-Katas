# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas 
# except for the last two names, which should be separated by an ampersand.

def namelist(names):

    namesList = []
    
    for i in names:
        name = i['name']
        namesList.append( name )

    if len( namesList ) >= 3:

        namesList.insert( len( namesList ) - 1 , '&' )

        beginning = namesList[ : len( namesList ) - 3 ]
        end = namesList[ len( namesList ) - 3: ]
        beginning = ', '.join( beginning )
        end = ' '.join( end )
        full = beginning + ', ' + end

        print( full )
        return full
        
    elif len( namesList ) == 2:

        namesList.insert( len( namesList ) - 1 , '&' )
        print( ' '.join( namesList ) )

    elif len( namesList ) == 1:

        print( namesList[0] )
        return namesList[0]
        
    else:
    
        return ''


# namelist([]) # ''
# namelist([{'name': 'Bart'}]) # 'Bart'
namelist([{'name': 'Bart'},{'name': 'Lisa'}]) # 'Bart & Lisa'
# namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]) # 'Bart, Lisa & Maggie'
# namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) # 'Bart, Lisa, Maggie, Homer & Marge'