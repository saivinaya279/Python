# Problem 1: Display All Nodes
# Given Linked List
# 10 → 20 → 30 → 40 → None
# Expected Output
# 10 → 20 → 30 → 40 → None
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
            print("empty list")
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
    ll.display()