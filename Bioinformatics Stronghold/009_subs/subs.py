#!python3
# Chendl 2025-02-03
## use kmp algorithm

datafile = "Bioinformatics Stronghold/009_subs/test.txt"
with open(datafile, 'r') as handle:
	string_s = handle.readline().strip()
	string_t = handle.readline().strip()

def pythonic_search(s:str,t:str):
    return [i+1 for i in range(len(s)) if s.startswith(t, i)]


def brute_force(s:str,t:str):
	len_s = len(s)
	len_t = len(t)
	ret = []
	for i in range(len_s-len_t+1):
		if s[i:i+len_t] == t:
			ret.append(i+1)
	return ret

def kmp_search(s: str, t: str):
    # Preprocess the pattern (t) to create the partial match table
    def compute_lps_array(pattern: str):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    len_s = len(s)
    len_t = len(t)
    lps = compute_lps_array(t)
    i = 0  # index for s
    j = 0  # index for t
    ret = []

    while i < len_s:
        if t[j] == s[i]:
            i += 1
            j += 1

            if j == len_t:
                ret.append(i - j + 1)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print(lps)
    print(t)
    return ret

# Example usage:
# brute_force(string_s, string_t)
# print(pythonic_search(string_s, string_t))
print(kmp_search(string_s, string_t))

brute_force(string_s,string_t)
print(pythonic_search(string_s,string_t))
print(kmp_search(string_s,string_t))