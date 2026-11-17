class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)

        i,j = 0,0
        resultlist = []

        while i < w1 and j < w2:
            resultlist.append(word1[i])
            resultlist.append(word2[j])

            i += 1
            j += 1

        while i < w1:
            resultlist.append(word1[i])
            i += 1

        while j < w2:
            resultlist.append(word2[j])
            j += 1

        return "".join(resultlist)