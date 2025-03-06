#!python3
# Chendl 2025-03-06
## Comment here

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
		amino:sum([
			1 for i in codontab.values() if i == amino
			]) for amino in set(codontab.values())
	}
	potential_num = codon_num_for_amino['*']
	for amino in protein:
		potential_num *= codon_num_for_amino[amino]
	return potential_num % 1000000

print(mrna("MANPKPESQWNPLAAWTNIVMTKWLSQWHYMHKPLRCHFHIKIIDRMETYNSDPGGCARSESFLNRAFMCRCKVFNMNVSFQGPNSRAERVPWNKCSFQCWHQLKQLFNVQLKDVRAIIGWLLRIQYCIALYNQQLQVVMERCKQNYEYANQWHPDPCTQIKGGSRHGACTLEQLGIYESTDDVNASKMPTGWHHMFLDEQRCYEWYQIITFAHKFQLYTMQHRNWKSWPYMMCFYKDSWVYTINLVSWNGYPWTPKFLCQFHDMIPWQLHFHIWRKEKTWAWRCSVDLVKQFLWLPMFYLPSTAQRIWCFNMFHTNWHRVGMLYEVTRNHIREIDWTNWHKYEECDFPARPPVYEAKQRKCMPEQMQMFAPIADWHKCCEGMRAIFACVDLPKPWDWAHCTGVHDPLWKHKLPNSVPHLEDHDGMWFDMDNRNKVCHYATEWGDRCSRQGSPADNSWMHVEQWQRPEWYNPGWWMCAQWPAIWWLEEKRSKKNHYEKWKNMQYMRFADQHCQLVTWGDNDSSGLSLPHCGTEEYADMIFSHCGPWAFDGGCYWAQQESDNNSMMRAWYDSNRVRRNKFKSCIYMRFRGVAKDEQHAIEIGPPWVWFIPMGEERGPIPEPTKGHDNRKATEVGVQFIGPIQDTQTHCQYPSPEMIDENLSQDSNDPSTGHKERVAMYTMSANTKLFLRQGRHTASKKVMYIEPHNYWAREPEMGREMHMQSYWCLWTLMANDLKTYYHAVGGPGWKITMDIGGEFTPTNESSPWFNDRWFPEHINQKGIAIFCQKMSIKARWQGGFLFTNFGEYRVKDWGDPSNNKENIMQWWVNHNQMDDWYKKHYTPRQKRDWAFDKLSVTIYDHVYWSPEIFRPVALCCNFFDFDTSETKCMPSEYQGGWGVTHYADWPKANKVHFSSGTFFTIKFSRDRDTARFYWCTYHVFGDYFHYFCTHHYYMFVDGKHKTGISEHQLKRAWPNPNSTVYKSWFNLNKITTCRLQLLISCFT"))