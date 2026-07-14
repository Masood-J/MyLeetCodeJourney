
# Brute Force Approach
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        arrLength=len(nums)

        result=list()
        for i in range(arrLength):
            sum_check=int()
            req_list=list()
            for j in range(i+1,arrLength):

                for k in range(j+1,arrLength):
                    sum_check=nums[i]+nums[j]+nums[k]
                    if(sum_check==0):
                        req_list=sorted([nums[i],nums[j],nums[k]])
                        if(req_list not in result):
                            result.append(req_list)

        
        return result
    
# Optimal Approach
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tripletsList=list()
    
        nums.sort()


        for fixed in range(len(nums)):

          if(fixed>0 and nums[fixed]==nums[fixed-1]):
            continue  

          target=-nums[fixed]
          i=fixed+1
          j=len(nums)-1

          while(i<j):


            if(nums[i]+nums[j]==target):
                tripletsList.append([nums[fixed],nums[i],nums[j]])
                i+=1
                j-=1

                while i<j and nums[i]==nums[i-1]:
                    i+=1
                while i<j and nums[j]==nums[j+1]:
                    j-=1
                continue

            if(nums[i]+nums[j]<target):
                i+=1
            elif(nums[i]+nums[j]>target):
                j-=1



        return tripletsList




        
                







        