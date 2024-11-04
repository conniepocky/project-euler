# primes below 50 million is 3,037,204

# so need to 3 million primes 3 times, for square cube and 4th power

# ancient greek algorithm sieve of eratosthenes to find primes

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  
    for start in range(2, int(limit**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]

sums = set() # set to avoid duplicates

max = 50000000

primes = sieve_of_eratosthenes(7072) # 7072 is the square root of 50 million

for sq in primes:
    for cu in primes:
        if sq**2 + cu**3 >= max:
            break
        for fo in primes:
            sum = sq**2 + cu**3 + fo**4
            if sum < max:
                sums.add(sum)

print(len(sums))
