A = 100
B = 100
ac = 0
bc = 0
f = 53
while True:
	a = int(input('A的输入：'))
	b = int(input('B的输入：'))
	if a == 0:
		ac += 1
		f -= 4
	if b == 0:
		bc += 10
		f -= 4
	if a + b > f:
		A -= a
		B -= b
		ac = 0
		bc = 0
		f -= 2
	else:
		if a > b:
			bc = 0
			ac += 1
			f += 3
			A += a * ac
		elif b > a:
			ac = 0
			bc += 1
			f += 3
			B += b * bc
	if A <= 0 or B <= 0:
		break
	print('A还有%d个金币，B还有%d个，炸的标准%d' % (A, B, f))
if A <= 0:
	print('A输了')
if B <= 0:
	print('B输了')
print('下次记得再来玩！')
