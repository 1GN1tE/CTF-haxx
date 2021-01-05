import angr 
import claripy

filename = "angrme"
flag_length = 0x25
find_string = b":)"

proj = angr.Project(filename,load_options={"auto_load_libs": False},main_opts={"base_addr": 0})
flag = [claripy.BVS(f"c_{i}", 8) for i in range(flag_length)]
flag_ast = claripy.Concat(*flag)
state = proj.factory.entry_state(stdin=flag_ast)
for f in flag:
    state.solver.add(f >= 0x20)
    state.solver.add(f < 0x7f)

simgr = proj.factory.simulation_manager(state)
print("[+] Start exploring")
simgr.explore(find=lambda s: find_string in s.posix.dumps(1))

if len(simgr.found) > 0:
    found = simgr.found[0]
    valid_flag = found.solver.eval(flag_ast, cast_to=bytes)
    print(valid_flag.decode())
else:
    print("[-] Sed lyf")
