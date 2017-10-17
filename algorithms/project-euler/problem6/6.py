sum = 0
sum_sqrs = 0
for i in range(1, 101):
    sum += i
    sum_sqrs += i ** 2
sqr_sum = sum ** 2
print(sqr_sum - sum_sqrs)

