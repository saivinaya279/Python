arr = list(map(int,input().split()))

target = int(input())

left = 0

right = len(arr)-1


while left<right:

    sum1 = arr[left]+arr[right]

    if sum1==target:
        print(left, right)
        break
    elif sum1<target:
        left+=1

    else:
        right-=1
