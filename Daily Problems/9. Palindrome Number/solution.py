import math

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        j = -1
        for i in range(math.floor(len(str(x)) / 2)):
            if str(x)[i] != str(x)[j]:
                return False   
            j = j - 1
        return True