"""
https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python

You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""

def tree_by_levels(node):
    
    return_value = []
    
    def find_stuff_recursively( next=None ):
        
        check_nodes_next = []
        
        if next == []:
            return
        
        for node in next:
        
            return_value.append( node.value )

            if isinstance( next, list ) and len( next ) == 0:
                return
            
            next = [] if next == None else next

            if node.left and node.left.value:
                check_nodes_next.append( node.left )
            if node.right and node.right.value:
                check_nodes_next.append( node.right )

        return find_stuff_recursively( check_nodes_next )
            
        
    if not node:
        return return_value
    
    find_stuff_recursively( [node] )

    return return_value