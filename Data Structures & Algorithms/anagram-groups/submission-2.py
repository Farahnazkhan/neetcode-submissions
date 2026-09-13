class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_group = defaultdict(list)
        for s in strs:
            str_list = [0]*26
            for c in s:
                str_list[ord(c)-ord('a')] += 1
            final_group[tuple(str_list)].append(s)        
        return list(final_group.values())