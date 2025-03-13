#!python3
# Chendl 2025-03-14
## Comment here

from functools import reduce
from math import log10

def get_prob(dna:str, gc_content:float)->float:
	base_prob = {
		'A':(1-gc_content)/2,
		'C':gc_content/2,
		'G':gc_content/2,
		'T':(1-gc_content)/2,
	}
	return log10(reduce(lambda x,y:x*y, 
						  [base_prob[base] for base  in dna]
						  ))


if __name__ == "__main__":
	dna = 'ACGATACAA'
	datafile = 'Bioinformatics_Stronghold/028_prob/rosalind_prob.txt'
	with open(datafile, 'r') as handle:
		dna = handle.readline().strip()
		gc_contents = [float(i) for i in handle.readline().strip().split(' ')]
	print(' '.join(
		[f'{get_prob(dna, gc_content):.3f}' for gc_content in gc_contents]
	))