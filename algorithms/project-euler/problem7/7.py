primes = [2]
candidate = 3
while len(primes) != 10001:
    is_prime = True
    for witness in primes:
        if witness * witness > candidate:
            break
        if candidate % witness == 0:
            is_prime = False           
            break
    if is_prime:
        primes.append(candidate)
    candidate += 1
print(primes[10000])
