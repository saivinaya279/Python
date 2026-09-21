# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         node1=Node(10)
#         node2=Node(20)
#         node3=Node(30)
#         node4=Node(40)
#         node1.next=node2
#         node2.next=node3
#         node3.next=node4
#         current=node1
#         while current is not None:
#             print(current.data,end="->")
#             current=current.next
#         print("None")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

if __name__=="__main__":

    obj1=Node(10)
    print(obj1.data)
    obj1=Node(20)
    print(obj1.data)