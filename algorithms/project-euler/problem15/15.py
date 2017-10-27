LENGTH = 20

DP = []
for i in range(0, LENGTH + 1):
    DP.append([])
    for j in range(0, LENGTH + 1):
        if i ==0 or j == 0:
            DP[i].append(1)
            continue
        DP[i].append(DP[i - 1][j] + DP[i][j - 1])
print(DP[LENGTH][LENGTH])
