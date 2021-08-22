class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        res = []
        cmap = defaultdict(list) # key is sorted word: value is index in strings for word
        for i, s in enumerate(strings):
            c = "".join(sorted(s))
            if c in cmap: cmap[c].append(i)
            else: cmap[c] = [i]
        
        for indexes in cmap.values(): res.append([strings[i] for i in indexes])
            
        return res