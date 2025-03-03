# Consensus and Profile

Chendl 2025-03-02

## Problem

Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n
 matrix has m
 rows and n
 columns. Given a matrix A
, we write Ai,j
 to indicate the value found at the intersection of row i
 and column j
.

Say that we have a collection of DNA strings, all having the same length n
. Their profile matrix is a 4×n
 matrix P
 in which P1,j
 represents the number of times that 'A' occurs in the j
th position of one of the strings, P2,j
 represents the number of times that C occurs in the j
th position, and so on (see below).

A consensus string c
 is a string of length n
 formed from our collection by taking the most common symbol at each position; the j
th symbol of c
 therefore corresponds to the symbol having the maximum value in the j
-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

### Given

A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

### Return

A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

## Solotion

### Python

``` python
from collections import Counter
datafile = "Bioinformatics_Stronghold/010_cons/rosalind_cons.txt"

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

seq_list = read_fasta(datafile)


cons_seq = ""
count_dict_list = []
for i in range(len(seq_list[0])):
	count_i = Counter([seq[i] for seq in seq_list])
	max_char = max(count_i, key=count_i.get) # can use mostcommon instead
	cons_seq += max_char
	count_dict_list.append(count_i)


print(cons_seq)

for count_i in count_dict_list:
	for char in "ACGT":
		if not count_i.get(char):count_i[char]=0

for char in "ACGT":
	num_text = ' '.join(
		[str(count_i.get(char)) for count_i in count_dict_list]
	)
	print(f"{char}: {num_text}")
```
