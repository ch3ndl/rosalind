# Creating a Distance Matrix

Chendl 2025-03-17

## Problem

For two strings s1
 and s2
 of equal length, the p-distance between them, denoted dp(s1,s2)
, is the proportion of corresponding symbols that differ between s1
 and s2
.

For a general distance function d
 on n
 taxa s1,s2,…,sn
 (taxa are often represented by genetic strings), we may encode the distances between pairs of taxa via a distance matrix D
 in which Di,j=d(si,sj)
.

Given: A collection of n
 (n≤10
) DNA strings s1,…,sn
 of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D
 corresponding to the p-distance dp
 on the given strings. As always, note that your answer is allowed an absolute error of 0.001.

## Solotion

### Python

``` python
def pdst(strings:list)->list:
	ret = [[0]*len(strings) for i in range(len(strings))]
	for i,string_i in enumerate(strings):
		for j,string_j in enumerate(strings):
			ret[i][j] = p_distant(string_i,string_j)
	return ret

def p_distant(s1,s2):
	assert len(s1) == len(s2)
	return sum([1 for c1,c2 in zip(s1,s2) if c1!=c2])/len(s1)
```
