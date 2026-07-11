class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxRecord=dict()
        
        if(len(nums)==2):
            if(nums[0]>nums[1]):
               return nums[0]
            else:
               return nums[1]
        elif(len(nums)==1):
               return nums[0];

            
            # [2,2,3,1]
        for numbers in nums:
            temp=int()
            if "first" not in maxRecord:
                maxRecord["first"]=numbers
                continue
            else:
                if(numbers>maxRecord["first"]):
                    temp=maxRecord["first"]
                    maxRecord["first"]=numbers;
                    if "second" not in maxRecord:
                        maxRecord["second"]=temp;
                    elif "second" in maxRecord:
                        maxRecord["third"]=maxRecord["second"];
                        maxRecord["second"]=temp
                if(numbers==maxRecord["first"]):
                    continue

                        
            if "second" not in maxRecord:
                if(numbers<maxRecord["first"]):
                    maxRecord["second"]=numbers
                else:
                    continue
            else:      
                if(numbers>maxRecord["second"]):
                    temp=maxRecord["second"]
                    maxRecord["second"]=numbers
                    maxRecord["third"]=temp

                if(numbers==maxRecord["second"]):
                    continue
                        
                        
            if "third"  not in maxRecord:
                if(numbers<maxRecord["second"]):
                    maxRecord["third"]=numbers
                else:
                    continue
            else:
                if(numbers>maxRecord["third"] and numbers!=maxRecord["second"]):
                    maxRecord["third"]=numbers
        
        if("third" in maxRecord):
            return maxRecord["third"]
        else:
            return maxRecord["first"]
            
        
        