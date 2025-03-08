# Locating Restriction Sites

Chendl 2025-03-08

## Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

## Solotion

Another Solotion is breaking the dna into different length. Then check every fragment.

### Python

``` python
def revc(dna:str)->str:
	complementary_dict = {
	"A":"T",
	"T":"A",
	"G":"C",
	"C":"G",
}
	return ''.join([
	complementary_dict[i] for i in dna[::-1]
])


def revp(dna:str):
	pos_len = []
	def revp_len(pos:int)->list:
		verified_len = []
		for potential_len in range(4,13,2):
			half_len = int(potential_len/2)
			start = pos + 1 - half_len
			end = pos + half_len + 1
			if start < 0 or end > len(dna): break
			print(start,end)
			print(dna[start:end])
			print(revc(dna[start:end]))
			if dna[start:end] == revc(dna[start:end]):
				verified_len.append(potential_len)
		return verified_len
	
	for middle in range(1,len(dna)-2):
		length_list = revp_len(middle)
		new_lenght_list = [ [int(middle+1-(length/2))+1, length] for length in length_list ]
		pos_len += new_lenght_list
		# if length:
		# 	pos_len.append([int(middle+1-(length/2))+1, length])
	return pos_len
```
