#!python3
# Chendl 2025-02-02
## Comment here
datafile = "005_gc/rosalind_gc.txt"

def caculate_GC(seq: str):
	return ( seq.count('G') + seq.count('C') ) / len(seq)

seq_dict = {}
with open(datafile, 'r') as handle:
	for line in handle.readlines():
		line = line.strip()
		if line[0]=='>':
			current_label = line[1:]
			seq_dict[current_label] = ""
		else:
			seq_dict[current_label] += line

max_seq_label = max(seq_dict, key=lambda x: caculate_GC(seq_dict[x]))
print(max_seq_label)
print(f"{caculate_GC(seq_dict[max_seq_label])*100:.6f}")