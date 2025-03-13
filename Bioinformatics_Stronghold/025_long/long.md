# Genome Assembly as Shortest Superstring

Chendl 2025-03-13

## Problem

For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

## Solotion

The key is the sentence saying that ' there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length'. If not, this question can be a NP-hard question. Using a DP solotion will get a O(n^2*2^n), which is unacceptable.

### Python

``` python
def get_overlap(s1,s2):
    max_overlap_len_1 = 0
    for i in range(1,min(len(s1),len(s2))+1):
        if s1[-i:] == s2[:i]:
            max_overlap_len_1 = i
    max_overlap_len_2 = 0
    for i in range(1,min(len(s1),len(s2))+1):
        if s2[-i:] == s1[:i]:
            max_overlap_len_2 = i
    if max_overlap_len_1 >= max_overlap_len_2:
        return max_overlap_len_1, s1, s2
    else:
        return max_overlap_len_2, s2, s1

def find_super_string(reads:list):
    temp_reads = [read for read in reads]
    max_overlap_len = 0
    max_overlap_pair = ()
    while len(temp_reads)>1:
        max_overlap_len = 0
        max_overlap_pair = ()
        for i, read_i in enumerate(temp_reads[:-1]):
            for j in range(i+1, len(temp_reads)):
                read_j = temp_reads[j]
                overlap_len, lead_read, behind_read = get_overlap(read_i,read_j)
                if overlap_len > max_overlap_len:
                    max_overlap_len = overlap_len
                    max_overlap_pair = lead_read, behind_read
        temp_reads.remove(max_overlap_pair[0])
        temp_reads.remove(max_overlap_pair[1])
        new_read = max_overlap_pair[0] + max_overlap_pair[1][max_overlap_len:]
        temp_reads.append(new_read)
    return temp_reads


def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq:  
                    sequences.append(seq) 
                seq = "" 
            else:
                seq += line 
        if seq:
            sequences.append(seq)
    return sequences
```
