# [2762. Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays)

**Type:** Medium <br>
**Topics:** Sliding Window, Array, Queue, Heap (Priority Queue), Ordered Set, Monotonic Queue, Two Pointers, Ordered Map, Hash Table <br>
**Companies:** Google, Yahoo, Amazon, Adobe, Uber
<hr>

You are given a **0-indexed** integer array `nums`. A subarray of `nums` is called **continuous** if:

- Let `i`, `i + 1`, ..., `j` be the indices in the subarray. Then, for each pair of indices <code>i <= i<sub>1</sub>, i<sub>2</sub> <= j</code>, <code>0 <= |nums[i<sub>1</sub>] - nums[<sub>2</sub>]| <= 2</code>.

Return *the total number of ***continuous*** subarrays*.

A subarray is a contiguous **non-empty** sequence of elements within an array.
<hr>

### Examples:

- **Example 1:** <br>
**Input:** nums = [5,4,2,4] <br>
**Output:** 8 <br>
**Explanation:** <br>
Continuous subarray of size 1: [5], [4], [2], [4]. <br>
Continuous subarray of size 2: [5,4], [4,2], [2,4]. <br>
Continuous subarray of size 3: [4,2,4]. <br>
Thereare no subarrys of size 4. <br>
Total continuous subarrays = 4 + 3 + 1 = 8. <br>
It can be shown that there are no more continuous subarrays.

- **Example 2:** <br>
**Input:** nums = [1,2,3] <br>
**Output:** 6 <br>
**Explanation:** <br>
Continuous subarray of size 1: [1], [2], [3]. <br>
Continuous subarray of size 2: [1,2], [2,3]. <br>
Continuous subarray of size 3: [1,2,3]. <br>
Total continuous subarrays = 3 + 2 + 1 = 6. 
<hr>

### Constraints:
- <code>1 <= nums.length <= 10<sup>5</sup></code>
- <code>1 <= nums[i] <= 10<sup>9</sup></code>

### Hints:
- Try using the sliding window technique.
- Use a set or map to keep track of the maximum and minimum of subarrays.