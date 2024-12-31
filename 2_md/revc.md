# REVC

## Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
.

### Sample Dataset

AAAACCCGGT

### Sample Output

ACCGGGTTTT

## Solotion

### Shell

``` bash
cat 0_data/rosalind_revc.txt | sed 's/./&\n/g' | awk '/A/{printf "T"}/T/{printf "A"}/G/{printf "C"}/C/{printf "G"}END{print}' | rev
```

### Python

``` python
datafile = "0_data/rosalind_revc.txt"
with open(datafile, 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
complementary_dict = {
	"A":"T",
	"T":"A",
	"G":"C",
	"C":"G",
}
string = ''.join([
	complementary_dict[i] for i in string[::-1]
])
print(string)
```
