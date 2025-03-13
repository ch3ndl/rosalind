#!python3
# Chendl 2025-03-13
## Comment here

from functools import reduce

def pper(x,y):
    def mult(x,y):
        return x*y
    return reduce(mult,[i for i in range(x-y+1,x+1)]) % 1000000

if __name__ == "__main__":
	print(pper(88,9))