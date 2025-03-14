#!python3
# Chendl 2025-03-14
## Comment here


def min_edge_num_for_tree(node_num, edges):
	nodes = [i for i in range(1,node_num+1)]
	linked_nodes_clusters = []
	for edge in edges:
		if any([i in nodes for i in edge]):
			if edge[1] in nodes and any([edge[0] in cluster for cluster in linked_nodes_clusters]):
				cluster_index = [edge[0] in cluster for cluster in linked_nodes_clusters].index(True)
				linked_nodes_clusters[cluster_index].append(edge[1])
				nodes.remove(edge[1])
				continue
			if edge[0] in nodes and any([edge[1] in cluster for cluster in linked_nodes_clusters]):
				cluster_index = [edge[1] in cluster for cluster in linked_nodes_clusters].index(True)
				linked_nodes_clusters[cluster_index].append(edge[0])
				nodes.remove(edge[0])
				continue
			linked_nodes_clusters.append(edge)
			nodes.remove(edge[0])
			nodes.remove(edge[1])
		else:
			cluster1_index = [edge[0] in cluster for cluster in linked_nodes_clusters].index(True)
			cluster2_index = [edge[1] in cluster for cluster in linked_nodes_clusters].index(True)
			linked_nodes_clusters[cluster1_index] += linked_nodes_clusters[cluster2_index]
			linked_nodes_clusters.pop(cluster2_index)
	for node in nodes:
		linked_nodes_clusters.append([node])
	return len(linked_nodes_clusters)-1
		

if __name__ == "__main__":
	datafile = 'Bioinformatics_Stronghold/032_tree/rosalind_tree.txt'
	with open(datafile, 'r') as handle:
		lines = [line.strip() for line in handle]
		node_num = int(lines[0])
		edges = [[int(i) for i in line.split(' ')] for line in lines[1:]]
	print(min_edge_num_for_tree(node_num,edges))