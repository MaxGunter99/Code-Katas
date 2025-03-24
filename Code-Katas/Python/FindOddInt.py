# RUN WITH: python code-katas/python/FindOddInt.py

# re

def find_it(seq):
    
    return_value = None

    for item in seq:
        item_count = len( [ i for i in seq if i == item ] )
        if item_count % 2 == True:
            return_value = item
            break

    print( f"Returning: {return_value}" )
    return return_value


find_it( 
    [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
)