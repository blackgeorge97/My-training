def lcm(a, b):
    from fractions import gcd
    return a * b / gcd(a, b)


n=1
for i in range(2, 21):
    n = lcm(n,i)
print(n)
