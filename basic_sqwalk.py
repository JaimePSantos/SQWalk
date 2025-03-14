from sqwalk import SQWalker

from qutip import ket2dm, basis, Options, Qobj
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#Number of nodes in the line
N = 50
#Build the graph using networkx (or the module of your choice)
graph = nx.path_graph(N)
nx.draw_circular(graph)

adj = nx.adjacency_matrix(graph).todense()
# plt.imshow(adj)
# plt.show()