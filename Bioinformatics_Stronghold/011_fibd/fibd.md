# Mortal Fibonacci Rabbits

Chendl 2025-03-03

## Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2
 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

### Given

Positive integers n≤100
 and m≤20
.

### Return

The total number of pairs of rabbits that will remain after the n
-th month if all rabbits live for m
 months.

## Solotion

Use a list to stoage num of every live time of rabbit

### Python

``` python
def fibd(n,m):
	num_list = [0]*m
	num_list[0] = 1
	for i in range(n-1):
		num_list.insert(0, sum(
			num_list[1:]
		))
		num_list.pop()
	return sum(num_list)
```
