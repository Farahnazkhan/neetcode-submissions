class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_group = defaultdict(list)
        for string in strs:
            str_list = [0]*26
            for s in string:
                str_list[ord(s)-ord('a')] += 1
            str_tuple = tuple(str_list)
            final_group[str_tuple].append(string)        
        return list(final_group.values())