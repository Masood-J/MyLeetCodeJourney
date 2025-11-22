class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Map_charac=dict()
        track_charac=set()
        for index,charac in enumerate(s):
            if charac not in Map_charac:
             if(t[index] not in track_charac):
                Map_charac[charac]=t[index]
                track_charac.add(t[index])
                continue;
            if(Map_charac.get(charac)!=t[index]):
                return False;
                break;
            
        return True

        