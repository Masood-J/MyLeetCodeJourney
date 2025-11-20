#include <iostream>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {


        int frequency_map[26]={0};
        if(s.size()!=t.size()){
            return false;
        }
        for(char x:s){
            frequency_map[x-'a']++;
        }
        for(char x:t){
            frequency_map[x-'a']--;
        }

        for(int counts:frequency_map){
            if(counts!=0){
                return false;
                break;
            }
        }
        return true;

    }
};

int main() {
    Solution S1;
    cout<<S1.isAnagram("ann","naa");
    return 0;
}