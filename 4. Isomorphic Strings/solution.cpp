class Solution {
public:
    bool isIsomorphic(string s, string t) {

        unordered_map<char,char> connector;
        unordered_set<char> mapped_charac;
        for(int i=0;i<s.size();i++){
         if(connector.count(s[i]) == 0){
         if(!mapped_charac.count(t[i])){
           connector[s[i]]={t[i]};
           mapped_charac.insert(t[i]);
}
         else{
          return false;
          break;
}
continue;
}
         if(connector[s[i]]!=t[i]){
          return false;
          break;
}
        }
        return true; 
    }
};