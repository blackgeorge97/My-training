LIMIT = 1000000
max = 0
length_cand = []
for candidate in range(2, LIMIT):
    count = 0
    n = candidate
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        if n < candidate and n > 2:
            count += length_cand[int(n) - 2]
            break
    length_cand.append(count)
    if max < count:
        max = count
        number_max = candidate
print(number_max)
