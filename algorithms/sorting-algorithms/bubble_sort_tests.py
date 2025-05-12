
import sys
import random
import unittest
from bubble_sort import bubble_sort

class BubbleSortTests( unittest.TestCase ):
    """
    All tests for Bubble Sort
    """

    def test_list_1( self ):
        unsorted_list = [ 2, 1 ]
        expected_output = [ 1, 2 ]

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

    def test_list_2( self ):
        unsorted_list = [ 2, 1, 7, 4, 5, 3, 6 ]
        expected_output = [ 1, 2, 3, 4, 5, 6, 7 ]

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )


    def test_list_3( self ):
        expected_output = list(range(1, 101))
        unsorted_list = list(range(1, 101))
        random.shuffle( unsorted_list )

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

    def test_list_4( self ):
        """
        Recursion is less effective with larger objects due to the call stack
        lets use a custom recursion limit and see what it does
        """
        use_recursion = True

        # Set a lower recursion depth limit
        sys.setrecursionlimit(500)

        unsorted_list = list(range(1, 10000))
        random.shuffle(unsorted_list)

        # Use assertRaises to check the exception type
        with self.assertRaises( RecursionError ) as context:
            bubble_sort(unsorted_list, use_recursion)
        self.assertEqual("maximum recursion depth exceeded in comparison", str(context.exception))
        # STACK OVERFLOW!!!! RecursionError: maximum recursion depth exceeded in comparison
        
    # def test_list_5( self ):
    #     """
    #     Recursion is less effective with larger objects, lets break it!
    #     """
    #     expected_output = list(range(1, 99999999999))
    #     unsorted_list = list(range(1, 99999999999))
    #     random.shuffle( unsorted_list )
    #     bubble_sort_output = bubble_sort( unsorted_list )
    #     self.assertEqual( bubble_sort_output, expected_output )

    def test_string_1( self ):
        unsorted_str = "bacefdg"
        expected_output = "abcdefg"

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_str, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_str, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

    def test_string_2( self ):
        unsorted_str = "aaaAAAbbbBBBcccCCC123"
        expected_output = "123AAABBBCCCaaabbbccc"

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_str, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_str, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

    def test_string_3( self ):
        unsorted_str = "avkajhlskdjvhiowuhwihuajnvccmnzxvhiuvhilzudvlIDJShvalksjdvnaiuhvlauerybvusehbvjhdvhbvsjehvblibejca"
        expected_output = "DIJSaaaaaaabbbbbcccddddeeeehhhhhhhhhhhhiiiiiijjjjjjjkkkllllllmnnnorssssuuuuuuuvvvvvvvvvvvvvvwwxyzz"

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_str, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_str, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

    def test_tuple_1( self ):
        unsorted_list = ( 2, 1 )
        expected_output = ( 1, 2 )

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

    def test_tuple_2( self ):
        unsorted_list = ( 3, 7, 5, 2, 6, 1, 4 )
        expected_output = ( 1, 2, 3, 4, 5, 6, 7 )

        # ITERATIVE
        use_recursion = False
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

        # RECURSIVE
        use_recursion = True
        bubble_sort_output = bubble_sort( unsorted_list, use_recursion )
        self.assertEqual( bubble_sort_output, expected_output )

if __name__ == '__main__':
    unittest.main()