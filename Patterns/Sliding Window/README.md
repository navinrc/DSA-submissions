# Sliding Window

Sliding window problems maintain a range of elements with two pointers, expanding or shrinking the range as the input is processed.

## Problems

| Problem | Window type | Pattern solution | Solved problem | Notes |
| --- | --- | --- | --- | --- |
| Maximum sum of a subarray of size `k` | Fixed length | [Implementation](01_max_sum_of_subarray_size_k.py) | Non-LeetCode practice problem | Maintains a running sum and removes the outgoing value after each full window |
| Maximum Points You Can Obtain from Cards | Fixed length | [Implementation](../../Data%20Structures%20%26%20Algorithms/maximum-points-you-can-obtain-from-cards/submission-0.py) | [Solved submission](../../Data%20Structures%20%26%20Algorithms/maximum-points-you-can-obtain-from-cards/submission-0.py) | Finds the maximum score by subtracting each excluded window of size `n - k` from the total |
| Fruit Into Baskets | Variable length | [Implementation](../../Data%20Structures%20%26%20Algorithms/fruit-into-baskets/submission-0.py) | [Solved submission](../../Data%20Structures%20%26%20Algorithms/fruit-into-baskets/submission-0.py) | Shrinks the window until it contains at most two fruit types |
| Best Time to Buy and Sell Stock | Variable length | [Implementation](../../Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/submission-2.py) | [Solved submission](../../Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/submission-2.py) | Tracks the lowest buying price and compares it with each later price |