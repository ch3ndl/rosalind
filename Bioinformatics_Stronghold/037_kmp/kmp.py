#!python3
# Chendl 2025-03-15
## Comment here

import os
import sys

import argparse as ap

from sys import argv

def fail_arr(string):
	arr = [0] * len(string)
	i = 1
	length = 0
	while i < len(string):
		if string[i] == string[length]:
			length += 1
			arr[i] = length
			i += 1
		else:
			if length != 0:
				length = arr[length - 1]
			else:
				arr[i] = 0
				i += 1
	return arr


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

if __name__ == "__main__":
	datafile = 'Bioinformatics_Stronghold/037_kmp/rosalind_kmp.txt'
	seq = read_fasta(datafile)[0]
	print(' '.join([str(i) for i in fail_arr(seq)]))