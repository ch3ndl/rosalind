#!python3
# Chendl 2025-03-04
## Comment here

from time import process_time
import cProfile

datafile = "Bioinformatics_Stronghold/014_lcsm/rosalind_lcsm.txt"

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

def bf_lcsm(seq_list):
    shortest = min(seq_list, key=lambda x:len(x))
    shortest_len = len(shortest)
    seq_list_len = len(seq_list)
    for i in range(shortest_len):
        for j in range(i+1):
            test_seq = shortest[j:shortest_len-i+j]
            #print(test_seq)
            for k,seq in enumerate(seq_list):
                flag = test_seq in seq
                if not flag:break
                if k == seq_list_len-1:
                    return test_seq
print(bf_lcsm(seq_list))