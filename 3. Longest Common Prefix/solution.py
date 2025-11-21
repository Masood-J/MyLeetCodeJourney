class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0];
        for data in strs:
            while not data.startswith(prefix):
                prefix = prefix[0:len(prefix)-1]

                if(len(prefix)==0):
                    return "";
                    break;
                
            

        return prefix;