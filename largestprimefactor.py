
def findPrimeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5)+1, 2): # checking odd numbers as after dividing by two n must be odd. goes up to square root as any number greater than that will have a factor less than the square root that has already been found
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2: 
        factors.append(n)

    return factors

def largestPrimeFactor(n):
    return max(findPrimeFactors(n))

print(largestPrimeFactor(600851475143))