class Node(object):

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self,data):
        if not self.data:
            self.data = data
        else:
            if self.data > data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    
    def search(self, data):
        if self.data == data:
            print "Found data %s" %str(self.data)
        else:
            if data < self.data:
                if self.left == None:
                    return "Data (%s) is not found" %data
                else:
                    self.left.search(data)
            elif data > self.data:
                if self.right == None:
                    return "Data (%s) is not found" %data
                else:   
                    self.right.search(data)
   
    def print_binary_tree(self):
        if self.left:
            self.left.print_binary_tree()
        print( self.data),
        if self.right:
            self.right.print_binary_tree() 
