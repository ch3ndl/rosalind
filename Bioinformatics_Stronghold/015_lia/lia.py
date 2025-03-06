#!python3
# Chendl 2025-03-05
## Comment here

# AABB AABb AAbb AaBB AaBb Aabb aaBB aaBb aabb

from math import comb

AA = [1/2,1/2,0]
Aa = [1/4,2/4,1/4]


def lia(k:int,n:int):
	population = 2**k
	probability = 1
	for i in range(n):
		probability -= (1/4)**i * (3/4)**(population-i) * comb(population,i)
	return probability
	# probability_list = [1/4,2/4,1/4]
	# # probability_list = [1/16,2/16,1/16,2/16,4/16,2/16,1/16,2/16,1/16]
	# new_probability_list = [0,0,0]
	# for i in range(k):
	# 	new_probability_list = [0,0,0]
	# 	AA = [1/2,1/2,0]
	# 	Aa = [1/4,2/4,1/4]
	# 	aa = [0,1/2,1/2]
	# 	for probability, a_type in zip(probability_list,[AA,Aa,aa]):
	# 		for j, a_prob in enumerate(a_type):
	# 			new_probability_list[j] += probability*probability_list[j]
	# 	probability_list = new_probability_list
	# return probability_list

print(f"{lia(5,7):.3}")