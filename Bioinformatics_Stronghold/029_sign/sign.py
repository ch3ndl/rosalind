#!python3
# Chendl 2025-03-14
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

def get_possible_sign(permutation:list)->list:
	if len(permutation) == 1 : return [ [permutation[0]],[-permutation[0]] ]
	return [ [permutation[0]] + possible_sign for possible_sign in get_possible_sign(permutation[1:])] + [ [-permutation[0]] + possible_sign for possible_sign in get_possible_sign(permutation[1:])]

def signed_permutation(n:int)->list:
	permutations = perm(n)
	ret = []
	for permutation in permutations:
		ret += get_possible_sign(permutation)
	return ret

if __name__ == "__main__":
	given_num = 3
	all_signd_perm = signed_permutation(given_num)
	print(len(all_signd_perm))
	print('\n'.join(
		[' '.join([str(i) for i in permutation]) for permutation in all_signd_perm]
	))