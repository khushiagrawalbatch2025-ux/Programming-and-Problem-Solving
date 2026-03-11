def reverse_string(st):
	new_st = ""
	length=len(st)
	for ch in range(length-1, -1,-1):
		new_st = new_st + st[ch]
	return new_st

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
