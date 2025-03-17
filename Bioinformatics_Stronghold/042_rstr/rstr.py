#!python3
# Chendl 2025-03-18
## Comment here

from functools import reduce

def rstr(n,x,dna):
	prob_base = {
		'G':x/2,
		'C':x/2,
		'A':(1-x)/2,
		'T':(1-x)/2,
	}
	return 1-(1-reduce(lambda x,y:x*y,[prob_base[char] for char in dna]))**n

if __name__ == "__main__":
	print(f"{rstr(87836 ,0.401243,'TCTTTGAA'):.3f}")