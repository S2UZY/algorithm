fst = []
est = []

for _ in range(int(input())):
	key = input()
	fst.clear()
	est.clear()

	for i in key:
		if i == '<':
			if fst:
				est.append(fst.pop())
		elif i == '>':
			if est:
				fst.append(est.pop())
		elif i=='-':
			if fst:
				fst.pop()
		else:
			fst.append(i)

	fst.extend(est)
	print(''.join(fst))

