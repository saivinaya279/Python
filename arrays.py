# FIND THE MAXIMUM ELEMENT IN AN ARRAY
arr=list(map(int,input().split()))
max_value=arr[0]
for i in arr:
    if i>max_value:
        max_value=i
print(max_value)
"""# One Small Issue (Edge Case)

If the user enters nothing, your code crashes.

Example:

Input: (empty)

Error:

IndexError: list index out of range"""
arr = list(map(int, input().split()))

if len(arr) == 0:
    print("Array is empty")
else:
    max_value = arr[0]

    for num in arr:
        if num > max_value:
            max_value = num

    print(max_value)
"""check if Array is Sorted

Example:

Input

1 2 3 4 5

Output

True

Input

1 3 2 5

Output

False

Hint:

Compare arr[i] with arr[i+1]"""
# method-1
arr=list(map(int,input().split()))
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print(is_sorted)
# method-2
arr=list(map(int,input().split()))
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        print(False)
        break
else:
    print(True)
"""Now write code for the last problem:

Reverse an Array

Example

Input:
1 2 3 4 5

Output

5 4 3 2 1

Constraint:

Do NOT use arr[::-1]

Use two pointers."""
        