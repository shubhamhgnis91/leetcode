class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []

        d = {}
        for word in dictionary:
            d[word] = d.get(word, 0) + 1

        s = sentence.split(" ")
        subS = False


        for word in s:
            subS = False
            w = ""
            for i in range(len(word)):
                w += word[i]
                if w in d:
                    res.append(w)
                    subS = True
                    break
            if not subS:
                res.append(word)

        return ' '.join(res)

        
                




        




        
        