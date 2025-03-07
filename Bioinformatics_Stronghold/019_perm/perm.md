# Enumerating Gene Orders

Chendl 2025-03-07

## Problem

Problem
A permutation of length n
 is an ordering of the positive integers {1,2,…,n}
. For example, π=(5,3,2,1,4)
 is a permutation of length 5
.

Given: A positive integer n≤7
.

Return: The total number of permutations of length n
, followed by a list of all such permutations (in any order).

## Solotion

### Python

``` python
def recu_perm(init_list:list):
	if len(init_list) == 1: return [init_list]
	ret_list = []
	for i in init_list:
		recu_list = init_list[:init_list.index(i)] + init_list[init_list.index(i)+1:]
		ret_list += [ [i] + posible_perm for posible_perm in recu_perm(recu_list) ]
	return ret_list

def perm(n:int):
	init_list = list(range(1,n+1))
	return recu_perm(init_list)
```
