class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedString = "".join([char for char in s if char.isalnum()]).lower()
        isPal = True
        if cleanedString != cleanedString[::-1]:
            isPal = False
        return isPal