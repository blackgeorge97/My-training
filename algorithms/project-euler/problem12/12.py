LIMIT = 500
triangle = 1
natural = 2
divisors = 1
while divisors < LIMIT:
    triangle += natural
    natural += 1
    divisors = 0
    for i in range(1, triangle):
        if triangle % i == 0:
            divisors += 2
        if i * i >= triangle:
            if i * i == triangle:
                divisors -= 1
            break
print(triangle)
