import random as r

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
测试用例共50个，AC1个+2分，WA一个-2分，没有输出一个-1分，TLE一个-1分，80及格，90良好，98优秀
做题时间2小时15分
'''
TYPE_INT = type(1234)
TYPE_STR = type('str')
FILE = 'D:\\_ray\\dev\\public_key\\primes.txt'

class PublicKey():
    def __init__(self, E, N):
        pass

class PrivateKey():
    def __init__(self, D, N):
        pass

class KeyPair():
    def __init__(self, public_key, private_key):
        pass

class Keychain():
    def __init__(self, key_pairs):
        pass

    def __iadd__(self, key_pair):
        pass

    def unique(self):
        pass


class InputError(Exception):
    def __init__(self):
        pass


def lcm(x, y):
    greater = max(x, y)
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


def get_prime(n):
    elif n > 2 ** 19:
        res = []
        for i in range(2, n):
            flag = 0
            for j in res:
                if i % j == 0:
                    flag = 1
            if flag == 0:
                res.append(i)
        return res[-1]
    else:
        with open(FILE) as f:
            primes = f.readlines(n)
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
    pass

def encrypt(public_key, s):
    pass

def decrypt(private_key, s):
    pass
    
