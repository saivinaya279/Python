def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[4,2,8,1] # 2 4 1 8 # 2 1 4 8 #
print(bubble_sort(arr))# 4,2,8,1  i=0 ,n-1 n=4-0-1 =2
