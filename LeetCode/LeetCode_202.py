class Solution:
    def isHappy(self, n: int) -> bool:
        def func(num):
            s = str(num)
            ret = 0
            for c in s:
                ret += int(c) ** 2
            return ret
        
        
        p = n
        q = n
        while True:
            p = func(p)
            p = func(p)
            q = func(q)
            if p == 1 or q == 1:
                return True
            if p == q:
                return False
