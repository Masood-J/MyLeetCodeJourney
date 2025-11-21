class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_dict=dict()
        for charac in s:
            word_dict[charac]=word_dict.get(charac,0)+1
        for index,charac in enumerate(s):
            if(word_dict.get(charac)==1):
                return index
                break;
            
        return -1