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
arr=[5,2,4,6,1,3]

for i in range(1,len(arr)):

    key=arr[i]

    j=i-1

    while j>=0 and arr[j]>key:

        arr[j+1]=arr[j]

        j-=1

    arr[j+1]=key

print(arr)
def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i<len(left) and j<len(right):

            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1

            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
def partition(arr,low,high):

    pivot=arr[high]

    i=low-1

    for j in range(low,high):

        if arr[j]<pivot:

            i+=1

            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1