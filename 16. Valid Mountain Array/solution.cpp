class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        
    bool isDown=false;
    if(arr.size()<3 || arr[1]<arr[0] ||arr[arr.size()-1]>arr[arr.size()-2])
    { return false; }
        for(int i=0,j=i+1;j<arr.size();i++,j++){
            if(isDown==false){
            if(arr[j]>arr[i]){
                continue;
            }
                else{
                    isDown=true;
                }
            }
            if(isDown==true){
                if(arr[j]<arr[i]){
                    continue;
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
};