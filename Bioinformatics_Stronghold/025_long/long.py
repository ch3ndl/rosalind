#!python3
# Chendl 2025-03-09
## Comment here


def get_overlap(s1,s2):
    max_overlap_len_1 = 0
    for i in range(1,min(len(s1),len(s2))+1):
        if s1[-i:] == s2[:i]:
            max_overlap_len_1 = i
    max_overlap_len_2 = 0
    for i in range(1,min(len(s1),len(s2))+1):
        if s2[-i:] == s1[:i]:
            max_overlap_len_2 = i
    if max_overlap_len_1 >= max_overlap_len_2:
        return max_overlap_len_1, s1, s2
    else:
        return max_overlap_len_2, s2, s1

def find_super_string(reads:list):
    temp_reads = [read for read in reads]
    max_overlap_len = 0
    max_overlap_pair = ()
    while len(temp_reads)>1:
        max_overlap_len = 0
        max_overlap_pair = ()
        for i, read_i in enumerate(temp_reads[:-1]):
            for j in range(i+1, len(temp_reads)):
                read_j = temp_reads[j]
                overlap_len, lead_read, behind_read = get_overlap(read_i,read_j)
                if overlap_len > max_overlap_len:
                    max_overlap_len = overlap_len
                    max_overlap_pair = lead_read, behind_read
        temp_reads.remove(max_overlap_pair[0])
        temp_reads.remove(max_overlap_pair[1])
        new_read = max_overlap_pair[0] + max_overlap_pair[1][max_overlap_len:]
        temp_reads.append(new_read)
    return temp_reads


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





if __name__ == '__main__':
    datafile = "Bioinformatics_Stronghold/025_long/rosalind_long.txt"
    reads = read_fasta(datafile)
    print(find_super_string(reads))
     




    
# def cost_table(reads:list)->list:
#     ret = [[0] * len(reads) for i in range(len(reads))]
#     for i,read_i in enumerate(reads):
#         for j,read_j in enumerate(reads):
#             ret[i][j] = cost(read_i,read_j)
#     return ret

# def cost(x:str,y:str)->int:
#     max_len = 0
#     for i in range(1,min(len(x),len(y))):
#         if x[-i:] == y[:i]:
#             max_len = i
#     return len(y)-max_len

# def point_least_cost_path(latest_path:list,remain_reads:list)->tuple:
#     """return:(path_cost,lastest_path)"""
#     if len(remain_reads) == 0 : return 0,latest_path
#     all_cost_path = []
#     latest_read = latest_path[-1]
#     for next_read in remain_reads:
#         #next_path = [x for x in latest_path]+[next_read]
#         next_remain_read = [read for read in remain_reads if read != next_read]
#         next_path_cost,next_path = point_least_cost_path([x for x in latest_path]+[next_read],next_remain_read)
#         all_cost_path.append(
#             (COST_TABLE[latest_read][next_read]+next_path_cost,next_path
#             )
#             )
#     return min(all_cost_path,key=lambda x:x[0])

# def least_cost_path(all_reads):
#     return [
#         point_least_cost_path([read],[x for x in all_reads if x != read]) for read in all_reads]