class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max=nums[0]
        global_max=nums[0]
        for index,number in enumerate(nums):
         if(index==0):
            continue
         current_max=max(number,current_max+number)
         global_max=max(global_max,current_max)
        return global_max
          
        