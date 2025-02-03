# DNA

## Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

### Sample Dataset

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

### Sample Output

20 12 17 21

## Solotion

### Shell

``` bash
cat 001_dna/rosalind_dna.txt |\
sed 's/./&\n/g' |\
# add '\n' after every char
sort |\
uniq -c |\
grep "[ACTG]" |\
awk '{print $1}' |\
xargs
```

### Python

``` python
datafile = "001_dna/rosalind_dna.txt"
with open(datafile, 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
for i in "ACTG":
	print(string.count(i), end = ' ')
print()
```
