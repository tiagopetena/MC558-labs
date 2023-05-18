# Lab4 - Clusters - MC558 UNICAMP 1s2023
# Tiago Petena RA187700

DEBUG = True


class DisjointSet(object):
    def __init__(self, n) -> None:
        self.n = n
        self._sizes = [0 for _ in range(0, n)]
        self._parents = list(range(0, n))
        self.n_components = n

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return
        if self._sizes[u_root] < self._sizes[v_root]:
            self._parents[u_root] = v_root
            self._sizes[v_root] += self._sizes[u_root]
        else:
            self._parents[v_root] = u_root
            self._sizes[u_root] += self._sizes[v_root]
        self.n_components -= 1

    def find(self, v):
        x = v
        while x != self._parents[x]:
            # path compression
            y = self._parents[x]
            self._parents[x] = self._parents[y]
            x = y

        return x


class Edge(object):
    def __init__(self, u, v, w) -> None:
        self.nodes = (u, v)
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
        self.adj_list[b].append((a, edge.id))

    def sort_edges_by_weight(self):
        self.edges = {k: v for k, v in sorted(self.edges.items(), key=lambda e: e[1].weight)}
        return self.edges

    def __str__(self) -> str:
        adj_string = []
        for i, node in enumerate(self.adj_list):
            adjs = sorted([a[0] for a in node])
            node_str = f"{i}"
            adj_string.append(node_str + f": {' '.join(map(str, adjs))}")
        return "\n".join(adj_string)


def get_minimum_cost_kruskal(G, k):
    A = DisjointSet(G.n_nodes)
    G.sort_edges_by_weight()
    total_cost = 0

    for edge_id, edge in G.edges.items():
        u, v = edge.nodes

        if A.find(u) != A.find(v):
            A.union(u,v)
            total_cost += edge.weight

        if A.n_components == k:
            break

    print(total_cost)

def parse_input():
    n, m, k = map(int, input().split())
    G = Graph(n, m)

    for i in range(0, m):
        u, v, w = map(int, input().split())
        G.link(u, v, w)

    return G, k


def main():
    G, k = parse_input()

    get_minimum_cost_kruskal(G, k)


if __name__ == "__main__":
    main()
