class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        bool isSatisfied=false;
        for (int i=0;i<arr.size();i++){
            if(isSatisfied==true){
                break;
            }
            for(int j=0;j<arr.size();j++){
                if(j==i){
                    continue;
                }
                if(arr[i]==arr[j]*2){
                    isSatisfied=true;
                    break;
                }
            }
        }
        
        return isSatisfied;
    }
};