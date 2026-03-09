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
arr=list(map(int,input().split()))
left=0
right =len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left += 1
    right -= 1
print(arr)
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

<<<<<<< HEAD
# Move elements one position to the left
arr = [1,2,3,4,5]
first = arr[0]
for i in range(len(arr)-1):
    arr[i] = arr[i+1]
arr[-1] = first
print(arr)

# Move elements one position to the right
arr = [1,2,3,4,5]
last = arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]
arr[0] = last
print(arr)
=======

# Second Largest Element in Array
def second_largest(arr):
    first = second = -1
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
arr = [10,5,20,8]
print(second_largest(arr))
>>>>>>> eee4155 (message)
