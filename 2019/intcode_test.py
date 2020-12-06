"""Check if the IntcodeComputer still works correctly after changing it.
Works by catching all the print outputs into a string and comparing it with the
expected outputs. This is easier than reworking everything to use a proper
unittest library.
"""


EXPECTED = """3101844
8478
0
0
0
0
0
0
0
0
0
9006673
3629692
21000
61379886
2457252183
70634
2428
 ███    ██ █    ████ ███  █  █  ██  █  █   
 █  █    █ █    █    █  █ █  █ █  █ █  █   
 █  █    █ █    ███  ███  █  █ █    █  █   
 ███     █ █    █    █  █ █  █ █    █  █   
 █ █  █  █ █    █    █  █ █  █ █  █ █  █   
 █  █  ██  ████ █    ███   ██   ██   ██    
268
13989
330
352
""".splitlines()


# Source: https://stackoverflow.com/a/40984270
import io
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
    import day_02
    import day_05
    import day_07
    import day_09
    import day_11
    import day_13
    import day_15
out = f.getvalue().splitlines()


ok = True
for i, line in enumerate(out):
    exp = EXPECTED[i]
    try:
        assert exp == line
    except AssertionError:
        print(f"{line=}")
        print(f"{exp=}\n")
        ok = False
if ok:
    print("Ok")
else:
    print("Found some errors.")
