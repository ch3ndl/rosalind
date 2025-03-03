# Overlap Graphs

Chendl 2025-03-03

## Problem

A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v
 and head w
 is represented by (v,w)
 (but not by (w,v)
). A directed loop is a directed edge of the form (v,v)
.

For a collection of strings and a positive integer k
, the overlap graph for the strings is a directed graph Ok
 in which each string is represented by a node, and string s
 is connected to string t
 with a directed edge when there is a length k
 suffix of s
 that matches a length k
 prefix of t
, as long as s≠t
; we demand s≠t
 to prevent directed loops in the overlap graph (although directed cycles may be present).

### Given

A collection of DNA strings in FASTA format having total length at most 10 kbp.

### Return

The adjacency list corresponding to O3
. You may return edges in any order.

## Solotion

### Shell

``` bash

```

### Python

``` python
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
```