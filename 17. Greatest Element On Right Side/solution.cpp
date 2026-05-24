//(n)^2
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        if(arr.size()==1){
            arr[0]=-1;
            return arr;
        }
        for(int i=0;i<arr.size()-1;i++){//1
            int currentlargestNumber{0};
            for(int j=i+1;j<arr.size();j++){//2
                
                if(arr[j]>currentlargestNumber){
                    currentlargestNumber=arr[j];
                }
            }
            if(currentlargestNumber!=0){
                arr[i]=currentlargestNumber;
            }
        }
        arr[arr.size()-1]=-1;
        return arr;
        
    }
};

// (n):
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        if(arr.size()==1){
            arr[0]=-1;
            return arr;
        }
        int maxRight = -1;

for (int i = arr.size() - 1; i >= 0; i--) {
    int current = arr[i];
    arr[i] = maxRight;
    maxRight = max(maxRight, current);
}
        
        return arr;
        
    }
};