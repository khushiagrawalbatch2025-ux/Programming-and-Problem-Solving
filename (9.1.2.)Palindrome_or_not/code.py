inp = input()
length = len(inp)
flag = True
for st in range(length):
	if inp[st] != inp[length - 1 - st]:
		flag = False
if flag:
	print('Palindrome')
else:
	print("Not a Palindrome")
