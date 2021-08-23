class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_1 = str(x)
        str_2 = ''
        for c in str_1:
            str_2 = c + str_2
        return str_1 == str_2
