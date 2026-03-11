import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])

def es_arbol(n):
    if nx.is_connected(n) and nx.number_of_edges(n) == nx.number_of_nodes(n) - 1:
        return True
    return False
print(es_arbol(G))  

numero_nodos = 55
graph5 = nx.complete_graph(range(numero_nodos))
nx.draw(graph5, with_labels=True)
plt.show()
print(f"grafo 5 {es_arbol(graph5)}")