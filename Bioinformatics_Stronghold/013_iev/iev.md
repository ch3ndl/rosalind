# Calculating Expected Offspring

Chendl 2025-03-03

## Problem

For a random variable X
 taking integer values between 1 and n
, the expected value of X
 is E(X)=∑nk=1k×Pr(X=k)
. The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

As a motivating example, let X
 be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5
.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X
 is a uniform random variable with minimum possible value a
 and maximum possible value b
, then E(X)=a+b2
. You may also wish to verify that for the dice example, if Y
 is the random variable associated with the outcome of a second die roll, then E(X+Y)=7
.

### Given

Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

### Return

The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

## Solotion

### Python

``` python
def iev(a,b,c,d,e,f):
	return 2*a + 2*b + 2*c + 1.5*d + e

print(iev(16292,17800,19654,18763,16335,17302))
```
