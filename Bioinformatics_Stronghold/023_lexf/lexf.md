# Enumerating k-mers Lexicographically

Chendl 2025-03-09

## Problem

Assume that an alphabet A
 has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak)
, where a1<a2<⋯<ak
. For instance, the English alphabet is organized as (A,B,…,Z)
.

Given two strings s
 and t
 having the same length n
, we say that s
 precedes t
 in the lexicographic order (and write s<Lext
) if the first symbol s[j]
 that doesn't match t[j]
 satisfies sj<tj
 in A
.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
 (n≤10
).

Return: All strings of length n
 that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

## Solotion

### Python

``` python
def lexf(symbol_list:list, str_len:int)->list:
	if str_len == 1: return symbol_list
	ret_str_list = []
	for exsited_str in lexf(symbol_list, str_len-1):
		for symbol in symbol_list:
			ret_str_list.append(exsited_str+symbol)
	return ret_str_list
```
