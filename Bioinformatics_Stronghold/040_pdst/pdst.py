#!python3
# Chendl 2025-03-17
## Comment here

def pdst(strings:list)->list:
	ret = [[0]*len(strings) for i in range(len(strings))]
	for i,string_i in enumerate(strings):
		for j,string_j in enumerate(strings):
			ret[i][j] = p_distant(string_i,string_j)
	return ret

def p_distant(s1,s2):
	assert len(s1) == len(s2)
	return sum([1 for c1,c2 in zip(s1,s2) if c1!=c2])/len(s1)

def read_fasta(file_path):
	sequences = []
	with open(file_path, 'r') as file:
		seq = ""
		for line in file:
			line = line.strip()
			if line.startswith(">"):
				if seq:  
					sequences.append(seq) 
				seq = "" 
			else:
				seq += line 
		if seq:
			sequences.append(seq)
	return sequences

if __name__ == "__main__":
	datafile = "Bioinformatics_Stronghold/040_pdst/rosalind_pdst.txt"
	seqs = read_fasta(datafile)
	for row in pdst(seqs):
		print(" ".join([f"{i:.3f}" for i in row]))