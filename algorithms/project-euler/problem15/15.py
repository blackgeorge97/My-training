LENGTH = 20
def path_explorer(i, j, path_collector):
    if i < LENGTH and j < LENGTH:
        count = 0
        if path_collector[i + 1][j] == 0:
            path_collector[i + 1][j] = path_explorer(i + 1, j, path_collector)
            path_collector[j][i + 1] = path_collector[i + 1][j]
            count += path_collector[i + 1][j]
        else:
            count += path_collector[i + 1][j]
        if path_collector[i][j + 1] == 0:
            path_collector[i][j + 1] = path_explorer(i, j + 1, path_collector)
            path_collector[j + 1][i] = path_collector[j + 1][i]
            count += path_collector[i][j + 1]
        else:
            count += path_collector[i][j + 1]
        return count
    else:
        return 1


path_collector = []
for i in range(0, LENGTH + 1):
    line = []
    for j in range(0, LENGTH + 1):
        line.append(0)
    path_collector.append(line)
print(path_explorer(0, 0, path_collector))
