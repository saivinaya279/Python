arr = [10, 20, 30, 40, 50]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print(i)
        break
else:
    print(-1)
arr = [10,20,30,40,50,60]

key = 40

low = 0
high = len(arr)-1

while low <= high:

    mid = (low+high)//2

    if arr[mid] == key:
        print(mid)
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1