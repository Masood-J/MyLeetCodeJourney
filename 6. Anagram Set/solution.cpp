class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string,vector<string>> anagram_check;
        vector<vector<string>> anagram_set;

        for(string charac:strs){
            string key=charac;
            sort(key.begin(),key.end());
            anagram_check[key].push_back(charac);
        }
        for(const auto&[key,group]:anagram_check){
            anagram_set.push_back(group);
        }
        return anagram_set;

      
        
    }
};