class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
     int freq_map[26]={0};

     for(char x:magazine){
        freq_map[x-'a']++;
     }   
     for(char x:ransomNote){

        if(freq_map[x-'a']<=0){
            return false;
            break;
        }
        freq_map[x-'a']--;
     }
     return true;
    }
};