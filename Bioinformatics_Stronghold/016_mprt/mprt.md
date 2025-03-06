# Finding a Protein Motif

Chendl 2025-03-06

## Problem

To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

## Solotion

It is harder that it seems like. 
The ID that rosalind give cannot be directly used in url.
We must split by '_' and take the first part as the access ID.

Another problem is that repeatly motic. Take an example, assert that we want match AA in string AAAA. Position 1,3 is wrong and the right answer is pos 1,2,3. 

The regex pattern used to repeatly match get by google. It check every char and then check the string after it.

### Python

``` python
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

pattern = r"(?=(N[^P][ST][^P]))" # repeat macth 
for record in record_list:
    match_pos_list  = [str(match.start()+1) for match in re.finditer(pattern, record.seq)]
    if match_pos_list:
        print(record.id)
        print(' '.join(match_pos_list))
```

