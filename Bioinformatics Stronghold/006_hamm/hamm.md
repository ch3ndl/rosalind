# HAMM

## Problem

Given two strings s
 and t
 of equal length, the Hamming distance between s
 and t
, denoted dH(s,t)
, is the number of corresponding symbols that differ in s
 and t
. See Figure 2.

### Given

Two DNA strings s
 and t
 of equal length (not exceeding 1 kbp).

### Return

The Hamming distance dH(s,t)
.

## Solotion

### Shell

``` bash
seq1=$(sed -n '1p' 006_hamm/test.txt)
seq2=$(sed -n '2p' 006_hamm/test.txt)
len=${#seq1}
mismatch_count=0
for ((i=0; i<len; i++)); do
    char1=${seq1:i:1}
    char2=${seq2:i:1}
    if [ "$char1" != "$char2" ]; then
        mismatch_count=$((mismatch_count + 1))
    fi
done

echo "$mismatch_count"
```

### Python

``` python
with open('006_hamm/rosalind_hamm.txt', 'r') as file:
    lines = file.readlines()

seq1 = lines[0].strip()
seq2 = lines[1].strip()

length = len(seq1)

mismatch_count = 0

for i in range(length):
    if seq1[i]!=seq2[i]:
        mismatch_count += 1 

print(mismatch_count)
```
