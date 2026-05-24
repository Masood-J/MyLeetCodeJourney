class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int evenPointer{0};
        
        for(int i=0;i<nums.size();i++){
          int temp_var{0};
if(nums[i]%2==0){
    temp_var=nums[evenPointer];
    nums[evenPointer]=nums[i];
    nums[i]=temp_var;
    evenPointer++;
}
        }
        
        return nums;
    }
};