from typing import List, Tuple
import unittest

# ============================================================
# 1) Profitable Project Pairs
# Count pairs (i, j), i < j such that profit[i] + profit[j] > target
# Typical solution: sort + two pointers or binary search per i.
# ============================================================

class Solution:
    def profitableProjectPairs(self, profits: List[int], target: int) -> int:
        """
        Return the number of pairs (i, j), i < j, with profits[i] + profits[j] > target.

        Expected: O(n log n) using sorting + binary search (or two pointers).
        """
        # TODO: implement
        raise NotImplementedError


# ============================================================
# 2) Maximum Swaps
# Given two lists A, B and an integer k (max swaps),
# swap elements between A and B at most k times to maximize the
# number of UNIQUE elements in A.
#
# NOTE: This is a "set/greedy" style question. Define your exact rules:
# - A and B can contain duplicates.
# - One swap exchanges one element from A with one from B.
# - Goal: maximize |set(A)| after <= k swaps.
# ============================================================

class Solution2:
    def maximumUniqueAfterSwaps(self, A: List[int], B: List[int], k: int) -> int:
        """
        Return max possible number of unique elements in A after at most k swaps with B.
        """
        # TODO: implement
        raise NotImplementedError


# ============================================================
# 3) Binary Circuit
# Given a binary string s, compute cost to move all '1's to the right.
#
# Common interpretation (like "minimum adjacent swaps"):
# cost = number of inversions '1' before '0' or '0' before '1' depending on direction.
# If moving 1s to the RIGHT via adjacent swaps, cost = count of pairs (i<j) where s[i]='1' and s[j]='0'
# (because each such pair must cross once).
# ============================================================

class Solution3:
    def binaryCircuitCost(self, s: str) -> int:
        """
        Return cost to move all '1's to the right (minimum adjacent swaps),
        i.e., count of ('1' before '0') inversions.
        """
        # TODO: implement
        raise NotImplementedError


# ============================================================
# TESTS
# Fill in your implementations, then run this file:
#   python your_file.py
# ============================================================

class TestProblems(unittest.TestCase):

    # ---------- Problem 1 tests ----------
    def test_profitable_pairs_basic(self):
        sol = Solution()
        profits = [3, 1, 2, 5]
        target = 4
        # pairs with sum > 4:
        # (3,2)=5, (3,5)=8, (1,5)=6, (2,5)=7 -> 4
        self.assertEqual(sol.profitableProjectPairs(profits, target), 4)

    def test_profitable_pairs_duplicates(self):
        sol = Solution()
        profits = [2, 2, 2]
        target = 3
        # all pairs sum to 4 -> C(3,2)=3
        self.assertEqual(sol.profitableProjectPairs(profits, target), 3)

    def test_profitable_pairs_none(self):
        sol = Solution()
        profits = [1, 1, 1]
        target = 5
        self.assertEqual(sol.profitableProjectPairs(profits, target), 0)

    # ---------- Problem 2 tests ----------
    def test_max_unique_after_swaps_simple(self):
        sol = Solution2()
        A = [1, 1, 2]
        B = [2, 3, 3]
        k = 1
        # Best: swap one of the duplicate '1' in A with '3' from B => A could become [1,3,2] => uniques=3
        self.assertEqual(sol.maximumUniqueAfterSwaps(A, B, k), 3)

    def test_max_unique_after_swaps_zero_k(self):
        sol = Solution2()
        A = [1, 2, 2, 2]
        B = [3, 4]
        k = 0
        self.assertEqual(sol.maximumUniqueAfterSwaps(A, B, k), 2)

    def test_max_unique_after_swaps_limited(self):
        sol = Solution2()
        A = [1, 1, 1]
        B = [2, 3, 4]
        k = 2
        # With 2 swaps, can introduce at most 2 distinct new values into A: e.g., [2,3,1] uniques=3
        self.assertEqual(sol.maximumUniqueAfterSwaps(A, B, k), 3)

    # ---------- Problem 3 tests ----------
    def test_binary_circuit_cost_basic(self):
        sol = Solution3()
        s = "1010"
        # '1' before '0' pairs:
        # positions: 1s at 0,2; 0s at 1,3
        # (0,1), (0,3), (2,3) => 3
        self.assertEqual(sol.binaryCircuitCost(s), 3)

    def test_binary_circuit_cost_sorted(self):
        sol = Solution3()
        self.assertEqual(sol.binaryCircuitCost("00111"), 0)  # already 1s to right
        self.assertEqual(sol.binaryCircuitCost("11100"), 6)  # 3 ones * 2 zeros = 6 inversions

    def test_binary_circuit_cost_edge(self):
        sol = Solution3()
        self.assertEqual(sol.binaryCircuitCost(""), 0)
        self.assertEqual(sol.binaryCircuitCost("0"), 0)
        self.assertEqual(sol.binaryCircuitCost("1"), 0)


if __name__ == "__main__":
    unittest.main()
