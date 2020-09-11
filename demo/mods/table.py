# Command line arguments

import sys

if len(sys.argv) < 2:  # No parameter passed
    print("Usage : python table.py  number [length]")
    exit(1)

length = 10    # Default length
if len(sys.argv) > 2:
    length = int(sys.argv[2])

num = int(sys.argv[1])

for n in range(1, length + 1):
    print(f"{num:4} * {n:2} = {n * num:6}")
