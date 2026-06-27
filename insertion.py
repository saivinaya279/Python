arr = [5, 2, 4, 1, 3]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
arr = [5, 2, 4, 1, 3]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
arr = [5, 1, 4, 2, 8]

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
arr = [5, 1, 4, 2, 8]

count = 0
n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            count += 1

print("Swaps:", count)
arr = [1, 2, 3, 4, 5]

swapped = False
n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

if swapped:
    print("Not Sorted")
else:
    print("Already Sorted")
arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):
    min_idx = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):
    min_idx = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    print("Minimum:", arr[min_idx])

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = ["mango", "apple", "banana"]

n = len(arr)

for i in range(n):
    min_idx = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
arr = [12, 11, 13, 5, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
arr = ["cat", "apple", "dog", "ball"]

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
arr = ["cat", "apple", "dog", "ball"]

n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
arr = [1, 2, 3, 4, 5]

swapped = False
n = len(arr)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

if swapped:
    print("Not Sorted")
else:
    print("Already Sorted")
