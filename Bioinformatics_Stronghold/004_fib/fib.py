#!python3
# Chendl 2024-12-31
## Comment here
datafile = "004_fib/rosalind_fib.txt"
with open(datafile, 'r') as handle:
	n,k = handle.readline().split(' ')
	n = int(n)
	k = int(k)

fib_list = [1,1] # store calculated Fn for avoiding repeated calculation

def cal_fib(n,k):
	assert n >= 1
	if n <= len(fib_list):
		return fib_list[n-1]
	if n == len(fib_list) + 1:
		fib_n = k * fib_list[n-3] + fib_list[n-2]
		fib_list.append(fib_n)
		return fib_n
	if n > len(fib_list) + 1:
		return k * cal_fib(n-2,k) + cal_fib(n-1,k) 

print(cal_fib(n,k))