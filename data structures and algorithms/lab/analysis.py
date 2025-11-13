
# THIS IS O(2^n)
def knapsack_bitwise(W, val, wt, n):
    max_val = 0
    # Iterate through all possible subsets (2^n)
    for i in range(1 << n):
        current_weight = 0
        current_val = 0
        for j in range(n):
            # Check if the j-th bit is set in i
            if (i >> j) & 1:
                current_weight += wt[j]
                current_val += val[j]

        # If the current subset's weight is within capacity and its value is greater
        if current_weight <= W and current_val > max_val:
            max_val = current_val
    return max_val
