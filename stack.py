stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)
stack = []

def push(value):
    stack.append(value)

push(10)
push(20)
push(30)

print(stack)
stack = [10, 20, 30]

if stack:
    print("Removed:", stack.pop())

print("Stack:", stack)