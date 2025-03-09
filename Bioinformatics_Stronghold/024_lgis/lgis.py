#!python3
# Chendl 2025-03-09
## Comment here

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


datafile = "Bioinformatics_Stronghold/024_lgis/rosalind_lgis.txt"
with open(datafile,'r') as handle:
	handle.readline()
	permutation = [ int(i) for i in handle.readline().strip().split(' ') ]

print(' '.join([
	str(i) for i in lgis(permutation)
]))

print(' '.join([
	str(i) for i in lgds(permutation)
]))


