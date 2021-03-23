from z3 import *
flag_len = 40
flag_chars = [BitVec(f'{i}', 8) for i in range(flag_len)] # Length of flag
s = Solver()

for i in range(flag_len):
	s.add(flag_chars[i]>44)
	s.add(flag_chars[i]<126)


# Other consraints and equations

sat = s.check()
if str(sat) == "sat":
	model = s.model()
	flag = ''.join([chr(int(str(model[flag_chars[i]]))) for i in range(len(model))])
	print(flag)
else:
	print(sat)
