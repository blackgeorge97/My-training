LIMIT = 500
triangle = 1
natural = 2
divisors = 1
while divisors < LIMIT:
    triangle += natural
    natural += 1
    divisors = 1
    current_triangle = triangle
    i = 2
    while current_triangle != 1:
        power = 0
        while current_triangle % i == 0:
            power += 1
            current_triangle = current_triangle / i
        divisors *= (power + 1)
        i += 1
print(triangle)
