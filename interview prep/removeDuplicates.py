"""
Given a string s, return a new string with duplicate characters removed, keeping only the first occurrence of each character and preserving the original order.

Example:

s = "banana" → "ban"

s = "cbacdcbc" → "cbad" (this is not the “smallest lexicographic” version; it’s “first occurrence order”)

If you meant a different classic variant (like Remove All Adjacent Duplicates or Remove Duplicate Letters to get lexicographically smallest), tell me which and I’ll swap the solution.
"""

from typing import *

class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Remove duplicate characters, keep first occurrence, preserve order.
        """
        # TODO
        pass


# -------------------------------
# Test for Remove Duplicates
# -------------------------------

class Solution:
    def removeDuplicates(self, s: str) -> str:
        seen = set()
        out = []
        for c in s:
            if c not in seen:
                seen.add(c)
                out.append(c)
        return "".join(out)


def test_remove_duplicates():
    sol = Solution()

    test_cases = [
        ("banana", "ban"),
        ("aaaa", "a"),
        ("abcabc", "abc"),
        ("", ""),
        ("a", "a"),
        ("cbacdcbc", "cbad"),  # first occurrence preserved
    ]

    print("Testing Remove Duplicates\n")

    for i, (input_str, expected) in enumerate(test_cases):
        result = sol.removeDuplicates(input_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: {status}")
        print(f"  Input:    {input_str}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()

if __name__ == "__main__":
    test_remove_duplicates()
