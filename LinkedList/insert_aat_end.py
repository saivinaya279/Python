class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node= Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def display(self):
        if self.head is None:
            print("list is empty")
            return 
        temp=self.head
        print("Linked list:",end="")
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("null")
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        


if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    ll.display()