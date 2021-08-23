import test
import time

ans = True
i = 0
stop = 1
while ans:
    i += 1
    stop *= 10
    t = time.time()
    ans = test.test(0, stop, 5)
    td = time.time() - t
    if td >= 60:
        print(False, td, i, 'TLE')
        break
    print(ans, td, i)
print('=' * 20, 'THE END OF TEST', '=' * 20)
