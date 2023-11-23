from graphviz import Digraph

# Creating Nodes
A = Node('A')
B = Node('B')
C = Node('C')

# Adding Neighbors
A.addOutNeighbor(B, 1)
A.addOutNeighbor(C, 2)
B.addOutNeighbor(C, 3)

# Creating Graph
G = [A, B, C]

# Running Prim's Algorithm
MST = prim(G, A)

# Creating Graphviz object
dot = Digraph()

# Adding Edges for Original Graph
dot.edge('A', 'B', label='1')
dot.edge('A', 'C', label='2')
dot.edge('B', 'C', label='3')

# Adding Edges for MST (you may need to adapt this to match the structure of MST)
for i in range(len(MST) - 1):
    u = MST[i]
    v = MST[i + 1]
    # Assuming there is a way to get the weight between u and v
    wt = get_weight(u, v)  # You will need to define this function
    dot.edge(str(u), str(v), label=str(wt))

# Render the graph
dot.render('graph.gv', view=True)
