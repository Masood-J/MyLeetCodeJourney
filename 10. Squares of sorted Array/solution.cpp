// (n)^2

#include <vector>
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
     //square each number in the array
        
        for (int i=0;i<nums.size();i++){
        nums[i]=pow(nums[i],2);
        }
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]>nums[j]){
                    nums[i]=nums[i]+nums[j];
                    nums[j]=nums[i]-nums[j];
                    nums[i]=nums[i]-nums[j];
                }
                
            }
        }
        return nums;
        
        
    }
};

// (n) 

//{-4,3,2,1}
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
            int sizeofArray=nums.size();
            vector<int> sorted(sizeofArray);
        int left=0; //1,2,3
        int right=sizeofArray-1;
        int pos=sizeofArray-1;
        
        while(left<=right){
            int leftSquared=nums[left]*nums[left]; 
            int rightSquared=nums[right]*nums[right]; 
             
            if(leftSquared>rightSquared){ 
                sorted[pos]=leftSquared; 
                left++;
            }
            else{
                sorted[pos]=rightSquared;
                right--;
            }
            pos--;
            
}
        return sorted;
        
        
        
    }
};
