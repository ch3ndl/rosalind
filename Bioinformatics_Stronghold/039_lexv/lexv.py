#!python3
# Chendl 2025-03-16
## Comment here

from functools import cmp_to_key


def compare_in_alphabet(alphabet):
	def _compare(string1,string2):
		for char1, char2 in zip(string1,string2):
			if alphabet.index(char1) > alphabet.index(char2):
				return 1
			if alphabet.index(char1) < alphabet.index(char2):
				return -1
			if alphabet.index(char1) == alphabet.index(char2):
				continue
		return 0
	return _compare


def lexv(alphabet:list, n:int)->list:
	if n == 1: return alphabet
	ret_list = []
	for previous_word in lexv(alphabet,n-1):
		for char in [""] + alphabet:
			if previous_word + char not in ret_list:ret_list.append(previous_word + char)
	return sorted(ret_list,key = cmp_to_key(compare_in_alphabet(alphabet)))

if __name__ == "__main__":
	datafile = "Bioinformatics_Stronghold/039_lexv/rosalind_lexv.txt"
	with open(datafile, 'r') as handle:
		alphabet = handle.readline().strip().split()
		n = int(handle.readline().strip())
	with open("Bioinformatics_Stronghold/039_lexv/res.txt", 'w') as handle:
		handle.write('\n'.join(lexv(alphabet,n)))