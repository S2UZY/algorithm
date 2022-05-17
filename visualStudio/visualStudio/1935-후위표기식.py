#import sys

#input = sys.stdin.readline
n = int(input())
clac = input()
data = []
st = []

for i in range(n):
	data.append(int(input()))

for i in clac:
	if 65 <= ord(i) <= 90:
		st.append(data[ord(i)-65])
	else:
		a =  st.pop()
		b =  st.pop()
		if i =='*':
			st.append(a*b)
		elif i =='+':
			st.append(a+b)
		elif i =='/':
			st.append(b/a)
		elif i =='-':
			st.append(b-a)

print("{:.2f}".format(st.pop()))