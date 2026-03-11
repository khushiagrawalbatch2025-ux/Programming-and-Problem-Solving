st = input()
new_st=""
for ch in st:
	if ch.isalnum() or ch.isspace():
		new_st = new_st + ch
print(new_st)
