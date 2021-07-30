class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        p = 0
        q = len(s1) - 1
        while q > p:
            p = move_p(s1, p, q)
            q = move_q(s1, p, q)
            if q - p <= 2:
                break
            if s1[p] != s1[q]:
                return False
            p += 1
            q -= 1
            p = move_p(s1, p, q)
            q = move_q(s1, p, q)
        if q - p < 1:
            return True
        else:
            if s1[p] == s1[q]:
                return True
            else:
                return False
    
def move_p(s, p, q):
    n1 = ord(s[p])
    while ((n1 < 48) or \
        (n1 > 57 and n1 < 97) or \
        (n1 > 122)) and \
        (p < q):
            p += 1
            n1 = ord(s[p])
    return p

def move_q(s, p, q):
    n2 = ord(s[q])
    while ((n2 < 48) or \
        (n2 > 57 and n2 < 97) or \
        (n2 > 122)) and \
        (q > p):
            q -= 1
            n2 = ord(s[q])
    return q
