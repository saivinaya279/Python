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
arr = [5,4,3,2,1]

n = len(arr)

for i in range(n-1):

    swapped = False

    for j in range(n-1-i):

        if arr[j] > arr[j+1]:

            arr[j],arr[j+1]=arr[j+1],arr[j]

            swapped=True

    if not swapped:
        break

print(arr)
arr=[64,25,12,22,11]

n=len(arr)

for i in range(n):

    minimum=i

    for j in range(i+1,n):

        if arr[j]<arr[minimum]:

            minimum=j

    arr[i],arr[minimum]=arr[minimum],arr[i]

print(arr)