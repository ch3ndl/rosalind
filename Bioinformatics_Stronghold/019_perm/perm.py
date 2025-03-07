#!python3
# Chendl 2025-03-07
## Comment here

def recu_perm(init_list:list):
	if len(init_list) == 1: return [init_list]
	ret_list = []
	for i in init_list:
		recu_list = init_list[:init_list.index(i)] + init_list[init_list.index(i)+1:]
		ret_list += [ [i] + posible_perm for posible_perm in recu_perm(recu_list) ]
	return ret_list

def perm(n:int):
	init_list = list(range(1,n+1))
	return recu_perm(init_list)

permutation_list = perm(6)
print(len(permutation_list))
print('\n'.join([' '.join([str(i) for i in permutation]) for permutation in permutation_list]))
