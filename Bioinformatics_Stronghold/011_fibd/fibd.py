#!python3
# Chendl 2025-03-03
## Comment here

def fibd(n,m):
	num_of_age = [1] + [0]*(m-1)
	for i in range(n-1):
		num_of_age.insert(0, sum(
			num_of_age[1:]
		))
		num_of_age.pop()
	return sum(num_of_age)

print(fibd(80,16))
# if __name__ == "__main__":
# 	main()