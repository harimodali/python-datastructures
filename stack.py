class Stack(object):
    
    def __init__(self):
        # Creates an empty list of items
        
        self.items = []

    def isEmpty(self):
        # Return True if items list is empty
        # Return False if items list is not empty

        return self.items == []

    def peek(self):
        # Return the last item that was pushed into stack
        # Since we push items at the first position,
        # Return the first item

        return self.items[0]

    def push(self,item):
        # Push an element at the first position in items list

        self.items.insert(0,item)

    def pop(self):
        # Take out the last item that was pushed into stack
        # Also return that item

        return self.items.pop(0)

    def contains(self,item):
        # Return True if item is present in the stack
        # Return False otherwise
        
        return (item in self.items)

    def length(self):
        #Return the length of the items list
        
        return len(self.items)
