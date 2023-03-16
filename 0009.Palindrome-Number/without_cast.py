class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        input = x
        reverse = 0

        while input > 0:
            reverse *= 10
            reverse += input % 10
            input = input // 10

        return x == reverse