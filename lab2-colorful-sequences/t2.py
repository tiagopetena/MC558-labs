# Trilhas Coloridas - MC558 UNICAMP 1s2023
# Tiago Petena RA187700

# 1st street may be red or blue
# Street colors must be alternated
# Can only go through one street at a time
# Must return to start node

# Find alternating Eulirian circuit
# Every vertex has even degree 

# import sys
# sys.setrecursionlimit(200000)

class Edge(object):
    def __init__(self, u, v, color) -> None:
        if color == 0:
            self.color = 'BLUE'
        else:
            self.color = 'RED'

        self.nodes = sorted([u, v])
        self.id = f"{self.nodes}"
        self.visited = False


class Graph(object):
    def __init__(self, n, m) -> None:
        self.n_nodes = n
        self.n_edges = m
        self.adj_list = [[] for _ in range(0, n)]
        self.degrees = [0 for _ in range(0, n)]
        self.edges = {}
        self.circuit = []

    def new_edge(self, u, v, color):
        edge = Edge(u, v, color)
        self.edges[edge.id] = edge
        return edge

    def link(self, a, b, color):
        edge = self.new_edge(a, b, color)

        self.adj_list[a].append((b, edge.id))
        self.adj_list[b].append((a, edge.id))

        self.degrees[a] += 1
        self.degrees[b] += 1

    def set_color(self, u, color):
        self.colors[u] = color

    def __str__(self) -> str:
        adj_string = []
        for node in self.adj_list:
            adjs = sorted([a+1 for a in node])
            adj_string.append(f"{' '.join(map(str, adjs))}")
        return '\n'.join(adj_string)

def DFS_non_recursive(G):
    stack = []
    u=0
    stack.append(u)
    last_color = None
    while stack != []:
        u = stack[-1]

        if G.degrees[u] == 0:
            G.circuit.append(u)
            stack.pop()
            continue

        for v, edge_id in G.adj_list[u][::-1]:
            if G.edges[edge_id].visited == False and G.edges[edge_id].color != last_color:
                G.edges[edge_id].visited = True
                last_color = G.edges[edge_id].color
                G.degrees[u] -= 1
                G.degrees[v] -= 1
                stack.append(v)
                break
        if stack[-1] == u:
            return None

def DFS(G):
    DFS_visit(G, 0, None)


def DFS_visit(G, u, last_color):
    for v, edge_id in G.adj_list[u]:
        if G.degrees[u] == 0: break
        if G.edges[edge_id].visited == False and G.edges[edge_id].color != last_color:
            G.edges[edge_id].visited = True
            G.degrees[u] -= 1
            G.degrees[v] -= 1
            DFS_visit(G, v, G.edges[edge_id].color)
    G.circuit.append(u)


def has_even_degrees(G):
    for d in G.degrees:
        if d % 2 != 0:
            return False    
    return True


def has_colorful_trail(G):
    if not has_even_degrees(G):
        return None
    DFS_non_recursive(G)
    if len(G.circuit) != G.n_edges + 1:
        return None
    if G.circuit[0] != G.circuit[-1]:
        return None
    return G.circuit


def parse_input():

    # First line - (1 < n <= 500)
    # Number of elements in sequence d
    n, m = map(int, input().split(' '))
    G = Graph(n, m)

    for i in range(0, m):
        u, v, c = map(int, input().split(' '))
        G.link(u,v, c)

    return G


def main():
    G = parse_input()
    trail = has_colorful_trail(G)

    if trail == None:
        print("Não possui trilha Euleriana alternante")
    else:
        print(*trail)


if __name__ == "__main__":
    main()