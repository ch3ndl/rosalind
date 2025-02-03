datafile = "002_rna/rosalind_rna.txt"
with open(datafile, 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
print(string.replace('T','U'))