class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        num_set=set(nums)
        listLength=len(nums)
        missingNumbers=list()
        for num in range(1, listLength + 1):
            if num not in num_set:
                missingNumbers.append(num)
        
        return missingNumbers
        

        
            
        