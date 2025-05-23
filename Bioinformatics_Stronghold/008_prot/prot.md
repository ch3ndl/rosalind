# Translating RNA into Protein

Chendl 2025-02-02

## Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

### Given

An RNA string s
 corresponding to a strand of mRNA (of length at most 10 kbp).

### Return

The protein string encoded by s
.

## Solotion

### Python

``` python
codon_text = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""
tmp_list = codon_text.replace('\n', ' ').split()
codon_dict = { key:value for key,value in
 zip(tmp_list[::2],tmp_list[1::2])
}

datafile = "008_prot/rosalind_prot.txt"
with open(datafile, 'r') as handle:
	seq = ''.join([line.strip().upper() for line in handle.readlines()])
assert(len(seq)%3 == 0)
for i in range(int(len(seq)/3)):
	codon = seq[3*i:3*i+3]
	aa = codon_dict[codon]
	if aa == "Stop":
		print()
		break
	print(aa,end='')
```
