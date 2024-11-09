from math import sqrt, ceil

def CalcRating(name, r, rank):
	print("CalcRating By Ray Hu <r@pythoner.work>")
	P = []
	n = len(r)
	for i in range(n):
		P.append([])
		for j in range(n):
			if i == j:
				P[i].append(0)
				continue
			P[i].append(1 / (1 + pow(10, (r[j] - r[i]) / 400)))
			print(f"{name[i]} v({P[i][j]})s {name[j]}")
	m = []
	d = []
	sigD = 0
	for i in range(n):
		sum = 1
		for j in range(n):
			if i == j:
				continue
			sum += P[j][i]
		m.append(sqrt(sum * rank[i]))
		left = 1
		right = 8000
		while right - left > 1e-3:
			mid = (left + right) / 2
			sd = 1
			for j in range(n):
				if i == j:
					continue
				sd += 1 / (1 + pow(10, (mid - r[j]) / 400))
			if sd < rank[i]:
				left = mid
			else:
				right = mid
		d.append(ceil((left - r[i]) / 2))
		sigD += d[i]
		print(f"{name[i]}'s seed is {sum}, performance is {left}")
	for i in range(n):
		print(f"{name[i]}'s delta is {d[i] + (-1-sigD)/n}")
	