# Introduction to Random Strings

Chendl 2025-03-14

## Problem

An array is a structure containing an ordered collection of objects (numbers, strings, other arrays, etc.). We let A[k]
 denote the k
-th value in array A
. You may like to think of an array as simply a matrix having only one row.

A random string is constructed so that the probability of choosing each subsequent symbol is based on a fixed underlying symbol frequency.

GC-content offers us natural symbol frequencies for constructing random DNA strings. If the GC-content is x
, then we set the symbol frequencies of C and G equal to x2
 and the symbol frequencies of A and T equal to 1−x2
. For example, if the GC-content is 40%, then as we construct the string, the next symbol is 'G'/'C' with probability 0.2, and the next symbol is 'A'/'T' with probability 0.3.

In practice, many probabilities wind up being very small. In order to work with small probabilities, we may plug them into a function that "blows them up" for the sake of comparison. Specifically, the common logarithm of x
 (defined for x>0
 and denoted log10(x)
) is the exponent to which we must raise 10 to obtain x
.

See Figure 1 for a graph of the common logarithm function y=log10(x)
. In this graph, we can see that the logarithm of x
-values between 0 and 1 always winds up mapping to y
-values between −∞
 and 0: x
-values near 0 have logarithms close to −∞
, and x
-values close to 1 have logarithms close to 0
. Thus, we will select the common logarithm as our function to "blow up" small probability values for comparison.

Given: A DNA string s
 of length at most 100 bp and an array A
 containing at most 20 numbers between 0 and 1.

Return: An array B
 having the same length as A
 in which B[k]
 represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k]
 will match s
 exactly.

## Solotion

### Python

``` python
def get_prob(dna:str, gc_content:float)->float:
	base_prob = {
		'A':(1-gc_content)/2,
		'C':gc_content/2,
		'G':gc_content/2,
		'T':(1-gc_content)/2,
	}
	return log10(reduce(lambda x,y:x*y, 
						  [base_prob[base] for base  in dna]
						  ))
```
