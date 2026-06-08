class Solution:
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums

nums=list(map(int,input().split()))
class Solution:
    def largestNumber(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        ans = ''.join(map(str, nums))
        if ans[0]=="0":
            return "0"
        return ans
nums=list(map(int,input().split()))
class Solution:
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
nums=list(map(int,input().split()))
        