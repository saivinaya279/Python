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
    def del_at_begin(self):
        if self.head is None:
            print("empty")
            return
        self.head=self.head.next
    def del_at_end(self):
        if self.head is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def del_by_value(self,val):
        if self.head.data==val:
            return self.del_at_begin
        prev=self.head
        curr=self.head.next
        while curr is not None:
            if curr.data==val:
                prev.next=curr.next
                return
            prev=curr
            curr=curr.next
    def display(self):
        if self.head is None:
            print("empty List")
            return
        temp=self.head
        print("Linkedlist:",end="")
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begin(30)
    ll.insert_at_begin(20)
    ll.insert_at_begin(10)
    # ll.insert_at_position(25,2)
    # ll.del_at_begin()
    ll.del_by_value(20)
    # ll.del_at_end()
    ll.display()
        