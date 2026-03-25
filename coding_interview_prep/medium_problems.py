"""
MEDIUM CODING INTERVIEW PROBLEMS - Python
==========================================
Instructions: Solve each problem on your own. No solutions here — just the questions!
Topics: Arrays, Strings, Sliding Window, Two Pointers, Backtracking,
        Trees, Graphs, DP, Heaps, Binary Search, Intervals, Greedy
"""

# ─────────────────────────────────────────────────────────────────────────────
# ARRAYS & HASHING
# ─────────────────────────────────────────────────────────────────────────────

# 1. TOP K FREQUENT ELEMENTS
# Given a list of integers and k, return the k most frequent elements.
# Example: [1,1,1,2,2,3], k=2 → [1, 2]


# 2. PRODUCT OF ARRAY EXCEPT SELF
# Return a list where output[i] is the product of all elements except nums[i].
# No division allowed. Must be O(n).
# Example: [1,2,3,4] → [24,12,8,6]


# 3. LONGEST CONSECUTIVE SEQUENCE
# Given an unsorted list, find the length of the longest consecutive sequence.
# Must be O(n).
# Example: [100,4,200,1,3,2] → 4 (sequence: 1,2,3,4)


# 4. VALID SUDOKU
# Determine if a 9×9 Sudoku board is valid. Only filled cells need to be validated.
# Rules: each row, column, and 3×3 box must contain digits 1–9 without repetition.


# 5. ENCODE AND DECODE STRINGS
# Design an algorithm to encode a list of strings into a single string,
# and decode it back to the original list.


# ─────────────────────────────────────────────────────────────────────────────
# TWO POINTERS & SLIDING WINDOW
# ─────────────────────────────────────────────────────────────────────────────

# 6. TWO SUM II (SORTED INPUT)
# Given a sorted list, find two numbers that add to the target.
# Must use O(1) extra space.
# Example: [2,7,11,15], target=9 → [1, 2] (1-indexed)


# 7. 3SUM
# Find all unique triplets in the list that sum to zero.
# The solution must not contain duplicate triplets.
# Example: [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]


# 8. CONTAINER WITH MOST WATER
# Given heights of lines, find two lines that together with the x-axis form
# a container that holds the most water.
# Example: [1,8,6,2,5,4,8,3,7] → 49


# 9. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# Find the length of the longest substring without repeating characters.
# Example: "abcabcbb" → 3


# 10. LONGEST REPEATING CHARACTER REPLACEMENT
# You may replace at most k characters. Find the length of the longest
# substring containing the same letter after replacements.
# Example: s="AABABBA", k=1 → 4


# 11. MINIMUM SIZE SUBARRAY SUM
# Given a list and target, return the minimum length subarray whose sum
# is >= target. Return 0 if no such subarray exists.
# Example: [2,3,1,2,4,3], target=7 → 2


# ─────────────────────────────────────────────────────────────────────────────
# STACK & QUEUES
# ─────────────────────────────────────────────────────────────────────────────

# 12. DAILY TEMPERATURES
# Given temperatures, return a list where output[i] is the number of days
# until a warmer temperature. 0 if no future warmer day.
# Example: [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]


# 13. EVALUATE REVERSE POLISH NOTATION
# Evaluate the value of an expression in Reverse Polish Notation.
# Example: ["2","1","+","3","*"] → 9


# 14. MIN STACK
# Design a stack that supports push, pop, top, and retrieving the minimum
# element — all in O(1) time.


# ─────────────────────────────────────────────────────────────────────────────
# BINARY SEARCH
# ─────────────────────────────────────────────────────────────────────────────

# 15. FIND MINIMUM IN ROTATED SORTED ARRAY
# A sorted array was rotated. Find the minimum element.
# Example: [3,4,5,1,2] → 1


# 16. SEARCH IN ROTATED SORTED ARRAY
# Search for a target in a rotated sorted array.
# Return index or -1. Must be O(log n).
# Example: [4,5,6,7,0,1,2], target=0 → 4


# 17. KOKO EATING BANANAS
# Koko can eat k bananas/hour. Find the minimum k such that she can finish
# all piles within h hours.
# Example: piles=[3,6,7,11], h=8 → 4


# ─────────────────────────────────────────────────────────────────────────────
# LINKED LIST
# ─────────────────────────────────────────────────────────────────────────────

# 18. REORDER LIST
# Given a linked list L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# Do it in-place.


# 19. REMOVE NTH NODE FROM END OF LIST
# Given a linked list, remove the nth node from the end and return the head.
# Example: 1→2→3→4→5, n=2 → 1→2→3→5


# 20. COPY LIST WITH RANDOM POINTER
# A linked list where each node has a next and random pointer.
# Make a deep copy of the list.


# ─────────────────────────────────────────────────────────────────────────────
# TREES
# ─────────────────────────────────────────────────────────────────────────────

# 21. BINARY TREE LEVEL ORDER TRAVERSAL
# Return the level-order traversal of a binary tree as a list of lists.
# Example: [3,9,20,null,null,15,7] → [[3],[9,20],[15,7]]


# 22. VALIDATE BINARY SEARCH TREE
# Given a binary tree, determine if it is a valid BST.


# 23. KTH SMALLEST ELEMENT IN A BST
# Given a BST, find the kth smallest value (1-indexed).
# Example: BST = [3,1,4,null,2], k=1 → 1


# 24. CONSTRUCT BINARY TREE FROM PREORDER AND INORDER TRAVERSAL
# Given preorder and inorder traversal arrays, construct the binary tree.


# 25. LOWEST COMMON ANCESTOR OF A BINARY TREE
# Given a binary tree, find the LCA of two given nodes p and q.


# ─────────────────────────────────────────────────────────────────────────────
# GRAPHS
# ─────────────────────────────────────────────────────────────────────────────

# 26. NUMBER OF ISLANDS
# Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and formed by connecting adjacent land cells.
# Example: [["1","1","0"],["0","1","0"],["0","0","1"]] → 2


# 27. CLONE GRAPH
# Given a reference to a node in an undirected graph, return a deep copy.


# 28. PACIFIC ATLANTIC WATER FLOW
# Find all cells where water can flow to both the Pacific and Atlantic oceans.
# Water flows from high to equal or lower cells.


# 29. COURSE SCHEDULE
# Given numCourses and prerequisites as [a, b] pairs (b must be done before a),
# determine if it's possible to finish all courses.
# Example: 2, [[1,0]] → True; 2, [[1,0],[0,1]] → False


# 30. COURSE SCHEDULE II (TOPOLOGICAL SORT)
# Return a valid course ordering, or [] if impossible.


# ─────────────────────────────────────────────────────────────────────────────
# BACKTRACKING
# ─────────────────────────────────────────────────────────────────────────────

# 31. SUBSETS
# Return all possible subsets (the power set) of a list of unique integers.
# Example: [1,2,3] → [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]


# 32. PERMUTATIONS
# Return all permutations of a list of distinct integers.
# Example: [1,2,3] → all 6 orderings


# 33. COMBINATION SUM
# Find all unique combinations from candidates that sum to target.
# You may reuse numbers.
# Example: candidates=[2,3,6,7], target=7 → [[2,2,3],[7]]


# 34. WORD SEARCH
# Given a 2D board and a word, return True if the word exists in the grid.
# The word must be formed by sequentially adjacent cells (horizontal or vertical).
# Each cell can be used only once.


# ─────────────────────────────────────────────────────────────────────────────
# DYNAMIC PROGRAMMING
# ─────────────────────────────────────────────────────────────────────────────

# 35. COIN CHANGE
# Given coins of certain denominations, find the fewest coins needed
# to make the amount. Return -1 if impossible.
# Example: coins=[1,5,10,25], amount=36 → 3


# 36. UNIQUE PATHS
# A robot is on an m×n grid, starting at top-left.
# It can only move right or down. Count distinct paths to bottom-right.
# Example: m=3, n=7 → 28


# 37. LONGEST INCREASING SUBSEQUENCE
# Find the length of the longest strictly increasing subsequence.
# Example: [10,9,2,5,3,7,101,18] → 4


# 38. HOUSE ROBBER
# You cannot rob two adjacent houses. Find the max amount you can rob.
# Example: [2,7,9,3,1] → 12


# 39. HOUSE ROBBER II (CIRCULAR)
# Same as House Robber but houses are in a circle (first and last are adjacent).
# Example: [2,3,2] → 3


# 40. JUMP GAME
# Given a list where each element is the max jump length from that position,
# return True if you can reach the last index.
# Example: [2,3,1,1,4] → True, [3,2,1,0,4] → False


# ─────────────────────────────────────────────────────────────────────────────
# INTERVALS & GREEDY
# ─────────────────────────────────────────────────────────────────────────────

# 41. MERGE INTERVALS
# Merge all overlapping intervals.
# Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]


# 42. INSERT INTERVAL
# Insert a new interval into a sorted list of non-overlapping intervals.
# Merge if necessary.
# Example: [[1,3],[6,9]], [2,5] → [[1,5],[6,9]]


# 43. NON-OVERLAPPING INTERVALS
# Find the minimum number of intervals to remove to make the rest non-overlapping.
# Example: [[1,2],[2,3],[3,4],[1,3]] → 1


# ─────────────────────────────────────────────────────────────────────────────
# HEAP / PRIORITY QUEUE
# ─────────────────────────────────────────────────────────────────────────────

# 44. KTH LARGEST ELEMENT IN AN ARRAY
# Find the kth largest element in an unsorted list.
# Example: [3,2,1,5,6,4], k=2 → 5


# 45. TASK SCHEDULER
# Given tasks and a cooldown n, find the minimum intervals needed to finish.
# Example: tasks=["A","A","A","B","B","B"], n=2 → 8
