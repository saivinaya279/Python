class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None    
    def insert_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        if self.head is None:
            print("the list is empty")
            return
        temp=self.head
        print("linkedlist:",end=" ")
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("null")
    def delete_by_value(self,value):
        if self.head is None:
            return
        if self.head.data==value:
            self.head=self.head.next
            return
        prev=self.head
        curr=self.head.next
        while curr is not None:
            if curr.data ==value:
                prev.next=curr.next
                return
            prev=curr
            curr=curr.next
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begin(10)
    ll.insert_at_begin(20)
    ll.insert_at_begin(30)
    ll.delete_by_value(20)
    ll.display()
         