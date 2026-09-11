# Sliding Window

Sliding window problems maintain a range of elements with two pointers, expanding or shrinking the range as the input is processed.

## Problems

| Problem | LeetCode | Window type | Pattern solution | Solved problem | Notes |
| --- | --- | --- | --- | --- | --- |
| Maximum sum of a subarray of size `k` | — | Fixed length | [Implementation](01_max_sum_of_subarray_size_k.py) | Non-LeetCode practice problem | Maintains a running sum and removes the outgoing value after each full window |
| Maximum Points You Can Obtain from Cards | [LeetCode 1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Fixed length | [Implementation](../../Data%20Structures%20%26%20Algorithms/maximum-points-you-can-obtain-from-cards/submission-0.py) | [Solved submission](../../Data%20Structures%20%26%20Algorithms/maximum-points-you-can-obtain-from-cards/submission-0.py) | Finds the maximum score by subtracting each excluded window of size `n - k` from the total |
| Fruit Into Baskets | [LeetCode 904](https://leetcode.com/problems/fruit-into-baskets/) | Variable length | [Implementation](../../Data%20Structures%20%26%20Algorithms/fruit-into-baskets/submission-0.py) | [Solved submission](../../Data%20Structures%20%26%20Algorithms/fruit-into-baskets/submission-0.py) | Shrinks the window until it contains at most two fruit types |
| Best Time to Buy and Sell Stock | [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Variable length | [Implementation](../../Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/submission-2.py) | [Solved submission](../../Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/submission-2.py) | Tracks the lowest buying price and compares it with each later price |