array = list(map(int, input().split()))
for i in range(len(array)):
    for j in range(i+1, len(array)):
        sum_i = sum(array[k] for k in range(0, i+1))
        sum_j = sum(array[k] for k in range(i+1, j+1))
        sum_n = sum(array[k] for k in range(j+1, len(array)))

        if ((sum_i % 3) == (sum_j % 3) == (sum_n % 3)) or ((sum_i % 3) != (sum_j % 3) != (sum_n % 3)):
            print(i, j)
            break
        else:
            pass
print(0,0)
        