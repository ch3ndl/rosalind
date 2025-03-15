# k-Mer Composition

Chendl 2025-03-15

## Problem

For a fixed positive integer k
, order all possible k-mers taken from an underlying alphabet lexicographically.

Then the k-mer composition of a string s
 can be represented by an array A
 for which A[m]
 denotes the number of times that the m
th k-mer (with respect to the lexicographic order) appears in s
.

Given: A DNA string s
 in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s
.

## Solotion

### Python

``` python
def kmer(k)->list:
	bases = ['A','C','G','T']
	if k == 1: return bases
	return sorted([base + i for base in bases for i in kmer(k-1)])

def kmer_composition(dna:str,k:int):
	return [len(re.findall(f"(?=({seq}))",dna)) for seq in kmer(k)]
```
