"""Design a class for a stream of integers supporting:

add(x) — add a number

get_max() — return maximum seen so far in O(1)

get_mean() — return mean in O(1)

get_mode() — return mode in O(1)

Assumptions I’ll use (typical interview / LeetCode-friendly):

Values are integers (can be negative).

get_mode() can return any mode if there are ties (or you can return the smallest mode; I’ll show how to do either).

If no elements exist yet, you can return None (or raise).
"""

from typing import *
from collections import defaultdict

class StatsTracker:
    def __init__(self):
        # TODO
        pass

    def add(self, x: int) -> None:
        # TODO
        pass

    def get_max(self) -> Optional[int]:
        # TODO
        pass

    def get_mean(self) -> Optional[float]:
        # TODO
        pass

    def get_mode(self) -> Optional[int]:
        # TODO
        pass


# -------------------------------
# Test for StatsTracker
# -------------------------------

from collections import defaultdict
from typing import Optional


class StatsTracker:
    def __init__(self):
        self.n = 0
        self.total_sum = 0
        self.current_max = None

        self.count = defaultdict(int)
        self.freq_to_vals = defaultdict(set)
        self.max_freq = 0

    def add(self, x: int) -> None:
        self.n += 1
        self.total_sum += x

        if self.current_max is None or x > self.current_max:
            self.current_max = x

        old_f = self.count[x]
        if old_f > 0:
            self.freq_to_vals[old_f].discard(x)

        new_f = old_f + 1
        self.count[x] = new_f
        self.freq_to_vals[new_f].add(x)

        if new_f > self.max_freq:
            self.max_freq = new_f

    def get_max(self) -> Optional[int]:
        return self.current_max

    def get_mean(self) -> Optional[float]:
        if self.n == 0:
            return None
        return self.total_sum / self.n

    def get_mode(self) -> Optional[int]:
        if self.n == 0:
            return None
        return next(iter(self.freq_to_vals[self.max_freq]))


def test_stats_tracker():
    tracker = StatsTracker()

    print("\nTesting StatsTracker\n")

    print("Initial state:")
    print("Max:", tracker.get_max())
    print("Mean:", tracker.get_mean())
    print("Mode:", tracker.get_mode())
    print()

    numbers = [5, 1, 5, 2, 2, 2, 3]

    for num in numbers:
        tracker.add(num)
        print(f"Added: {num}")
        print("  Max :", tracker.get_max())
        print("  Mean:", tracker.get_mean())
        print("  Mode:", tracker.get_mode())
        print()

    print("Final Checks:")
    print("Expected Max: 5")
    print("Expected Mean:", sum(numbers)/len(numbers))
    print("Expected Mode: 2")
    print()

if __name__ == "__main__":
    test_stats_tracker()
