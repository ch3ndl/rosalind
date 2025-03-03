#!python3
# Chendl 2025-02-02
## Comment here
with open('007_iprb/rosalind_iprb.txt', 'r') as file:
    k,m,n = [int(i) for i in file.readline().strip().split(' ')]
num = k+m+n

print(f"{k/num + m/num * k/(num-1) + m/num * (m-1)/(num-1) * 3/4 + m/num * n/(num-1) * 1/2 + n/num * k/(num-1) + n/num * m/(num-1) * 1/2:.6f}")