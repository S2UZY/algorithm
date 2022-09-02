str = input()
str = str.replace(',', '')
str = str.replace(';','')
str_list = str.split(' ')

for i in range(1,len(str_list)):
	temp = str_list[0]
	var = ''
	name = ''

	for j in list(str_list[i]):
		if j == '[':
			var += ']'
		elif j==']':
			var +='['
		elif j=='&' or j=='*':
			var += j
		else:
			name +=j
	var = var[::-1]
	print(temp+var+' '+name+';' )