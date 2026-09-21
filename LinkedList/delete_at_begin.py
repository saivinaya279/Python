class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Insert_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        if self.head is None:
            print("print the list is empty")
            return
        temp=self.head
        print("linked list",end="")
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("null")
    def delete_at_begin(self):
        if self.head is None:
            raise IndexError("list empty")
        self.head=self.head.next
if __name__=="__main__":
    ll=LinkedList()
    ll.Insert_at_begin(10)
    ll.Insert_at_begin(20)
    ll.Insert_at_begin(30)
    ll.delete_at_begin()
    ll.display()


