# Finding a Shared Motif

Chendl 2025-03-05

## Problem

Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

### Given

A collection of k
 (k≤100
) DNA strings of length at most 1 kbp each in FASTA format.

### Return

A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

## Solotion

Give a simple bf algorithm here. Can be improved by using SA and LCP.
TODO: SA and LCP

### Python

``` python
def bf_lcsm(seq_list):
    shortest = min(seq_list, key=lambda x:len(x))
    shortest_len = len(shortest)
    seq_list_len = len(seq_list)
    for i in range(shortest_len):
        for j in range(i+1):
            test_seq = shortest[j:shortest_len-i+j]
            #print(test_seq)
            for k,seq in enumerate(seq_list):
                flag = test_seq in seq
                if not flag:break
                if k == seq_list_len-1:
                    return test_seq
```
