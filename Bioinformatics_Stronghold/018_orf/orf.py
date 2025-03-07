#!python3
# Chendl 2025-03-07
## Comment here

def revc(dna_seq:str)->str:
    complementary_dict = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G",
}
    return ''.join([
    complementary_dict[i] for i in dna_seq[::-1]
])

def orf(dna_seq:str)->list:
    codontab = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}
    protein_list = []
    protein_list.append(''.join([
        codontab[codon] for codon in [dna_seq[i:i+3] for i in range(0,len(dna_seq)-2,3)]
    ]))
    protein_list.append(''.join([
        codontab[codon] for codon in [dna_seq[i+1:i+4] for i in range(0,len(dna_seq)-3,3)]
    ]))
    protein_list.append(''.join([
        codontab[codon] for codon in [dna_seq[i+2:i+5] for i in range(0,len(dna_seq)-4,3)]
    ]))
    dna_seq = revc(dna_seq)
    protein_list.append(''.join([
        codontab[codon] for codon in [dna_seq[i:i+3] for i in range(0,len(dna_seq)-2,3)]
    ]))
    protein_list.append(''.join([
        codontab[codon] for codon in [dna_seq[i+1:i+4] for i in range(0,len(dna_seq)-3,3)]
    ]))
    protein_list.append(''.join([
        codontab[codon] for codon in [dna_seq[i+2:i+5] for i in range(0,len(dna_seq)-4,3)]
    ]))
    print(protein_list)
    possible_protein_list = set()
    for protein in protein_list:
        for i in range(len(protein)):
            if protein[i] ==  'M':
            	for j in range(i,len(protein)):
                    if protein[j] == '*':
                        possible_protein_list.add(protein[i:j])
                        break
    return possible_protein_list
    

datafile = "Bioinformatics_Stronghold/018_orf/rosalind_orf.txt"
with open(datafile,'r') as handle:
    dna_seq = ""
    for line in handle:
        if line[0] == '>':continue
        dna_seq += line.strip()
print(dna_seq)
print("\n".join(orf(dna_seq)))