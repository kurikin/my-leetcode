class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        array = [int(d) for d in str(x)]
        length = len(array)

        for i in range(length // 2):
            if array[i] != array[length-i-1]:
                return False
        return True