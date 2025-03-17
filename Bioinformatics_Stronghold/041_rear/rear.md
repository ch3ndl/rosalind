# Reversal Distance

Chendl 2025-03-18

## Problem

A reversal of a permutation creates a new permutation by inverting some interval of the permutation; (5,2,3,1,4)
, (5,3,4,1,2)
, and (4,1,2,3,5)
 are all reversals of (5,3,2,1,4)
. The reversal distance between two permutations π
 and σ
, written drev(π,σ)
, is the minimum number of reversals required to transform π
 into σ
 (this assumes that π
 and σ
 have the same length).

Given: A collection of at most 5 pairs of permutations, all of which have length 10.

Return: The reversal distance between each permutation pair.

## Solotion

Reverse permutation both direction. If simply reverse one direction, the computation time will be unacceptable.

### Python

``` python
def all_rev(permutation):
	ret = set()
	for interval_len in range(2,len(permutation)+1):
		for start in range(0,len(permutation)-interval_len+1):
			ret.add(
				tuple(permutation[:start] + permutation[start:start+interval_len][::-1] + permutation[start+interval_len:])
			)
	return ret

def rear(target_permutation, ori_permutation)->int:
	t_perms = set()
	t_perms.add(tuple(target_permutation))
	o_perms = set()
	o_perms.add(tuple(ori_permutation))
	rev_distant = 0
	while not bool(t_perms & o_perms):
		new_t_perms = set(tuple(j) for i in t_perms for j in all_rev(i))
		new_o_perms = set(tuple(j) for i in o_perms for j in all_rev(i))
		if t_perms & new_o_perms:
			return rev_distant + 1
		if o_perms & new_t_perms:
			return rev_distant + 1
		t_perms = new_t_perms
		o_perms = new_o_perms
		rev_distant += 2
	return rev_distant
```
