set_A = set(map(int, input("Set A: ").split()))
set_B = set(map(int,input("Set B: ").split()))
uni_set=set_A | set_B
print ("Union:",uni_set)
inter_set= set_A & set_B
print("Intersection:", inter_set)
diff_set=set_A - set_B
print("Difference:", diff_set)
