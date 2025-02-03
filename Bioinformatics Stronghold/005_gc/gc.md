# GC

## Problem

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

### Given

At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

### Return

The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

## Solotion

### Python

``` python
datafile = "005_gc/rosalind_gc.txt"

def caculate_GC(seq: str):
	return ( seq.count('G') + seq.count('C') ) / len(seq)

seq_dict = {}
with open(datafile, 'r') as handle:
	for line in handle.readlines():
		line = line.strip()
		if line[0]=='>':
			current_label = line[1:]
			seq_dict[current_label] = ""
		else:
			seq_dict[current_label] += line

max_seq_label = max(seq_dict, key=lambda x: caculate_GC(seq_dict[x]))
print(max_seq_label)
print(f"{caculate_GC(seq_dict[max_seq_label])*100:.6f}")
```
