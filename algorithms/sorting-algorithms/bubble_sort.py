
# What is the bubble sort algorithm? How does it work?

# 1. Start at the beginning of the list.
# 2. Compare the first two elements. If the first is greater than the second, swap them.
# 3. Move to the next pair of elements and repeat the comparison and swap if necessary.
# 4. Continue this process, moving through the list until the end is reached.
# 5. After the first pass, the largest element is guaranteed to be at the end.
# 6. Repeat the process for the remaining elements (excluding the last one, which is already sorted).
# 7. Continue these passes until no more swaps are needed.

use_recursion = True
# use_recursion = False

def bubble_sort( given_item ):
    """
    Algorithm to bubble sort an unsorted input
    input can be any of these types: List, String, and Tuple

    Why is Dictionary not in bubble sort? 
    Bubble sort has a time complexity of O(n^2), making it less suitable for large datasets 
    compared to more efficient sorting algorithms like Timsort (used in Python's built-in sorted() function) 
    with a time complexity of O(n log n).

    completed both iteratively and recursively. Iterative is the classic way to do it for O(n^2) as the call stack 
    using recursion may fail when given larger objects. 
    """

    return_value = None
    # print( f"Sorting - {type(given_item)} - {given_item}" )

    # ==========================--------------------------------

    if isinstance( given_item , list ):

        # === RECURSIVE ===

        if use_recursion:

            def bubble_sort_recursive( given_item ):

                item_mutated = False
                for i in range( len( given_item ) - 1 ):

                    el_1 = given_item[i]
                    el_2 = given_item[i + 1]

                    if el_1 > el_2:
                        given_item[i] = el_2
                        given_item[i + 1] = el_1
                        item_mutated = True

                if item_mutated:
                    return bubble_sort_recursive( given_item )
                else: 
                    return given_item

            # Initiate recursion
            return_value = bubble_sort_recursive( given_item )

        elif not use_recursion:

            # === ITERATIVE ===
            
            for _ in range( len( given_item ) ):
                for i in range( len( given_item ) ):

                    item_mutated = False
                    for i in range( len( given_item ) - 1 ):

                        el_1 = given_item[i]
                        el_2 = given_item[i + 1]

                        if el_1 > el_2:
                            given_item[i] = el_2
                            given_item[i + 1] = el_1
                            item_mutated = True

                    if not item_mutated:
                        return given_item


    # ==========================--------------------------------

    elif isinstance( given_item, str ):

        # === RECURSIVE ===

        def bubble_sort_recursive( given_item ):

            item_mutated = False
            for i in range( len( given_item ) - 1 ):

                el_1 = given_item[i]
                el_2 = given_item[i + 1]

                # print( f"Comparing: {el_1} to {el_2}" )
                if el_1 > el_2:
                    print( f"Before: {given_item}" )
                    start_index = i
                    end_index = i + 2
                    if start_index < 0:
                        start_index = i - 1
                    if end_index > len(given_item):
                        end_index = -1
                    given_item = given_item[:start_index] + el_2 + el_1 + given_item[ end_index: ]
                    # print( f"After: {given_item}" )
                    item_mutated = True

            if item_mutated:
                return bubble_sort_recursive( given_item )
            else: 
                return given_item

        # Initiate recursion
        return_value = bubble_sort_recursive( given_item )

        # === ITERATIVE ===
        # for _ in range( len( given_item ) ):
        #     for i in range( len( given_item ) ):


    # ==========================--------------------------------

    elif isinstance( given_item , tuple ):

        # === RECURSIVE ===
                
        def bubble_sort_recursive( given_item ):

            item_mutated = False
            for i in range( len( given_item ) - 1 ):

                el_1 = given_item[i]
                el_2 = given_item[i + 1]

                if el_1 > el_2:

                    start_index = i
                    end_index = i + 2
                    if start_index < 0:
                        start_index = i - 1
                    if end_index > len(given_item):
                        end_index = -1
                    given_item = given_item[:start_index] + ( el_2 , el_1 ) + given_item[ end_index: ]
                    item_mutated = True

            if item_mutated:
                return bubble_sort_recursive( given_item )
            else: 
                return given_item

        # Initiate recursion
        return_value = bubble_sort_recursive( given_item )

    else:
        raise Exception( f"given type not supported: {type(given_item)}" )


    return return_value

# Ending question ( when completed ): What is the big O notation complexity for this?
# My bubble sort time complexity is O(n^2)