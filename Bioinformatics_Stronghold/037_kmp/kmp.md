# 

Chendl 2025-03-15

## Problem

A prefix of a length n
 string s
 is a substring s[1:j]
; a suffix of s
 is a substring s[k:n]
.

The failure array of s
 is an array P
 of length n
 for which P[k]
 is the length of the longest substring s[j:k]
 that is equal to some prefix s[1:k−j+1]
, where j
 cannot equal 1
 (otherwise, P[k]
 would always equal k
). By convention, P[1]=0
.

Given: A DNA string s
 (of length at most 100 kbp) in FASTA format.

Return: The failure array of s
.

## Solotion

### Python

``` python
def fail_arr(string):
	arr = [0] * len(string)
	i = 1
	length = 0
	while i < len(string):
		if string[i] == string[length]:
			length += 1
			arr[i] = length
			i += 1
		else:
			if length != 0:
				length = arr[length - 1]
			else:
				arr[i] = 0
				i += 1
	return arr
```
