#!python3
# Chendl 2025-03-18
## Comment here
from math import comb

def aspc(n,m):
	return sum(
		[comb(n,k) for k in range(m,n+1)]
	) % 1000000


if __name__ == "__main__":
	print(aspc(1884,627))