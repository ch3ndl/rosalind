# Completing a Tree

Chendl 2025-03-14

## Problem

An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See Figure 2.

We have already grown familiar with trees in “Mendel's First Law”, where we introduced the probability tree diagram to visualize the outcomes of a random variable.

In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.

Given: A positive integer n
 (n≤1000
) and an adjacency list corresponding to a graph on n
 nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

## Solotion

### Python

``` python
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
```
