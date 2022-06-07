import sieve as s

def prime_fac(n):
    prime_factors_powers = []
    for i in s.sieve(n + 1):
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n = n // i
            prime_factors_powers.append((i, power))
    return prime_factors_powers

def phi(prime_factors_powers):
    totient = 1
    for i in range(len(prime_factors_powers)):
        totient *= (prime_factors_powers[i][0] ** (prime_factors_powers[i][1] - 1)) * (prime_factors_powers[i][0] - 1)
    return totient








