#!python3
# Chendl 2025-03-06
## Comment here

import urllib.request
import urllib.error
import re

from collections import namedtuple

Record = namedtuple("Record",["id","seq"])

def download_uniprot_seq(uniprot_id:str)->str:
    uniprot_id = uniprot_id.split('_')[0]
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    try:
        response = urllib.request.urlopen(url)
        fasta_data = response.read().decode('utf-8')
        seq = ''.join([
            line for line in fasta_data.split('\n') if not line.startswith('>')
		])
        return seq
    except urllib.error.URLError as e:
        print(f"Error downloading {uniprot_id}: {e}")
        return None

datafile = "Bioinformatics_Stronghold/016_mprt/rosalind_mprt.txt"
with open(datafile,'r') as handle:
    uniprot_id_list = [line.strip() for line in handle]

record_list = [ Record(uniprot_id,download_uniprot_seq(uniprot_id)) for uniprot_id in uniprot_id_list]

pattern = r"(?=(N[^P][ST][^P]))"
for record in record_list:
    match_pos_list  = [str(match.start()+1) for match in re.finditer(pattern, record.seq)]
    if match_pos_list:
        print(record.id)
        print(' '.join(match_pos_list))