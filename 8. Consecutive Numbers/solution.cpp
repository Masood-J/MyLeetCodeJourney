#include <iostream>
#include <vector>
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums,int NumberToBeChecked) {
int totalOnes{0};
        vector<int> SeenOnes;
        for (int i=0;i<nums.size();i++){
if(nums[i]==NumberToBeChecked){
totalOnes++;}
            else if(nums[i]!=NumberToBeChecked){
                SeenOnes.push_back(totalOnes);
                totalOnes=0;   
            }
            
        }
        SeenOnes.push_back(totalOnes);
        int highest_num{0};
        for(int i=0;i<SeenOnes.size();i++){
            if(SeenOnes[i]>highest_num){
                highest_num=SeenOnes[i];
            }
        }
  
        return highest_num;
    }
};