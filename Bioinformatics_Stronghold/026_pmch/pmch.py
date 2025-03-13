#!python3
# Chendl 2025-03-13
## Comment here

from math import factorial

def pmch(rna:str):
	num_a = rna.count('A')
	num_c = rna.count('C')
	return factorial(num_a)*factorial(num_c)

if __name__ == "__main__":
	print(pmch('UCUUAUGUCAGUUACCACCCCUGCAUGACAUGAAGAUGCCCGGACAUUAGUCAGGUGGCGACAUUGGAUUAACCGAGUCG'))