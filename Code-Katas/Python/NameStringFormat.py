# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas 
# except for the last two names, which should be separated by an ampersand.

def namelist(names):

    namesList = []
    answer = ''
    
    for i in names:
        name = i.values()[0]
        namesList.append( name )

    if len( namesList ) >= 2:
        namesList.insert( len( namesList ) - 1 , '&' )

        beginning = namesList[ : len( namesList ) - 3 ]
        end = namesList[ len( namesList ) - 3: ]
        full = beginning + end

        for i in full:
            print( i )
        
    else:

        print( namesList )

namelist([]) # ''
namelist([{'name': 'Bart'}]) # 'Bart'
# namelist([{'name': 'Bart'},{'name': 'Lisa'}]) # 'Bart & Lisa'
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]) # 'Bart, Lisa & Maggie'
# namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]) # 'Bart, Lisa, Maggie, Homer & Marge'