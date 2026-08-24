class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers - O(1) space and O(n) time [in place]
        l = 0
        r = len(s) - 1
        # s = s.lower()
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            if l >=r:
                return True
            l += 1
            r -= 1
        return True
            