class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node = new_next

class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.get_next()
        return count
    
    def search(self,data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        raise ValueError("No node with Data: %s" %data)

    def delete(self,data):
        current = self.head
        previous = None
        found = 0
        while current and not found:
            if current.data == data:
                found = 1
            else:
                previous = current
                current = current.get_next()
        if not found:
            raise ValueError("No node with Data: %s" %data)
        else:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def insert_in_end(self,data):
        current = self.head
        if not current.get_data():
            current = Node(data)
        else:
            while current:
                if current.get_next() == None:
                    break
                else:
                    current = current.get_next()
            new_node = Node(data)
            current.set_next(new_node)

    def __str__(self):
        rs = "Head -->"
        current = self.head
        while current:
            rs += str(current.get_data()) + "-->"
            current = current.get_next()
        rs += "None"
        return rs
            

                    
            
