#!python3
# Chendl 2024-12-31
## Comment here
datafile = "3_revc/rosalind_revc.txt"
with open(datafile, 'r') as handle:
	line_list = handle.readlines()
	string = ''.join([
		line.strip() for line in line_list
	])
complementary_dict = {
	"A":"T",
	"T":"A",
	"G":"C",
	"C":"G",
}
string = ''.join([
	complementary_dict[i] for i in string[::-1]
])
print(string)