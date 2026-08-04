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
stack = [10, 20, 30]

if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")
stack = []

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
stack = []

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
stack = [10, 20, 30, 40]

print("Stack elements:")

for element in reversed(stack):
    print(element)
stack = [10, 20, 30, 40]

print("Stack elements:")

for element in reversed(stack):
    print(element)