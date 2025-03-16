# Ordering Strings of Varying Length Lexicographically

Chendl 2025-03-16

## Problem

Say that we have strings s=s1s2⋯sm
 and t=t1t2⋯tn
 with m<n
. Consider the substring t′=t[1:m]
. We have two cases:

If s=t′
, then we set s<Lext
 because s
 is shorter than t
 (e.g., APPLE<APPLET
).
Otherwise, s≠t′
. We define s<Lext
 if s<Lext′
 and define s>Lext
 if s>Lext′
 (e.g., APPLET<LexARTS
 because APPL<LexARTS
).
Given: A permutation of at most 12 symbols defining an ordered alphabet A
 and a positive integer n
 (n≤4
).

Return: All strings of length at most n
 formed from A
, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

## Solotion

### Python

``` python
from functools import cmp_to_key
def compare_in_alphabet(alphabet):
	def _compare(string1,string2):
		for char1, char2 in zip(string1,string2):
			if alphabet.index(char1) > alphabet.index(char2):
				return 1
			if alphabet.index(char1) < alphabet.index(char2):
				return -1
			if alphabet.index(char1) == alphabet.index(char2):
				continue
		return 0
	return _compare

def lexv(alphabet:list, n:int)->list:
	if n == 1: return alphabet
	ret_list = []
	for previous_word in lexv(alphabet,n-1):
		for char in [""] + alphabet:
			if previous_word + char not in ret_list:ret_list.append(previous_word + char)
	return sorted(ret_list,key = cmp_to_key(compare_in_alphabet(alphabet)))
```
