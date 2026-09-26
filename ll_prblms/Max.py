# Problem 4: Find the Maximum Value
# Let's understand the logic first. No code yet. 😊
# 📌 Given Linked List
# 10 → 40 → 20 → 50 → 30 → None
# 🎯 Expected Output
# Maximum value: 50
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
    def Max_value(self):
        if self.head is None:
            print("empty list")
            return
        temp=self.head
        max_v=temp.data
        while temp is not None:
            if temp.data > max_v:
                max_v=temp.data
            temp=temp.next
        print(max_v)
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_begin(30)
    ll.insert_at_begin(20)
    ll.insert_at_begin(10)
    ll.Max_value()
    ll.display()