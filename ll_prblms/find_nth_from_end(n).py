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
    def find_nth_from_end(self,n):
        slow=self.head
        fast=self.head
        for _ in range(n):
            fast=fast.next
        while fast is not None:
            slow=slow.next
            fast=fast.next
        return slow
    # def find_middle(self):
    #     slow=self.head
    #     fast=self.head
    #     while fast is not None and fast.next is not None:
    #         slow=slow.next
    #         fast=fast.next.next
    #     return slow
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
    # def insert_at_end(self,data):
    #     new_node=Node(data)
    #     if self.head is None:
    #         self.head=new_node
    #         return
    #     temp=self.head
    #     while temp.next is not None:
    #         temp=temp.next
    #     temp.next=new_node
        


if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(40)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(10)
    nth_end=ll.find_nth_from_end(2)
    print(nth_end.data)
    # middle = ll.find_middle()
    # print(middle.data)
    # ll.insert_at_end(30)
    ll.display()
# better version to handle the edge cases
"""def find_nth_from_end(self, n):
    if self.head is None:
        print("list is empty")
        return None

    if n <= 0:
        print("invalid n")
        return None

    slow = self.head
    fast = self.head

    # Move fast n steps
    for _ in range(n):
        if fast is None:
            print("n is greater than list length")
            return None
        fast = fast.next

    # Move both pointers
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow"""