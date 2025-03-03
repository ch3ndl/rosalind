#!python3
# Chendl 2025-03-03
## Comment here

from collections import namedtuple

Record = namedtuple("Record",["id","seq"])

datafile = "Bioinformatics_Stronghold/012_grph/rosalind_grph.txt"

with open(datafile, 'r') as handle:
	rec_list = []
	seq = ""
	id=""
	for line in handle:
		line = line.strip()
		if line.startswith(">"):
			if seq:
				rec_list.append(Record(id,seq))
			id = line[1:]
			seq = "" 
		else:
			seq += line 
	if seq:
		rec_list.append(Record(id,seq))

for i in range(len(rec_list)):
	rec_i = rec_list[i]
	for j in range(len(rec_list)):
		if i == j: continue
		rec_j = rec_list[j]
		if rec_i.seq[-3:] == rec_j.seq[:3]:
			print(rec_i.id, rec_j.id)