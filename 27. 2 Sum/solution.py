class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        seen_dict=dict()

        for i in range(len(nums)):
            need=target-nums[i]

            if need in seen_dict:
                return [i,seen_dict[need]]
            else:
                seen_dict[nums[i]] = i

        