class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        quadretList=list()
        currentSum=None

        nums.sort()
        for current in range(len(nums)):

            if(current>0 and nums[current]==nums[current-1]):
              continue  




            for fixed in range(current+1,len(nums)):

                if fixed > current + 1 and nums[fixed] == nums[fixed - 1]:
                    continue

                i=fixed+1
                j=len(nums)-1
                
                while i<j:

                    currentSum=nums[fixed]+nums[current]+nums[i]+nums[j]
                    if(currentSum==target):
                        quadretList.append([nums[fixed],nums[current],nums[i],nums[j]])
                        i+=1
                        j-=1

                        while i<j and nums[i]==nums[i-1]:
                          i+=1
                        while i<j and nums[j]==nums[j+1]:
                          j-=1

                    elif(currentSum<target):
                        i+=1
                    else:
                        j-=1


        return quadretList



        