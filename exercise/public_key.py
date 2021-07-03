from random import randint
from time import time
from math import gcd                    # lcm


def is_prime(num):
    if num % 2 == 0:
        return False
    for i in  range(3, num-1):
        if num % i == 0:
            return False
    return True

def lcm(a, b):
    return a * b // gcd(a, b)



class RandomNumberGenerator():
    def __init__(self):
        pass

    def generate(self, bits):
        return randint(2 ** (bits-1), 2 ** bits)


class PublicKeyGenerator():
    def __init__(self):
        self.gen = RandomNumberGenerator()

    def make_key_pair(self):
        p = 888
        q = 888
        while not is_prime(p):
            p = gen.generate(64)
        while not is_prime(q):
            q = gen.generate(64)
        N = p * q
        L = lcm(p - 1, q - 1)
        E = gcd(E, L)
        D = None
        for n in range(1, L):
            if (L * n + 1) % E == 0:
                D = (L * n + 1) // E
                break
        if D is None:
            raise RuntimeError('D not found')
        return ((E, N), (D, N))
