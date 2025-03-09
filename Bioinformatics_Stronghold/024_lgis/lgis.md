# Longest Increasing Subsequence

Chendl 2025-03-09

## Problem

A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000
 followed by a permutation π
 of length n
.

Return: A longest increasing subsequence of π
, followed by a longest decreasing subsequence of π
.

## Solotion

DP. Use two array, one for record longest length for current index, one for previous position.

### Shell

### Python

``` python
def lgis(permutation:list)->list:
	perm_len = len(permutation)
	longest_inc_len = [1] * perm_len
	prev_pos = [-1] * perm_len
	for i in range(1,perm_len):
		for prev in range(i):
			if permutation[i] > permutation[prev]:
				if longest_inc_len[prev]+1 > longest_inc_len[i]:
					prev_pos[i] = prev
					longest_inc_len[i] = longest_inc_len[prev]+1

	longest_index = longest_inc_len.index(max(longest_inc_len))
	ret = []
	while longest_index != -1:
		ret = [permutation[longest_index]] + ret
		longest_index = prev_pos[longest_index]
	return ret

def lgds(permutation:list)->list:
	perm_len = len(permutation)
	longest_inc_len = [1] * perm_len
	prev_pos = [-1] * perm_len
	for i in range(1,perm_len):
		for prev in range(i):
			if permutation[i] < permutation[prev]: # the only difference
				if longest_inc_len[prev]+1 > longest_inc_len[i]:
					prev_pos[i] = prev
					longest_inc_len[i] = longest_inc_len[prev]+1

	longest_index = longest_inc_len.index(max(longest_inc_len))
	ret = []
	while longest_index != -1:
		ret = [permutation[longest_index]] + ret
		longest_index = prev_pos[longest_index]
	return ret
```
