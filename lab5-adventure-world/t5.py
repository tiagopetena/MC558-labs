# Lab5 - MC558 UNICAMP 1s2023
# Tiago Petena RA187700


class Edge(object):
    def __init__(self, u, v) -> None:
        self.nodes = (u, v)
        self.id = f"{self.nodes}"


class Graph(object):
    def __init__(self, n, m, w) -> None:
        self.n_nodes = n
        self.n_edges = m
        self.weights = w
        self.adj_list = [[] for _ in range(0, n)]
        self.in_degrees = [0 for _ in range(0, n)]
        self.out_degrees = [0 for _ in range(0, n)]
        self.edges = {}

    def new_edge(self, u, v):
        edge = Edge(u, v)
        self.edges[edge.id] = edge
        self.out_degrees[u] += 1
        self.in_degrees[v] += 1
        return edge

    def link(self, a, b):
        edge = self.new_edge(a, b)
        self.adj_list[a].append((b, edge.id))

    def __str__(self) -> str:
        adj_string = []
        for i, node in enumerate(self.adj_list):
            adjs = sorted([a[0] for a in node])
            node_str = f"{i}({self.weights[i]})"
            adj_string.append(node_str + f": {' '.join(map(str, adjs))}")
        return "\n".join(adj_string)


def parse_input():
    n = int(input())
    w = list(map(int, input().split()))
    m = int(input())
    G = Graph(n, m, w)
    for _ in range(0, m):
        u, v = map(int, input().split())
        G.link(u, v)

    print(f"Rooms: {n}")
    print(f"Doors: {m}")
    print(f"Weights: {w}")
    print(G)

    return G


def main():
    G = parse_input()


if __name__ == "__main__":
    main()
