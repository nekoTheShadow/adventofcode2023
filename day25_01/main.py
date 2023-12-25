import networkx

G = networkx.Graph()
with open('./input.txt') as f:
    for line in f:
        src, dsts = line.strip().split(': ')
        for dst in dsts.split(' '):
            G.add_edge(src.strip(), dst.strip())

cut_set = networkx.minimum_edge_cut(G)
G.remove_edges_from(cut_set)
ans = 1
for connected_component in networkx.connected_components(G):
    ans *= len(connected_component)
print(ans)