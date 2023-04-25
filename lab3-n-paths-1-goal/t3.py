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
        adj_g = [[] for _ in range(0, n)]
        adj_y = [[] for _ in range(0, n)]
        adj_r = [[] for _ in range(0, n)]
        self.adj_lists = [adj_g, adj_y, adj_r]
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
        self.adj_lists[color][a].append((b, edge.id))

    def set_color(self, u, color):
        self.colors[u] = color

    def __str__(self) -> str:
        adj_string = []
        for i, node in enumerate(sum(self.adj_lists, [])):
            adjs = sorted([a[0] for a in node])
            node_str = f"{i}"
            if self.target == i:
                node_str += "(target)"
            if self.start == i:
                node_str += "(start)"
            adj_string.append(node_str + f": {' '.join(map(str, adjs))}")
        return "\n".join(adj_string)


def topological_ordering(G):
    u = 0
    stack = [G.start]
    visited = [False for v in range(G.n_nodes)]
    ordering = []
    while stack != []:
        visited_all = True
        u = stack[-1]

        visited_all = True
        # Green
        for v, edge_id in G.adj_lists[0][u]:
            if visited[v] == False:
                visited[v] = True
                stack.append(v)
                visited_all = False
        # Yellow
        for v, edge_id in G.adj_lists[1][u]:
            if visited[v] == False:
                visited[v] = True
                stack.append(v)
                visited_all = False
        # Red
        for v, edge_id in G.adj_lists[2][u]:
            if visited[v] == False:
                visited[v] = True
                stack.append(v)
                visited_all = False
        if visited_all:
            ordering.insert(0, u)
            stack.pop()
    print(ordering)


def parse_input():
    n, m, s, t = map(int, input().split(" "))
    G = Graph(n, m, s, t)

    for i in range(0, m):
        u, v, c = map(int, input().split(" "))
        G.link(u, v, c)

    return G


def main():
    G = parse_input()
    print(G)
    topological_ordering(G)


if __name__ == "__main__":
    main()
