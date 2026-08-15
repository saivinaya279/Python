# nums=[4,-1,2,-7,3,4]
# global_sum=nums[0]
# currsum=0
# for i in nums:
#     currsum+=i
#     if currsum<0:
#         currsum=0
#     else:
#         global_sum=max(global_sum,currsum)
# print(global_sum)
def solve(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    start=0
    best_start=0
    best_end=0
    for i in range(1,len(arr)):
        if curr_sum<arr[i]:
            curr_sum=arr[i]
            start=i
        else:
            curr_sum+=arr[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
            best_start=start
            best_end=i
    return max_sum,best_start,best_end, arr[best_start:best_end+1]
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solve(arr))