class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        
        int curr_max=nums[0];
        int global_max=nums[0];

for(int i=1;i<nums.size();i++){//[2,3,4][2][2,3][2,3,4],[3],[3,4],[4]
curr_max=max(nums[i],curr_max+nums[i]);

global_max=max(global_max,curr_max);


}
        return global_max;
        
    }
};