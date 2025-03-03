#!python3
# Chendl 2025-03-02
## Comment here
from collections import Counter
datafile = "Bioinformatics_Stronghold/010_cons/rosalind_cons.txt"

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

seq_list = read_fasta(datafile)


cons_seq = ""
count_dict_list = []
for i in range(len(seq_list[0])):
	count_i = Counter([seq[i] for seq in seq_list])
	max_char = max(count_i, key=count_i.get) # can use mostcommon instead
	cons_seq += max_char
	count_dict_list.append(count_i)


print(cons_seq)

for count_i in count_dict_list:
	for char in "ACGT":
		if not count_i.get(char):count_i[char]=0

for char in "ACGT":
	num_text = ' '.join(
		[str(count_i.get(char)) for count_i in count_dict_list]
	)
	print(f"{char}: {num_text}")