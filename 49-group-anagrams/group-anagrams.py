class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for word in strs:
            w = sorted(word)

            w1 = ""
            for c in w:
                w1 += c

            mp[w1].append(word)

        print(mp)
        res = []
        for word in mp:
            row = []

            for w in mp[word]:
                row.append(w)

            res.append(row)

        return res