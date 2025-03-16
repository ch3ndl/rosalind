# Finding a Shared Spliced Motif

Chendl 2025-03-16

## Problem

A string u
 is a common subsequence of strings s
 and t
 if the symbols of u
 appear in order as a subsequence of both s
 and t
. For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA".

Analogously to the definition of longest common substring, u
 is a longest common subsequence of s
 and t
 if there does not exist a longer common subsequence of the two strings. Continuing our above example, "ACCTTG" is a longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".

Given: Two DNA strings s
 and t
 (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s
 and t
. (If more than one solution exists, you may return any one.)

## Solotion

DP problem. The key is that when char_i == chat_j, we can know that the longest length is 1 + longest_lenght(i-1,j-1)

### Python

``` python
def lcsq(string_1:str, string_2:str)->str:
	longest_lenght_table = [[0] * (len(string_2)+1) for i in  range(len(string_1)+1)]
	preceded_pos_table = [[[]] * (len(string_2)+1) for i in  range(len(string_1)+1)]
	for i,char_i in enumerate(string_1):
		for j,char_j in enumerate(string_2):
			if char_i == char_j:
				longest_lenght_table[i+1][j+1] = longest_lenght_table[i][j]+1
				preceded_pos_table[i+1][j+1] = [i,j]
			else:
				if longest_lenght_table[i][j+1] > longest_lenght_table[i+1][j]:
					longest_lenght_table[i+1][j+1] = longest_lenght_table[i][j+1]
					preceded_pos_table[i+1][j+1] = [i,j+1]
				else:
					longest_lenght_table[i+1][j+1] = longest_lenght_table[i+1][j]
					preceded_pos_table[i+1][j+1] = [i+1,j]

	pos = preceded_pos_table[-1][-1]
	ret_string = ""
	for i in longest_lenght_table:
		print(i)
	while pos[0]!=0 and pos[1]!=0:
		next_pos = preceded_pos_table[pos[0]][pos[1]]
		if pos[0]-1 == next_pos[0] and pos[1]-1 == next_pos[1]:
			print(pos)
			ret_string = string_1[pos[0]-1] + ret_string
		pos = next_pos
	return ret_string
```
