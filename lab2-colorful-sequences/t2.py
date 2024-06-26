# Trilhas Coloridas - MC558 UNICAMP 1s2023
# Tiago Petena RA187700

# 1st street may be red or blue
# Street colors must be alternated
# Can only go through one street at a time
# Must return to start node

# Find alternating Eulirian circuit
# Every vertex has even degree 


class Edge(object):
    def __init__(self, u, v, color) -> None:
        self.color = color

        if u < v:
            self.nodes = [u, v]
        else:
            self.nodes = [v, u]
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
    u=0
    stack = [u]
    color_stack = [None]
    while stack != []:
        u = stack[-1]
        last_color = color_stack[-1]

        if G.degrees[u] == 0:
            G.circuit.append(u)
            stack.pop()
            color_stack.pop()
        else:
            changed = False
            for v, edge_id in G.adj_list[u]:
                if G.edges[edge_id].visited == False and G.edges[edge_id].color != last_color:
                    G.edges[edge_id].visited = True

                    G.degrees[u] -= 1
                    G.degrees[v] -= 1
                    stack.append(v)
                    color_stack.append(G.edges[edge_id].color)
                    G.adj_list[u].remove((v, edge_id))
                    G.adj_list[v].remove((u, edge_id))
                    changed = True
                    break
        if not changed:
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


def validate_colors(G):
    edges_taken = []
    
    for i in range(0, len(G.circuit)-1):
        edges_taken.append([G.circuit[i],G.circuit[i+1]])
    colors = []
    for i, edge_c in enumerate(edges_taken):
        edge_key = f"{sorted(edge_c)}"
        color = G.edges[edge_key].color
        colors.append(color)
        if i != 0:
            if colors[-1] == colors[-2]:
                print(f"INVALID TRASITION: {edge_c}: {color}")

def has_even_degrees(G):
    for d in G.degrees:
        if d % 2 != 0:
            return False    
    return True


def has_colorful_trail(G):
    # if not has_even_degrees(G):
    #     return None
    DFS_non_recursive(G)
    if len(G.circuit) != G.n_edges + 1:
        return None
    if G.circuit[0] != G.circuit[-1]:
        return None
    # validate_colors(G)
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