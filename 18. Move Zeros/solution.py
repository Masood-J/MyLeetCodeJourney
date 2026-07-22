class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        rightpointer=0

        for i,num in enumerate(nums):
            if num!=0:
                nums[rightpointer]=num
                rightpointer+=1
            
        
        for j in range(rightpointer,len(nums),1):
            nums[j]=0


        