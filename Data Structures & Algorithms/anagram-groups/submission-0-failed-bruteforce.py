class Solution:
  # failed because of inefficient time complexity for hidden very large test cases 35/45 passed
  # Time Complexity:
  # isAnagram() → O(k), where k = length of a string
  # Nested loops → O(n²), where n = number of strings
  # Overall → O(n² * k)
  #
  # Space Complexity:
  # visited → O(n)
  # set1, set2 → O(k)
  # Overall auxiliary space → O(n + k)
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
                if self.isAnagram(strs[i], strs[j]):
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
