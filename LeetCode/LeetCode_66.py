class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        i = int(s)
        a = i + 1
        ret = list(str(a))
        for c in range(len(ret)):
            ret[c] = int(ret[c])
        return ret
