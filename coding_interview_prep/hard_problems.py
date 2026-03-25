"""
HARD CODING INTERVIEW PROBLEMS - Python
========================================
Instructions: Solve each problem on your own. No solutions here — just the questions!
Topics: DP, Graphs, Sliding Window, Heaps, Trees, Tries, Binary Search,
        Monotonic Stack, Backtracking, Advanced Algorithms
"""

# ─────────────────────────────────────────────────────────────────────────────
# ARRAYS & SLIDING WINDOW
# ─────────────────────────────────────────────────────────────────────────────

# 1. TRAPPING RAIN WATER
# Given n non-negative integers representing an elevation map,
# compute how much water it can trap after raining.
# Example: [0,1,0,2,1,0,1,3,2,1,2,1] → 6


# 2. SLIDING WINDOW MAXIMUM
# Given a list and a window size k, return the maximum of each sliding window.
# Must be O(n) using a monotonic deque.
# Example: [1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]


# 3. MINIMUM WINDOW SUBSTRING
# Find the smallest substring of s that contains all characters of t.
# Example: s="ADOBECODEBANC", t="ABC" → "BANC"


# 4. LONGEST SUBSTRING WITH AT MOST K DISTINCT CHARACTERS
# Find the length of the longest substring with at most k distinct characters.
# Example: s="eceba", k=2 → 3 ("ece")


# 5. MAXIMUM PROFIT WITH AT MOST K TRANSACTIONS
# Given prices and k, find the max profit with at most k buy/sell transactions.
# You cannot hold more than one stock at a time.
# Example: k=2, prices=[3,2,6,5,0,3] → 7


# ─────────────────────────────────────────────────────────────────────────────
# STACK & MONOTONIC STRUCTURES
# ─────────────────────────────────────────────────────────────────────────────

# 6. LARGEST RECTANGLE IN HISTOGRAM
# Given heights of bars in a histogram, find the largest rectangle area.
# Example: [2,1,5,6,2,3] → 10


# 7. MAXIMAL RECTANGLE
# Given a 2D binary matrix, find the largest rectangle containing only 1s.
# (Hint: use largest rectangle in histogram per row)
# Example: [["1","0","1","0","0"],["1","0","1","1","1"],...] → 6


# 8. BASIC CALCULATOR
# Implement a basic calculator to evaluate a string expression
# containing '+', '-', '(', ')'. No multiplication or division.
# Example: "(1+(4+5+2)-3)+(6+8)" → 23


# ─────────────────────────────────────────────────────────────────────────────
# BINARY SEARCH
# ─────────────────────────────────────────────────────────────────────────────

# 9. MEDIAN OF TWO SORTED ARRAYS
# Find the median of two sorted arrays in O(log(min(m,n))) time.
# Example: nums1=[1,3], nums2=[2] → 2.0


# 10. SPLIT ARRAY LARGEST SUM
# Split an array into k non-empty subarrays to minimize the largest subarray sum.
# Example: [7,2,5,10,8], k=2 → 18


# 11. FIND IN MOUNTAIN ARRAY
# A MountainArray interface supports .get(i) and .length().
# Find the minimum index of a target in a mountain array.
# You may call .get() at most 100 times.


# ─────────────────────────────────────────────────────────────────────────────
# TREES & GRAPHS
# ─────────────────────────────────────────────────────────────────────────────

# 12. BINARY TREE MAXIMUM PATH SUM
# A path in a binary tree can start and end at any node.
# Find the maximum sum of any path.
# Example: [-10,9,20,null,null,15,7] → 42


# 13. SERIALIZE AND DESERIALIZE BINARY TREE
# Design an algorithm to serialize a binary tree to a string
# and deserialize that string back to the tree.


# 14. BINARY TREE CAMERAS
# Place cameras on some nodes to monitor the entire tree.
# Each camera can monitor its parent, itself, and its children.
# Find the minimum number of cameras needed.


# 15. WORD LADDER
# Transform beginWord to endWord by changing one letter at a time.
# Each intermediate word must be in the word list.
# Return the number of words in the shortest transformation sequence.
# Example: beginWord="hit", endWord="cog", wordList=[...] → 5


# 16. ALIEN DICTIONARY
# Given a sorted list of words in an alien language,
# derive the order of characters in the alphabet.
# Return the characters in sorted order, or "" if invalid.


# 17. CRITICAL CONNECTIONS IN A NETWORK (BRIDGES)
# Given a network of servers and connections, find all critical connections
# (removing which disconnects the network). Use Tarjan's algorithm.
# Example: n=4, connections=[[0,1],[1,2],[2,0],[1,3]] → [[1,3]]


# ─────────────────────────────────────────────────────────────────────────────
# TRIE
# ─────────────────────────────────────────────────────────────────────────────

# 18. IMPLEMENT TRIE (PREFIX TREE)
# Implement a Trie with insert(word), search(word), and startsWith(prefix).


# 19. WORD SEARCH II
# Given a 2D board and a list of words, find all words that exist in the board.
# Each word must be formed by adjacent cells (horizontal/vertical).
# Use a Trie for efficiency.


# 20. DESIGN ADD AND SEARCH WORDS DATA STRUCTURE
# Implement a data structure that supports addWord(word) and
# search(word) where search supports '.' as a wildcard for any letter.


# ─────────────────────────────────────────────────────────────────────────────
# HEAP / ADVANCED DATA STRUCTURES
# ─────────────────────────────────────────────────────────────────────────────

# 21. FIND MEDIAN FROM DATA STREAM
# Implement a MedianFinder class that supports:
# - addNum(num): Add a number to the data stream.
# - findMedian(): Return the median of all numbers so far.
# Both operations must be O(log n). Use two heaps.


# 22. MERGE K SORTED LISTS
# Merge k sorted linked lists into one sorted linked list.
# Example: [[1,4,5],[1,3,4],[2,6]] → [1,1,2,3,4,4,5,6]


# 23. SMALLEST RANGE COVERING ELEMENTS FROM K LISTS
# Find the smallest range [a, b] such that at least one element from
# each of the k lists is in the range.


# ─────────────────────────────────────────────────────────────────────────────
# DYNAMIC PROGRAMMING
# ─────────────────────────────────────────────────────────────────────────────

# 24. EDIT DISTANCE
# Find the minimum number of operations (insert, delete, replace) to
# convert word1 into word2.
# Example: "horse" → "ros" → 3


# 25. REGULAR EXPRESSION MATCHING
# Implement regex matching with '.' and '*'.
# '.' matches any single character.
# '*' matches zero or more of the preceding element.
# Example: s="aab", p="c*a*b" → True


# 26. WILDCARD MATCHING
# Implement wildcard matching with '?' and '*'.
# '?' matches any single character.
# '*' matches any sequence of characters (including empty).
# Example: s="adceb", p="*a*b" → True


# 27. BURST BALLOONS
# Given balloons with numbers, burst them to maximize coins.
# Bursting balloon i gives nums[i-1] * nums[i] * nums[i+1] coins.
# Example: [3,1,5,8] → 167


# 28. PALINDROME PARTITIONING II (MIN CUTS)
# Find the minimum number of cuts to partition a string
# such that every substring is a palindrome.
# Example: "aab" → 1 (["aa","b"])


# 29. DISTINCT SUBSEQUENCES
# Count the number of distinct subsequences of s that equal t.
# Example: s="rabbbit", t="rabbit" → 3


# 30. INTERLEAVING STRING
# Given s1, s2, s3, determine if s3 is formed by interleaving s1 and s2.
# Example: s1="aabcc", s2="dbbca", s3="aadbbcbcac" → True


# ─────────────────────────────────────────────────────────────────────────────
# BACKTRACKING (ADVANCED)
# ─────────────────────────────────────────────────────────────────────────────

# 31. N-QUEENS
# Place n queens on an n×n chessboard so no two queens attack each other.
# Return all distinct solutions as board configurations.
# Example: n=4 → 2 solutions


# 32. SUDOKU SOLVER
# Write a program to solve a Sudoku puzzle by filling in the empty cells.
# A solution must satisfy all the standard Sudoku rules.


# 33. EXPRESSION ADD OPERATORS
# Given a string of digits and a target, add '+', '-', or '*' between digits
# to reach the target. Return all valid expressions.
# Example: "123", target=6 → ["1+2+3","1*2*3"]


# ─────────────────────────────────────────────────────────────────────────────
# GRAPH ALGORITHMS
# ─────────────────────────────────────────────────────────────────────────────

# 34. NETWORK DELAY TIME (DIJKSTRA)
# Given a network of nodes and weighted edges, find the time it takes for all
# nodes to receive a signal sent from source k.
# Return -1 if not all nodes can be reached.


# 35. SWIM IN RISING WATER
# Given an n×n grid where grid[i][j] is the elevation, find the minimum time
# to travel from top-left to bottom-right.
# At time t, you can swim to any adjacent cell with elevation <= t.


# 36. MINIMUM COST TO CONNECT ALL POINTS (MST - PRIM'S)
# Given points on a 2D plane, find the minimum cost to connect all points.
# Cost = Manhattan distance. Use Prim's or Kruskal's algorithm.


# 37. RECONSTRUCT ITINERARY (HIERHOLZER'S ALGORITHM)
# Given airline tickets as [from, to] pairs, find the itinerary using
# all tickets starting from "JFK". Use the lexically smallest itinerary.
# Example: [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#          → ["JFK","MUC","LHR","SFO","SJC"]


# ─────────────────────────────────────────────────────────────────────────────
# MISCELLANEOUS
# ─────────────────────────────────────────────────────────────────────────────

# 38. LRU CACHE
# Design a data structure that follows the Least Recently Used (LRU) policy.
# Support get(key) and put(key, value) — both in O(1) time.


# 39. LFU CACHE
# Design a Least Frequently Used (LFU) cache.
# Support get(key) and put(key, value) — both in O(1) time.


# 40. MAXIMUM FREQUENCY STACK
# Design a stack where pop() returns the most frequent element.
# On ties, return the element closest to the top.
