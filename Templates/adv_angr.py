 #!/usr/bin/env python3

import angr 
import claripy

if __name__ == '__main__':
	print("[+] Solver Started")

	binary = "./" #Binary
	flag_length = # Flag_length
	print("[+] flag Length : 0x%02x" % flag_length)
	print("[+] Starting Project :", binary)
	
	proj = angr.Project(binary)
	flag = [claripy.BVS(f"c_{i}", 8) for i in range(flag_length)]
	flag_ast = claripy.Concat(*flag)

	state = proj.factory.entry_state(stdin=flag_ast)
	for f in flag:
		state.solver.add(f >= 0x20)
		state.solver.add(f < 0x7f)

	simgr = proj.factory.simulation_manager(state)
	print("[+] Exploring...")

	good = 0x400000+ # Good Address
	bad = 0x400000+ # Bad Address

	simgr.explore(find=good, avoid=bad)

	if len(simgr.found) > 0:
		print("[+] Solution Found")
		found = simgr.found[0]
		valid_flag = found.solver.eval(flag_ast, cast_to=bytes)
		print("[+] Flag :", valid_flag.decode())
	else:
		print("[-] Sed Lyf")
