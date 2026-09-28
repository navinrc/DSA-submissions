class Solution:

    def encode(self, strs: List[str]) -> str:
        return "$".join(str(s) for s in strs)
    def decode(self, s: str) -> List[str]:
        return s.split("$")