#!python3
# Chendl 2025-03-15
## Comment here

import re

def kmer(k)->list:
	bases = ['A','C','G','T']
	if k == 1: return bases
	return sorted([base + i for base in bases for i in kmer(k-1)])

def kmer_composition(dna:str,k:int):
	return [len(re.findall(f"(?=({seq}))",dna)) for seq in kmer(k)]

def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq:  
                    sequences.append(seq) 
                seq = "" 
            else:
                seq += line 
        if seq:
            sequences.append(seq)
    return sequences

if __name__ == "__main__":
	datafile = 'Bioinformatics_Stronghold/036_kmer/rosalind_kmer.txt'
	seq = read_fasta(datafile)[0]
	print(' '.join([str(i) for i in kmer_composition(seq,4)]))