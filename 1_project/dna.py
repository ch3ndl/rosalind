datafile = "0_data/rosalind_dna.txt"
with open(datafile, 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
for i in "ACTG":
	print(string.count(i), end = ' ')
print()