# unique_in_order takes arguments ia sequence and returns a list of items without any elements with the same value next to each other 
# and preserving the original order of elements.

def unique_in_order(iterable):

    bank = []

    for i in range( len( iterable ) ):

        if len( bank ) == 0:
            bank.append( iterable[i] )

        else:

            if iterable[i] == bank[ len(bank) - 1 ]:
                pass

            else:
                bank.append( iterable[i] )

    return bank

# unique_in_order('AAAABBBCCDAABBB') # ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD') # ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3]) # [1,2,3]