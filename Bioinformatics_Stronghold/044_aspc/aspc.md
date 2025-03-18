# Introduction to Alternative Splicing

Chendl 2025-03-18

## Problem

In “Counting Subsets”, we saw that the total number of subsets of a set S
 containing n
 elements is equal to 2n
.

However, if we intend to count the total number of subsets of S
 having a fixed size k
, then we use the combination statistic C(n,k)
, also written (nk)
.

Given: Positive integers n
 and m
 with 0≤m≤n≤2000
.

Return: The sum of combinations C(n,k)
 for all k
 satisfying m≤k≤n
, modulo 1,000,000. In shorthand, ∑nk=m(nk)
.

## Solotion

### Python

``` python
def aspc(n,m):
	return sum(
		[comb(n,k) for k in range(m,n+1)]
	) % 1000000
```
