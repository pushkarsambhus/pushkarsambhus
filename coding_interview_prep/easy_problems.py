"""
EASY CODING INTERVIEW PROBLEMS - Python
========================================
Instructions: Solve each problem on your own. No solutions here — just the questions!
Topics: Arrays, Strings, Hashing, Stack, Linked List, Trees, Binary Search, DP
"""

# ─────────────────────────────────────────────────────────────────────────────
# ARRAYS & HASHING
# ─────────────────────────────────────────────────────────────────────────────

# 1. TWO SUM
# Given a list of integers and a target, return the indices of two numbers
# that add up to the target. Assume exactly one solution exists.
# Example: nums = [2, 7, 11, 15], target = 9 → [0, 1]


# 2. CONTAINS DUPLICATE
# Given a list of integers, return True if any value appears at least twice,
# and False if every element is distinct.
# Example: [1, 2, 3, 1] → True


# 3. VALID ANAGRAM
# Given two strings s and t, return True if t is an anagram of s.
# Example: s = "anagram", t = "nagaram" → True


# 4. GROUP ANAGRAMS (Easy version: just detect, not group)
# Given a list of strings, determine which strings are anagrams of each other.
# Example: ["eat", "tea", "tan"] → "eat" and "tea" are anagrams


# 5. MISSING NUMBER
# Given a list containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing.
# Example: [3, 0, 1] → 2


# ─────────────────────────────────────────────────────────────────────────────
# STRINGS
# ─────────────────────────────────────────────────────────────────────────────

# 6. VALID PALINDROME
# Given a string, determine if it is a palindrome considering only
# alphanumeric characters and ignoring case.
# Example: "A man, a plan, a canal: Panama" → True


# 7. REVERSE A STRING
# Write a function that reverses a string in-place (using a list of characters).
# Example: ["h","e","l","l","o"] → ["o","l","l","e","h"]


# 8. FIRST UNIQUE CHARACTER IN A STRING
# Given a string, find the first non-repeating character and return its index.
# If it doesn't exist, return -1.
# Example: "leetcode" → 0


# 9. IS SUBSEQUENCE
# Given two strings s and t, return True if s is a subsequence of t.
# Example: s = "ace", t = "abcde" → True


# 10. LONGEST COMMON PREFIX
# Find the longest common prefix string among a list of strings.
# Return an empty string "" if there is no common prefix.
# Example: ["flower","flow","flight"] → "fl"


# ─────────────────────────────────────────────────────────────────────────────
# STACK & QUEUE
# ─────────────────────────────────────────────────────────────────────────────

# 11. VALID PARENTHESES
# Given a string containing '(', ')', '{', '}', '[', ']',
# determine if the input string is valid (properly opened and closed).
# Example: "()[]{}" → True, "(]" → False


# 12. IMPLEMENT A STACK USING QUEUES
# Implement a stack (LIFO) using only standard queue operations.


# ─────────────────────────────────────────────────────────────────────────────
# BINARY SEARCH
# ─────────────────────────────────────────────────────────────────────────────

# 13. BINARY SEARCH
# Given a sorted list and a target, return the index of the target
# or -1 if it doesn't exist. Must be O(log n).
# Example: nums = [-1, 0, 3, 5, 9, 12], target = 9 → 4


# 14. FIRST BAD VERSION
# You have n versions. Given a function isBadVersion(version) → bool,
# find the first bad version. Minimize API calls.


# 15. SEARCH INSERT POSITION
# Given a sorted list and a target, return the index if found,
# or the index where it would be inserted.
# Example: [1, 3, 5, 6], target = 5 → 2


# ─────────────────────────────────────────────────────────────────────────────
# LINKED LIST
# ─────────────────────────────────────────────────────────────────────────────

# 16. REVERSE A LINKED LIST
# Given the head of a singly linked list, reverse it and return the new head.
# Example: 1 → 2 → 3 → 4 → 5 → 5 → 4 → 3 → 2 → 1


# 17. MERGE TWO SORTED LINKED LISTS
# Merge two sorted linked lists and return the merged list (also sorted).
# Example: 1→2→4 and 1→3→4 → 1→1→2→3→4→4


# 18. LINKED LIST CYCLE DETECTION
# Given a linked list, determine if it contains a cycle.
# Use Floyd's Tortoise and Hare algorithm.


# ─────────────────────────────────────────────────────────────────────────────
# TREES
# ─────────────────────────────────────────────────────────────────────────────

# 19. INVERT BINARY TREE
# Given the root of a binary tree, invert it (mirror it) and return the root.
# Example:
#       4              4
#      / \    →       / \
#     2   7          7   2


# 20. MAXIMUM DEPTH OF BINARY TREE
# Given the root of a binary tree, return its maximum depth.
# Example: [3, 9, 20, null, null, 15, 7] → 3


# 21. SYMMETRIC TREE
# Given a binary tree, check whether it is a mirror of itself (symmetric).
# Example: [1, 2, 2, 3, 4, 4, 3] → True


# 22. PATH SUM
# Given a binary tree and a target sum, return True if the tree has a
# root-to-leaf path such that adding up all values equals targetSum.


# ─────────────────────────────────────────────────────────────────────────────
# DYNAMIC PROGRAMMING
# ─────────────────────────────────────────────────────────────────────────────

# 23. CLIMBING STAIRS
# You can climb 1 or 2 steps at a time. In how many distinct ways
# can you climb to the top of n stairs?
# Example: n = 3 → 3


# 24. MAXIMUM SUBARRAY (Kadane's Algorithm)
# Find the contiguous subarray with the largest sum and return the sum.
# Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6


# 25. BEST TIME TO BUY AND SELL STOCK
# Given daily prices, find the max profit from a single buy and sell.
# You must buy before you sell. Return 0 if no profit is possible.
# Example: [7, 1, 5, 3, 6, 4] → 5


# ─────────────────────────────────────────────────────────────────────────────
# MATH & BIT MANIPULATION
# ─────────────────────────────────────────────────────────────────────────────

# 26. REVERSE INTEGER
# Given a signed 32-bit integer, reverse its digits.
# Return 0 if the reversed number overflows.
# Example: 123 → 321, -120 → -21


# 27. POWER OF TWO
# Given an integer n, return True if it is a power of two.
# Example: n = 16 → True, n = 3 → False


# 28. SINGLE NUMBER
# Given a list where every element appears twice except for one,
# find that single one. Must be O(n) time and O(1) space.
# Example: [4, 1, 2, 1, 2] → 4


# 29. COUNT BITS
# Given an integer n, return a list of the number of 1's in the binary
# representation of every number in the range [0, n].
# Example: n = 5 → [0, 1, 1, 2, 1, 2]


# 30. HAPPY NUMBER
# A number is "happy" if repeatedly replacing it with the sum of the
# squares of its digits eventually leads to 1.
# Return True or False.
# Example: 19 → True


# ─────────────────────────────────────────────────────────────────────────────
# MISC / GRID
# ─────────────────────────────────────────────────────────────────────────────

# 31. FLOOD FILL
# Given an image (2D grid), a starting pixel, and a new color,
# perform a flood fill (like paint bucket tool).
# Change the color of the starting pixel and all connected same-color pixels.


# 32. FIBONACCI NUMBER
# Compute the nth Fibonacci number.
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
# Solve iteratively (no recursion).


# 33. ROMAN TO INTEGER
# Convert a Roman numeral string to an integer.
# Example: "IX" → 9, "LVIII" → 58


# 34. MAJORITY ELEMENT
# Given a list of size n, find the element that appears more than n//2 times.
# Assume the majority element always exists.
# Solve with O(1) extra space using Boyer-Moore Voting.
# Example: [2, 2, 1, 1, 1, 2, 2] → 2


# 35. MOVE ZEROES
# Given a list, move all 0's to the end while maintaining the relative order
# of non-zero elements. Do this in-place.
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
