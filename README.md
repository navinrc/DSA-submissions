# DSA Problems and Patterns

Solved data structures and algorithms problems, organized alongside reusable problem-solving patterns.

## Patterns

- [Sliding Window](Patterns/Sliding%20Window/README.md)
- [Two Pointers](Patterns/Two%20Pointers/README.md)

## Generic Arrays Problems

| Problem | LeetCode | Solution | Notes
| --- | --- | --- | --- |
| Anagram Groups | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Solved submission](Data%20Structures%20%26%20Algorithms/anagram-groups/submission-4.py) | Using frequency count stored as a key in a hash map to group anagrams |
| Duplicate Integer | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Solved submission](Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-2.py) | Detecting duplicates with a set |
| Two Integer Sum | [Two Sum](https://leetcode.com/problems/two-sum/) | [Solved submission](Data%20Structures%20%26%20Algorithms/two-integer-sum/submission-2.py) | Finding a complement with a hash map |
| Top K Elements in List | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Solved submission](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list/submission-3.py) | Using frequency counting and bucket sort |
| Products of Array Except Self | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [Submission 1](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/submission-1.py) / [Submission 2](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/submission-2.py) | Submission 1: builds separate prefix and suffix product arrays, then multiplies `prefix[i-1] * suffix[i+1]` (O(n) extra space). Submission 2: stores running prefix products in the result, then multiplies in a running postfix on a reverse pass (O(1) extra space) |
| Longest Consecutive Sequence | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [Submission 1](Data%20Structures%20%26%20Algorithms/longest-consecutive-sequence/submission-1.py) / [Submission 2](Data%20Structures%20%26%20Algorithms/longest-consecutive-sequence/submission-2.py) | Puts nums in a hash set, starts counting only from sequence starts (`n - 1` not in set) and extends while `n + length` is in the set. Submission 1 iterates `nums`, so duplicate starts get re-scanned (can degrade to O(n²)). Submission 2 iterates the set, so each start is scanned once (true O(n)) |

## Basic String Problems

| Problem | LeetCode | Solution | Notes |
| --- | --- | --- | --- |
| Is Anagram | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Solved submission](Data%20Structures%20%26%20Algorithms/is-anagram/submission-2.py) | Comparing character frequencies with hash maps |
| Is Palindrome | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Solved submission](Data%20Structures%20%26%20Algorithms/is-palindrome/submission-4.py) | Comparing characters with two pointers |
| Encode and Decode Strings | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (premium) / [NeetCode](https://neetcode.io/problems/string-encode-and-decode/question) | [Solved submission](Data%20Structures%20%26%20Algorithms/string-encode-and-decode/submission-2.py) | Using length-prefixed encoding to serialize and deserialize strings |

## Stack Problems

| Problem | LeetCode | Solution | Notes |
| --- | --- | --- | --- |
| Validate Parentheses | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Solved submission](Data%20Structures%20%26%20Algorithms/validate-parentheses/submission-1.py) | Matching closing brackets with a stack |
