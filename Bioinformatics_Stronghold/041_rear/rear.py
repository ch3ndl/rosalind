#!python3
# Chendl 2025-03-17
## Comment here
from functools import reduce

def all_rev(permutation):
	ret = set()
	for interval_len in range(2,len(permutation)+1):
		for start in range(0,len(permutation)-interval_len+1):
			ret.add(
				tuple(permutation[:start] + permutation[start:start+interval_len][::-1] + permutation[start+interval_len:])
			)
	return ret

def rear(target_permutation, ori_permutation)->int:
	t_perms = set()
	t_perms.add(tuple(target_permutation))
	o_perms = set()
	o_perms.add(tuple(ori_permutation))
	rev_distant = 0
	while not bool(t_perms & o_perms):
		new_t_perms = set(tuple(j) for i in t_perms for j in all_rev(i))
		new_o_perms = set(tuple(j) for i in o_perms for j in all_rev(i))
		if t_perms & new_o_perms:
			return rev_distant + 1
		if o_perms & new_t_perms:
			return rev_distant + 1
		t_perms = new_t_perms
		o_perms = new_o_perms
		rev_distant += 2
	return rev_distant

if __name__ == "__main__":
	# a = set()
	# a.add(tuple([3,10,8,2,5,4,7,1,6,9]))
	# b = set()
	# b.add(tuple([5,2,3,1,7,4,10,8,6,9]))
	# print(reversal_distance(a,b))
	datafile = 'Bioinformatics_Stronghold/041_rear/rosalind_rear.txt'
	with open(datafile, 'r') as handle:
		pairs = [
			[[int(i) for i in line.split()] for line in part.split('\n')] for part in handle.read().split('\n\n')
		]
	for pair in pairs:
		print(rear(*pair), end= ' ')
	print(pairs)
	print(rear([1,2,3,4,5,6,7,8,9,10],[3,1,5,2,7,4,9,6,10,8]))