import random
from math import gcd as gcd

size = 100

def is_prime (n):
    factors = []
    for i in range(2,n):
        if (n % i) == 0:
            factors.append(i)
    if len(factors) == 1:
        return True

def get_prime_factors(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst

def coprime(n, lst):
    coprimes = []
    for i in lst:
        divisor = gcd(n, i)
        if ( divisor == 1):
            coprimes.append(i)
    print(coprime)
    return coprimes

def get_primes():
    p = 0
    q = 0
    while not (is_prime(p) and is_prime(q) and p != q):
        p = random.randint(17, 100)
        q = random.randint(17, 100)
    return p, q

def get_n (p, q):
    n = p * q
    return n

def get_phi(p , q):
    phi = ((p - 1)) * ((q - 1))
    return phi

def get_e (n , phi):
    n_factors = get_prime_factors(n)
    phi_factors = get_prime_factors(phi)
    n_factors.extend(phi_factors)
    possibilities = []
    for i in range (2, (phi + 1)):
        lst = coprime(i, n_factors)
        possibilities.extend(lst)
    real_pos = list(set(possibilities))
    e = random.choice(real_pos)
    return e

def get_d (e, phi):
    lst = []
    for n in range(3, phi):
        if ((e * n) % phi) == 1:
            lst.append(n)
    d = random.choice(lst)
    return d

def generate_keys():
    p, q = get_primes()
    n = get_n(p, q)
    phi = get_phi(p, q)
    e = get_e(n, phi)
    d = get_d(e, phi)
    return (e,n), (d,n)

print(str(generate_keys()))



        
    
    
    

    
