LIMIT = 2000000
primes = [2]
for candidate in range(3, LIMIT):
    is_prime = True
    for witness in primes:
        if candidate % witness == 0:
           is_prime = False
           break
        if witness * witness > candidate:
           break
    if is_prime:
        primes.append(candidate)
sum_of_primes = sum(primes)
print(sum_of_primes)
