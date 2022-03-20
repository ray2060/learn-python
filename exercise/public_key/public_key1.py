import random as r
import time as t

'''
目标：
实现公钥密码 （算法已了解）
给出最大公倍数、最小公约数、最大小于等于n的质数三个函数
generate_key_pair(size)函数用来生成密钥对，输入类型不对抛出TypeError，size小于等于2抛出InputError，返回KeyPair，正常输入size <= 32，限时1200000ms
encrypt(public_key, s)函数用来加密，输入类型不正确抛出TypeError，密钥太短输出RunimeError，限时800000ms
decrypt(private_key, s)函数用来解密，输入类型不对抛出TypeError，密钥太短抛出RuntimeError，限时800000ms
PublicKey和PrivateKey类用于存储钥匙
KeyPair类存储密钥对
Keychain类存储多个KeyPair，如果key_pairs的类型不是List[KeyPair]抛出TypeError，长度不超过300
Keychain += KeyPair 增加密钥对，限时200ms
Keychain.unique()排重，限时1000ms
测试用例共50个， 可以正常使用+2分， 不可以使用-2分，超时-1分，30及格，50良好，80优秀
做题时间35分钟，到20分钟时为了UP的视力休息10分钟
'''
TYPE_INT = type(1234)
TYPE_STR = type('str')
TYPE_LIST = type([])
FILE = 'D:\\_ray\\dev\\public_key\\primes.txt'

class PublicKey():
    def __init__(self, E, N):
        self.E = E
        self.N = N

class PrivateKey():
    def __init__(self, D, N):
        self.D = D
        self.N = N

class KeyPair():
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

TYPE_PUBLIC_KEY = type(PublicKey(1, 2))
TYPE_PRIVATE_KEY = type(PrivateKey(1, 2))
TYPE_KEY_PAIR = type(KeyPair(PublicKey(1, 2), PrivateKey(1, 2)))
class Keychain():
    def __init__(self, key_pairs):
        flag = False
        if type(key_pairs) != TYPE_LIST:
            flag = True
        for key_pair in key_pairs:
            if type(key_pair) != TYPE_KEY_PAIR:
                flag = True
        if flag:
            raise TypeError
        self.key_pairs = key_pairs

    def __iadd__(self, key_pair):
        self.key_pairs.append(key_pair)

    def unique(self):
        self.key_pairs = list(set(self.key_pairs))


class InputError(Exception):
    def __init__(self):
        pass


def lcm(x, y):
    greater = max(x, y)
    if x == 0 or y == 0:
        return 1
    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


def get_prime(n):
    if n > 2 ** 19:
        n = int(t.time())
        res = []
        for i in range(2, n):
            flag = 0
            for j in res:
                if i % j == 0:
                    flag = 1
                if n - int(t.time()) > 120000:
                    raise RuntimeError
            if flag == 0:
                res.append(i)
        return res[-1]
    else:
        with open(FILE) as f:
            primes = f.readlines(n)
            for i in range(len(primes)):
                primes[i] = int(i)
            ans = []
            for i in primes:
                if primes[i] <= n:
                    ans.append(primes[i])
        return ans[-1]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_key_pair(size):
    if size <= 2:
        raise InputError
    if type(size) != TYPE_INT:
        raise TypeError
    p = get_prime(r.randrange(2 ** (size - 2), 2 ** size - 1))
    q = get_prime(r.randrange(2 ** (size - 2), 2 ** size - 1))
    N = p * q
    L = lcm(p - 1, q - 1)
    E = 1  # 0
    while gcd(E, L) != 1:
        E += 1
    D = 1  # 0
    while E * D % L != 1:
        D += 1
    return KeyPair(PublicKey(E, N), PrivateKey(D, N))

def encrypt(public_key, s):
    if type(public_key) != TYPE_PUBLIC_KEY:
        raise TypeError
    b = '0b0'
    if type(s) == TYPE_INT:
        b = bin(s)
    elif type(s) == TYPE_STR:
        for c in s:
            b += str(bin(ord(c))) [2:]
    else:
        raise TypeError
    d = int(b, base=2)
    n = pow(d, public_key.E)
    if n < public_key.N:
        raise RuntimeError
    return n % public_key.N

def decrypt(private_key, d):
    if type(d) != TYPE_INT:
        raise TypeError
    elif type(private_key) != TYPE_PRIVATE_KEY:
        raise TypeError
    m = pow(d, private_key.D)
    if m < private_key.N:
        raise RuntimeError
    n = m % private_key.N
    b = bin(n)
    s = ''
    for i in range(2, len(b), 8):
        s += chr(int('0b' + b[i:i+8], base=2))
    return s
    
