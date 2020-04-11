class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self,value):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(value)

    def delete(self,value):
        