class Queue(object):

    def __init__(self):
        #Start an emptylist of items

        self.items = []

    def isEmpty(self):
        #return True if no item exists in items list

        return self.items = []

    def Enqueue(self, item):
        # items get added in the back (item 0) in the list

        self.items.insert(0,item)

    def Dequeue(self):
        # Take the first added item (FIFO)
        # That would be the last item in the list
        # Also return that item

        return self.items.pop()

    def size(self):
        
        return len(self.items)

    def peek(self):
        #return the next element in the queue
        #This would be the last item in the items list

        return self.items[-1]


