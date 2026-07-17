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


def is_pal(s):
    left = 0

    right = len(s)-1

    while left<right:
        if s[left]!=s[right]:
            return False
        else:
            left+=1
            right-=1

    return True



s = input()
if is_pal(s):
    print("palindrome")

else:
    print("not a palindrome")
hts=int(input())
n = len(hts)

left = 0
right = n-1
max_area = 0

while left<right:

    area = min(hts[left], hts[right])*(right-left)

    max_area = max(area, max_area)

    if hts[left]<hts[right]:
        left+=1
    else:
        right-=1

print(max_area)
