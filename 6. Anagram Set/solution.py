class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams=defaultdict(list);
        grouped_list=list()
        for charac in strs:
            sorted_charac="".join(sorted(charac))
            group_anagrams[sorted_charac].append(charac)
        for index,value in enumerate(group_anagrams):
            grouped_list.append(group_anagrams.get(value))
        
        return grouped_list


        