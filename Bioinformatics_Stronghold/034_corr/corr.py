#!python3
# Chendl 2025-03-15
## Comment here

def hamming_distant(string_1, string_2)->int:
	return sum([
		c1 != c2 for c1,c2 in zip(string_1,string_2)
	])

def revc(seq):
	complementary_dict = {
	"A":"T",
	"T":"A",
	"G":"C",
	"C":"G",
}
	return ''.join([
	complementary_dict[i] for i in seq[::-1]
])

def min_hamming_distant(seq_1,seq_2)->int:
	hamming_distant_1 = hamming_distant(seq_1,seq_2)
	hamming_distant_2 = hamming_distant(seq_1,revc(seq_2))
	return min(hamming_distant_1,hamming_distant_2)

def corr(reads:list)->list:
	similar_reads_list = []
	for read in reads:
		found_simimlar = False
		for similar_reads in similar_reads_list:
			if read in similar_reads or revc(read) in similar_reads:
				similar_reads.append(read)
				found_simimlar = True
				break
		if not found_simimlar:
			similar_reads_list.append([read])
	remain_reads = [reads[0] for reads in similar_reads_list if len(reads)==1]
	similar_reads_list = [reads for reads in similar_reads_list if len(reads)>1]
	corr_list = []
	for read in remain_reads:
		for similar_reads in similar_reads_list:
			similar_count = sum([
				min_hamming_distant(read, similar_read)==1 for similar_read in similar_reads
			])
			if similar_count < 2: continue
			for similar_read in similar_reads:
				if hamming_distant(read,similar_read) == 1:
					corr_list.append([read, similar_read])
					break
				if hamming_distant(read,revc(similar_read)) == 1:
					corr_list.append([read, revc(similar_read)])
					break
	return corr_list

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
	datafile = 'Bioinformatics_Stronghold/034_corr/rosalind_corr.txt'
	reads = read_fasta(datafile)
		
	print('\n'.join(
		['->'.join(pair) for pair in corr(reads)]
		))