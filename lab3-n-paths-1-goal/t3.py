# Lab3 - Muitos caminhos e um destino - MC558 UNICAMP 1s2023
# Tiago Petena RA187700


class Edge(object):
    def __init__(self, u, v, color) -> None:
        self.color = color
        self.nodes = [u, v]
        self.id = f"{self.nodes}"
        self.visited = False


class Graph(object):
    def __init__(self, n, m, s, t) -> None:
        self.n_nodes = n
        self.n_edges = m
        self.adj_list = [[] for _ in range(0, n)]
        self.in_degrees = [0 for _ in range(0, n)]
        self.out_degrees = [0 for _ in range(0, n)]
        self.edges = {}
        self.circuit = []
        self.start = s
        self.target = t

    def new_edge(self, u, v, color):
        edge = Edge(u, v, color)
        self.edges[edge.id] = edge
        self.out_degrees[u] += 1
        self.in_degrees[v] += 1
        return edge

    def link(self, a, b, color):
        edge = self.new_edge(a, b, color)
        self.adj_list[a].append((b, edge.id))

    def set_color(self, u, color):
        self.colors[u] = color

    def __str__(self) -> str:
        adj_string = []
        for i, node in enumerate(self.adj_list):
            adjs = sorted([a[0] for a in node])
            node_str = f"{i}"
            if self.target == i:
                node_str += "(target)"
            if self.start == i:
                node_str += "(start)"
            adj_string.append(node_str + f": {' '.join(map(str, adjs))}")
        return '\n'.join(adj_string)


def parse_input():

    n, m, s, t= map(int, input().split(" "))
    G = Graph(n, m, s, t)

    for i in range(0, m):
        u, v, c = map(int, input().split(" "))
        G.link(u, v, c)

    return G


def main():
    G = parse_input()
    print(G)


if __name__ == "__main__":
    main()
