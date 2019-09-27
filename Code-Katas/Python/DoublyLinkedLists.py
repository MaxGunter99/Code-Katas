### Doubly Linked Lists
#  * The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
#  * The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
#    * `add_to_head` replaces the head of the list with a new value that is passed in.
#    * `add_to_tail` replaces the tail of the list with a new value that is passed in.
#    * `remove_from_head` removes the head node and returns the value stored in it.
#    * `remove_from_tail` removes the tail node and returns the value stored in it.
#    * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
#    * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
#    * `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
#    * `get_max` returns the maximum value in the list. 
#  * The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
 
import os
os.system( 'clear' )

class ListNode:
    def __init__ ( self , value , previous = None, next = None ):
        self.value = value
        self.previous = previous
        self.next = next

    def insert_before( self , value ):
        next_node_before = self.previous
        print( next_node_before )

    def insert_after( self , value ):
        next_node_after = self.next
        print( next_node_after )

