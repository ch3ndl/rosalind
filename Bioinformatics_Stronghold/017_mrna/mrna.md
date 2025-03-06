# Inferring mRNA from Protein

Chendl 2025-03-06

## Problem

For positive integers a
 and n
, a
 modulo n
 (written amodn
 in shorthand) is the remainder when a
 is divided by n
. For example, 29mod11=7
 because 29=11×2+7
.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a
 and b
 are congruent modulo n
 if amodn=bmodn
; in this case, we use the notation a≡bmodn
.

Two useful facts in modular arithmetic are that if a≡bmodn
 and c≡dmodn
, then a+c≡b+dmodn
 and a×c≡b×dmodn
. To check your understanding of these rules, you may wish to verify these relationships for a=29
, b=73
, c=10
, d=32
, and n=11
.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

## Solotion

### Python

``` python
def mrna(protein:str)->int:
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
	codon_num_for_amino = {
		amino:sum([1 for i in codontab.values() if i == amino]) for amino in set(codontab.values())
	}
	potential_num = codon_num_for_amino['*']
	for amino in protein:
		potential_num *= codon_num_for_amino[amino]
	return potential_num % 1000000

print(mrna("MANPKPESQWNPLAAWTNIVMTKWLSQWHYMHKPLRCHFHIKIIDRMETYNSDPGGCARSESFLNRAFMCRCKVFNMNVSFQGPNSRAERVPWNKCSFQCWHQLKQLFNVQLKDVRAIIGWLLRIQYCIALYNQQLQVVMERCKQNYEYANQWHPDPCTQIKGGSRHGACTLEQLGIYESTDDVNASKMPTGWHHMFLDEQRCYEWYQIITFAHKFQLYTMQHRNWKSWPYMMCFYKDSWVYTINLVSWNGYPWTPKFLCQFHDMIPWQLHFHIWRKEKTWAWRCSVDLVKQFLWLPMFYLPSTAQRIWCFNMFHTNWHRVGMLYEVTRNHIREIDWTNWHKYEECDFPARPPVYEAKQRKCMPEQMQMFAPIADWHKCCEGMRAIFACVDLPKPWDWAHCTGVHDPLWKHKLPNSVPHLEDHDGMWFDMDNRNKVCHYATEWGDRCSRQGSPADNSWMHVEQWQRPEWYNPGWWMCAQWPAIWWLEEKRSKKNHYEKWKNMQYMRFADQHCQLVTWGDNDSSGLSLPHCGTEEYADMIFSHCGPWAFDGGCYWAQQESDNNSMMRAWYDSNRVRRNKFKSCIYMRFRGVAKDEQHAIEIGPPWVWFIPMGEERGPIPEPTKGHDNRKATEVGVQFIGPIQDTQTHCQYPSPEMIDENLSQDSNDPSTGHKERVAMYTMSANTKLFLRQGRHTASKKVMYIEPHNYWAREPEMGREMHMQSYWCLWTLMANDLKTYYHAVGGPGWKITMDIGGEFTPTNESSPWFNDRWFPEHINQKGIAIFCQKMSIKARWQGGFLFTNFGEYRVKDWGDPSNNKENIMQWWVNHNQMDDWYKKHYTPRQKRDWAFDKLSVTIYDHVYWSPEIFRPVALCCNFFDFDTSETKCMPSEYQGGWGVTHYADWPKANKVHFSSGTFFTIKFSRDRDTARFYWCTYHVFGDYFHYFCTHHYYMFVDGKHKTGISEHQLKRAWPNPNSTVYKSWFNLNKITTCRLQLLISCFT"))
```
