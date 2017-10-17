def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return a * b / gcd(a, b)



#main code
n=11
for i in range(12, 21):
    n = lcm(n,i)
print(n)
 

