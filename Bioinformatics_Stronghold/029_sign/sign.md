# Enumerating Oriented Gene Orderings

Chendl 2025-03-14

## Problem

A signed permutation of length n
 is some ordering of the positive integers {1,2,…,n}
 in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4)
 is a signed permutation of length 5
.

Given: A positive integer n≤6
.

Return: The total number of signed permutations of length n
, followed by a list of all such permutations (you may list the signed permutations in any order).

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

def get_possible_sign(permutation:list)->list:
	if len(permutation) == 1 : return [ [permutation[0]],[-permutation[0]] ]
	return [ [permutation[0]] + possible_sign for possible_sign in get_possible_sign(permutation[1:])] + [ [-permutation[0]] + possible_sign for possible_sign in get_possible_sign(permutation[1:])]

def signed_permutation(n:int)->list:
	permutations = perm(n)
	ret = []
	for permutation in permutations:
		ret += get_possible_sign(permutation)
	return ret
```
