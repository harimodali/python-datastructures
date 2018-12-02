class Stack(object):
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def contains(self,item):
        return (item in self.items)

    def length(self):
        return len(self.items)
