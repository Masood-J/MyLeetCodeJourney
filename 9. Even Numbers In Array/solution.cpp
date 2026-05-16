class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int totalevenNum{0};
        
        for(int i=0;i<nums.size();i++){
            int current_num=to_string(nums[i]).size();
      if(current_num%2==0){
          totalevenNum++;
      }
        
}
        return totalevenNum;
    }
};