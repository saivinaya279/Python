class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        print("ll:",end="")
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("null")
    def insert_at_position(self,data,Position):
        if Position==0:
            self.insert_at_begin(data)
            return
        new_node=Node(data)
        temp=self.head
        for _ in range(Position-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begin(10)
    ll.insert_at_begin(20)
    ll.insert_at_begin(30)
    ll.insert_at_position(25,2)
    ll.display()
        

