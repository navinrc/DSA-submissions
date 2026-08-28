class Solution:
    # 4#str3#str2 approach where we encode with len(str)#strlen(str2)#str2
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # we read s char by char until we find the delim '#'
    # get the len of str before #
    # append the chars upto len (found above) to res list
    # repeat
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length #! end of the current string
        return res
