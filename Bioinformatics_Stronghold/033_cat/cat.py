#!python3
# Chendl 2025-03-14
## Comment here


def _is_pair(x,y):
	pair_base = ('AUCG','UAGC')
	return pair_base[0].index(x) == pair_base[1].index(y)

def cat(rna:str)->int:
	if not hasattr(cat, "known_result"):
		cat.known_result = {}
	if rna in cat.known_result.keys(): return cat.known_result.get(rna)
	if len(rna) == 0: return 1
	if len(rna) == 2:
		if _is_pair(rna[0],rna[1]):
			cat.known_result[rna] = 1
			return 1
		else:
			return 0
	possible_division_point = []
	for i in range(1,len(rna),2):
		if _is_pair(rna[0],rna[i]):
			possible_division_point.append(i)
		else:
			pass
	if not possible_division_point:
		return 0
	result = sum([
		cat(rna[1:division_point])*cat(rna[division_point+1:]) for division_point in possible_division_point
	])
	cat.known_result[rna] = result
	return result
	


if __name__ == "__main__":
	print(cat('CAGAUCGCAAAUUAAUGUUAACUAUAACCGGCGUUUUAAUGCAUAUUUUAGCACGCGGUUUACGCGAAGAUAUCCAUGCGUAUACUAGUGCGUCGACGCGGCCUAGGCGCCACUAUGCAGCUAUAUUAAGCGGGAUGGUACCUGCAAUCCGCUCUGGGCCCAUAGAGCAUAUUAUAUUAAGCUAGUAUGUAAUUACACCGCAUGCGGGAAAUUUGCAUCCGGCCGAUCCAUACGUAUACGGCCGUCGAUCCGGAUUGGCCUAACAUGCGCGCCGAUGAUGAUGGCCAAUUAUAUUA')%1000000)