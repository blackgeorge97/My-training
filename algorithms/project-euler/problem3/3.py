n = int(input("Please give an integer:"))
i = 2
while i ** 2 <= n:
    while n % i == 0:
        n = n / i
    i += 1        
print(n)
