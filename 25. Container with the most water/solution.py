class Solution:
    def maxArea(self, height: List[int]) -> int:


        current_maxArea=None
        calculated_area=int()
        curr_width=int()

        i=0
        j=len(height)-1



        while i<j:
            curr_width=j-i

            if current_maxArea is None:
                calculated_area=min(height[i],height[j])*curr_width
                current_maxArea=calculated_area
                
                if(height[i]<height[j]):
                  i+=1
                else:
                  j-=1
                continue

            calculated_area=min(height[i],height[j])*curr_width

            if(calculated_area>current_maxArea):
                current_maxArea=calculated_area
            
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1

            
        return current_maxArea



            


        