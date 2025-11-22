class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charac_pool=dict()
        for charac in magazine:
            charac_pool[charac]=charac_pool.get(charac,0)+1
        for charac in ransomNote:
            current_count = charac_pool.get(charac, 0)
            if(current_count==0):
                return False
                
            charac_pool[charac] -= 1
        return True
        