'''
Linked List class that implements the data structure
'''

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head 
        counter = 1
        
        if position < 1:
            pass
        while current and counter   <= position:
            if counter == position -1: 
                temp = current.next 
                current.next = new_element
                new_element.next = temp
            current = current.next
            counter += 1
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current 
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next 
            else:
                self.head = current.next
        
        