import public_key1 as p
import time as t

score = 0
# test cases
# 1 - 30
for i in range(3, 33):
    n = int(float(t.time()) * 1000)
    try:
        tmp = p.generate_key_pair(i)
    except RuntimeError:
        score -= 1
    else:
        if int(float(t.time()) * 1000) - n > 120000:
            score -= 1
        else:
            score += 2
    print(score)
# 31
try:
    tmp = p.generate_key_pair(2)
except InputError:
    score += 2
else:
    score -= 2
print(score)
# 32 - 35
lst = ['hello', 'bye-bye']
for s in lst:
    flag1, flag2 = 0, 0
    n = int(float(t.time()) * 1000)
    tmp2 = p.encrypt(tmp.public_key, s)
    if n - int(float(t.time()) * 1000) > 80000:
        score -= 1
        flag1 += 1
    print(score)
    n = int(float(t.time()) * 1000)
    tmp3 = p.decrypt(tmp.private_key, tmp2)
    if n - int(float(t.time()) * 1000) > 80000:
        score -= 1
        flag2 += 1
    if tmp3 != s:
        score -= 4 - flag1 - flag2
    else:
        score += 2
    print(score)
# 36
try:
    trash = p.generate_key_pair('3')
except TypeError:
    score += 2
else:
    score -= 2
print(score)
# 37
try:
    trash = p.encrypt(tmp.public_key, 1234654323456928428748754479579407777777045004945003381737)
except TypeError:
    score += 2
else:
    score -= 2
print(score)
# 38
try:
    trash = p.encrypt(tmp.public_key, 'jfdklqjsadfxneoifnjcrsjkfch')
except RuntimeError:
    score += 2
else:
    score -= 2
print(score)
# 39
try:
    trash = p.decrypt(tmp.private_key, 'fahuicfgncuxdnkxf')
except TypeError:
    score += 2
else:
    score -= 2
print(score)
# 40
try:
    trash = p.decrypt(tmp.private_key, 540175203485274059475802785760850475802780475487502784907)
except TypeError:
    score += 2
else:
    score -= 2
print(score)
# 41
try:
    kc = Keychain([KeyPair(PublicKey(1, 2), PrivateKey(1, 2))])
except:
    score -= 2
else:
    score += 2
print(score)
# 42
try:
    kc = Keychain([1, 2, 3])
except:
    score += 2
else:
    score -= 2
print(score)
# 43
n = int(float(t.time()) * 1000)
kc = Keychain([KeyPair(PublicKey(1, 2), PrivateKey(1, 2)), KeyPair(PublicKey(1, 2), PrivateKey(1, 2))])
kc.unique()
if n - int(float(t.time()) * 1000) > 1000:
    score -= 1
if kc == [KeyPair(PublicKey(1, 2), PrivateKey(1, 2))]:
    score += 2
else:
    score -= 2
print(score)
# 44
n = int(float(t.time()) * 1000)
kc = Keychain([KeyPair(PublicKey(1, 2), PrivateKey(1, 2))])
kc += KeyPair(PublicKey(1, 2), PrivateKey(1, 2))
if n - int(float(t.time()) * 1000) > 200:
    score -= 1
if kc == [[KeyPair(PublicKey(1, 2), PrivateKey(1, 2)), KeyPair(PublicKey(1, 2), PrivateKey(1, 2))]]:
    score += 2
else:
    score -= 2
print(score)
# 45 - 50
if score >= 85:
    score += 12
elif score >= 65:
    score += 4
else:
    score += 2
# get score
print(score)
