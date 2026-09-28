class Solution:
    def isAnagram(self, str1: str, str2: str):
        if len(str1) != len(str2):
            return False
        set1, set2 = {}, {}  # storing in hash set to count the freq of each chars
        for i in range(len(str1)):
            set1[str1[i]] = 1 + set1.get(str1[i], 0)
            set2[str2[i]] = 1 + set2.get(str2[i], 0)
        if set1 == set2:
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
        # # a visited hashmap
        visited = {i: 1 for i in range(len(strs))}

        # naive approach
        for i in range(len(strs)):
            sublist = []
            for j in range(len(strs) - 1, i, -1):
                if (visited.get(i) == 1 or visited.get(j) == 1) and self.isAnagram(
                    strs[i], strs[j]
                ):
                    if visited.get(i) == 1:
                        sublist.append(strs[i])
                        visited[i] = 0
                    if visited.get(j) == 1:
                        sublist.append(strs[j])
                        visited[j] = 0
            if len(sublist):
                result.append(sublist)

        for key in visited:
            if visited.get(key) == 1:
                result.append([strs[key]])

        return result
