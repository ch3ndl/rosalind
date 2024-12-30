with open("0_data/rosalind_dna.txt", 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
	for i in "ACTG":
		print(string.count(i), end = ' ')
print()