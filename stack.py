class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
obj_st = Stack()
obj_st.push(1)
obj_st.push(2)
obj_st.push(3)
print("stack:", obj_st.stack)
print("pop:", obj_st.pop())
print("after pop-stack:", obj_st.stack)