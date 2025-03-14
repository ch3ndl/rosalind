# Transitions and Transversions

Chendl 2025-03-14

## Problem

For DNA strings s1
 and s2
 having the same length, their transition/transversion ratio R(s1,s2)
 is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1
 and s2
 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2)
.

## Solotion

### Python

``` python
def transition_transversion_ratio(s1,s2):
	transition = 0
	transversion = 0
	for base1,base2 in zip(s1,s2):
		if base1 == base2:continue
		if all([base in "AG" for base in (base1,base2)]) or all([base in "CT" for base in (base1,base2)]):
			transition += 1
		else:
			transversion +=1
	return transition/transversion
```
