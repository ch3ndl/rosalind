#!python3
# Chendl 2025-02-02
## Comment here
with open('006_hamm/rosalind_hamm.txt', 'r') as file:
    lines = file.readlines()

seq1 = lines[0].strip()
seq2 = lines[1].strip()

length = len(seq1)

mismatch_count = 0

for i in range(length):
    if seq1[i]!=seq2[i]:
        mismatch_count += 1 

print(mismatch_count)