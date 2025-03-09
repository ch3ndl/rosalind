#!python3
# Chendl 2025-03-08
## Comment here

datafile = "Bioinformatics_Stronghold/023_lexf/test.txt"

with open(datafile, 'r') as handle:
	symbol_list = handle.readline().strip().split(' ')
	str_len =int( handle.readline().strip() )

def lexf(symbol_list:list, str_len:int)->list:
	if str_len == 1: return symbol_list
	ret_str_list = []
	for exsited_str in lexf(symbol_list, str_len-1):
		for symbol in symbol_list:
			ret_str_list.append(exsited_str+symbol)
	return ret_str_list
# def lexf(symbol_list:list, str_len:int)->list:
# 	symbol_list.sort()
# 	iter_str_list = [""]
# 	ret_str_list = [""]
# 	for exsit_str in iter_str_list:
# 		iter
# 	for i in range(str_len):
# 		ret_list = []

print("\n".join(lexf(symbol_list,str_len)))