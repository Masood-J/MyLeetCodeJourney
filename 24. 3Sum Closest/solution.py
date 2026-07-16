class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:



        current_sum=int()
        nums.sort()
        closest_num=None
        for current in range(len(nums)):
            i=current+1
            j=len(nums)-1
            
            while i<j:

                current_sum=nums[current]+nums[i]+nums[j]
                if closest_num is None:
                  closest_num=current_sum
                if(abs(target-current_sum)<abs(target-closest_num) or abs(target-current_sum)==abs(target-closest_num)):
                  closest_num=current_sum
                if(current_sum<target):
                    i+=1
                elif(current_sum>target):
                    j-=1
                elif(current_sum==target):
                    return target

            


        return closest_num

            

            

            




            


        