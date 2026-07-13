
def count_sort(arr, place):

    n = len(arr)
    output = [0]*n

    count = [0]*10 

    for i in range(0,n):
        index = arr[i]//place
        count[index%10]+=1

    for i in range(1,10):
        count[i]+=count[i-1]


    i = n-1

    while i>=0:

        ind = arr[i]//place
        output[count[ind%10]-1] = arr[i]
        count[ind%10]-=1
        i-=1

    for i in range(0,n):
        arr[i]= output[i]
        
    
        
