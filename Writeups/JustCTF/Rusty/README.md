# Rusty
> Looking at rust code in disassembler/decompiler hurts, so... look somewhere else

## Solution
I was unable to solve this during the CTF. This `exe` has 2 code segments.
- A x86 part where there is Rust Code which is actually a rabbit hole.
- A DOS Stub part where the main challenge is located.
### Rust
Running the program in CMD we get -->
```
C:\Users\Arijeet\Downloads\CTF>rusty.exe
Give me the flag:
justCTF{test_flag}
lol. That's not even close.
```
We get the main function by checking the strings. It does some checks on our input string.
```c
if ((*(char *)local_c8 == 'j') &&
	(*(char *)((longlong)local_c8 + 1) == 'c') &&
	(*(char *)((longlong)local_c8 + 2) == 't') &&
	(*(char *)((longlong)local_c8 + 3) == 'f') &&
	(*(char *)((longlong)local_c8 + 4) == '{') &&
	(*(char *)((longlong)local_c8 + 0x36) == '}'))
	{
```
Then it checks every char of our flag on a looping algo
```c
      do {
        local_c8 = ppuVar6;
        if (uVar8 == 0x39) {
          local_70 = &PTR_s_Are_you_sure???_Try_somewhere_el_140020610;
          uStack104 = (undefined **)0x1;
          local_60 = 0;
          local_50 = "Are you sure??? Try somewhere else.\n";
          local_48 = 0;
          FUN_140008690((undefined4 *)&local_70);
          goto LAB_140002784;
        }
        uVar1 = uVar8 - 2;
        uVar2 = uVar8 - 1;
        uVar9 = uVar8 % 0x37;
        lVar3 = uVar8 * 2;
        uVar8 = uVar8 + 1;
      } while ((ushort)((ushort)*(byte *)((longlong)ppuVar5 + uVar9) +
                       (ushort)*(byte *)((longlong)ppuVar5 + uVar2 % 0x37) +
                       (ushort)*(byte *)((longlong)ppuVar5 + uVar1 % 0x37)) ==
               *(short *)((longlong)ppuVar6 + lVar3 + -0xe));
```

We get the values of the `ppuVar6` by using IDA debugging. Then we write a [solver script](https://github.com/1GN1tE/CTF-haxx/blob/master/Writeups/JustCTF/Rusty/solver.py) in `z3`.

We get this `jctf{this_IS_not_the_|>_you_are_looking_4_FAKEFLAG!!!!}` as the output.
Using this is the binary gives this.

```
C:\Users\Arijeet\Downloads\CTF>rusty.exe
Give me the flag:
jctf{this_IS_not_the_|>_you_are_looking_4_FAKEFLAG!!!!}
Are you sure??? Try somewhere else.
```
So this gives a fake flag.

### DOS
