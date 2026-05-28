n=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
target=2
index=0
for row in n:
    count=0
    for num in row:
        if num==1:
            count+=1
    if count!=target:
        print(index,count)
    index+=1
# right shifting"""
arr=list(map(int,input().split()))
arr_new=[]
for i in range(len(arr)-1,2,-1):
    arr[i]=arr[i-1]
arr[2]=99
print(arr)