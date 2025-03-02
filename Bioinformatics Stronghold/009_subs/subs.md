# Finding a Motif in DNA

Chendl 2025-02-03

## Problem

Given two strings s
 and t
, t
 is a substring of s
 if t
 is contained as a contiguous collection of symbols in s
 (as a result, t
 must be no longer than s
).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
 of s
 is denoted by s[i]
.

A substring of s
 can be represented as s[j:k]
, where j
 and k
 represent the starting and ending positions of the substring in s
; for example, if s
 = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]
 = "UGCU".

The location of a substring s[j:k]
 is its beginning position j
; note that t
 will have multiple locations in s
 if it occurs more than once as a substring of s
 (see the Sample below).

### Given

Two DNA strings s
 and t
 (each of length at most 1 kbp).

### Return

All locations of t
 as a substring of s
.

## Solotion

It seems like a kmp problem. Compute the lps of the pattern first. When the searching missmatch at i, we can know that the pattern[:i] is matched. So we can push the pattern forward by the lps. Take an example we missmatch at the last place in ATAT. We know that ATA is matched. So we can push the pattern forward to where the next check is the second char in ATAT. Because we know that the header of matched is A and the tail of the matched is also A. So we can just skip this check and check from the second char.

### Python

``` python

def pythonic_search(s:str,t:str):
    return [i+1 for i in range(len(s)) if s.startswith(t, i)]

def brute_force(s:str,t:str):
	len_s = len(s)
	len_t = len(t)
	ret = []
	for i in range(len_s-len_t+1):
		if s[i:i+len_t] == t:
			ret.append(i+1)
	return ret

def kmp_search(s: str, t: str):
    # Preprocess the pattern (t) to create the partial match table
    def compute_lps_array(pattern: str):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    len_s = len(s)
    len_t = len(t)
    lps = compute_lps_array(t)
    i = 0  # index for s
    j = 0  # index for t
    ret = []

    while i < len_s:
        if t[j] == s[i]:
            i += 1
            j += 1

            if j == len_t:
                ret.append(i - j + 1)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print(lps)
    print(t)
    return ret

# Example usage:
# brute_force(string_s, string_t)
# print(pythonic_search(string_s, string_t))
print(kmp_search(string_s, string_t))

brute_force(string_s,string_t)
print(pythonic_search(string_s,string_t))
print(kmp_search(string_s,string_t))
```
