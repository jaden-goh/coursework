array = list(map(int, input().split()))
n = len(array)

# prefix sums so we don't recompute sums in the loops
pre = [0]*(n+1)
for idx, v in enumerate(array, 1):
    pre[idx] = pre[idx-1] + v

found = False
# ensure all three parts are non-empty: i <= n-3, j <= n-2
for i in range(0, n-2):          # i corresponds to l-1
    for j in range(i+1, n-1):    # j corresponds to r-1
        sum_i = pre[i+1]                      # a[0..i]
        sum_j = pre[j+1] - pre[i+1]          # a[i+1..j]
        sum_n = pre[n] - pre[j+1]            # a[j+1..n-1]

        s1, s2, s3 = sum_i % 3, sum_j % 3, sum_n % 3

        # all equal OR all different
        if len({s1, s2, s3}) in (1, 3):
            print(i+1, j+1)   # print 1-based l, r
            found = True
            break
    if found:
        break

if not found:
    print(0, 0)
