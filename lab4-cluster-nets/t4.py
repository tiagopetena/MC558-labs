# Lab4 - Clusters - MC558 UNICAMP 1s2023
# Tiago Petena RA187700

DEBUG = True

class DisjointSet(object):
    def __init__(self, n) -> None:
        self._elements = [[] for _ in range(0, n)]
        self._parents = [[] for _ in range(0, n)]
    

    def union(self, u, v):

        return
    
    def find(self, v):
        x = v
        while x != self._parents[x]:
            # path compression
            y = self._parents[x]
            self._parents[x] = self._parents[y]
            x = y

        return y
        



class Edge(object):
    def __init__(self, u, v, w) -> None:
        self.nodes = [u, v]
        self.weight = w
        self.id = f"{self.nodes}"


class Graph(object):
    def __init__(self, n, m) -> None:
        self.n_nodes = n
        self.n_edges = m
        self.adj_list = [[] for _ in range(0, n)]
        self.in_degrees = [0 for _ in range(0, n)]
        self.out_degrees = [0 for _ in range(0, n)]
        self.edges = {}

    def new_edge(self, u, v, w):
        edge = Edge(u, v, w)
        self.edges[edge.id] = edge
        self.out_degrees[u] += 1
        self.in_degrees[v] += 1
        return edge

    def link(self, a, b, w):
        edge = self.new_edge(a, b, w)
        self.adj_list[a].append((b, edge.id))

    def __str__(self) -> str:
        adj_string = []
        for i, node in enumerate(self.adj_list):
            adjs = sorted([a[0] for a in node])
            node_str = f"{i}"
            adj_string.append(node_str + f": {' '.join(map(str, adjs))}")
        return "\n".join(adj_string)


def parse_input():
    n, m, k = map(int, input().split())
    G = Graph(n, m)

    for i in range(0, m):
        u, v, w = map(int, input().split())
        G.link(u, v, w)

    if DEBUG: print(G)

    return G, k


def main():


    G = parse_input()


if __name__ == "__main__":
    main()
