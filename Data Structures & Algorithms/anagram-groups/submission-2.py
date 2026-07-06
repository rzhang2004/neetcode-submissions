class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        groups = defaultdict(list)
        
        for s in strs:
            letter_freq = {letter:0 for letter in alpha}
            for l in s:
                letter_freq[l] += 1

            primary_key = tuple(letter_freq.items())
            groups[primary_key].append(s)

        return list(groups.values())
            