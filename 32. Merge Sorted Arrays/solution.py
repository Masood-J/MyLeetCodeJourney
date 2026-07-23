class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i=0
        j=0

        sorted_final=list()

        while i<m and j<n:
            if(nums1[i]<nums2[j]):
                sorted_final.append(nums1[i])
                i+=1
            else:
                sorted_final.append(nums2[j])
                j+=1


        sorted_final.extend(nums1[i:m])
        sorted_final.extend(nums2[j:n])

        nums1[:]=sorted_final
 
        """
        Do not return anything, modify nums1 in-place instead.
        """
        