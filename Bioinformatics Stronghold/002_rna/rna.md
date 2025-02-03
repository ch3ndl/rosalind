# RNA

## Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u
.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t
.

### Sample Dataset

GATGGAACTTGACTACGTAAATT

### Sample Output

GAUGGAACUUGACUACGUAAAUU

## Solotion

### Shell

``` bash
sed 's/T/U/g' 2_rna/rosalind_rna.txt 
```

### Python

``` python
datafile = "2_rna/rosalind_rna.txt"
with open(datafile, 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
print(string.replace('T','U'))
```
