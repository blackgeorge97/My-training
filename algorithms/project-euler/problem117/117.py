LENGTH = 50

memo = [0, 1, 2, 4, 8]
for i in range(5, LENGTH + 1):
    memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3] + memo[i - 4])
print(memo[LENGTH])
