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
        rev_adj_g = [[] for _ in range(0, n)]
        rev_adj_y = [[] for _ in range(0, n)]
        rev_adj_r = [[] for _ in range(0, n)]
        self.rev_adj_lists = [rev_adj_g, rev_adj_y, rev_adj_r]
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
        self.rev_adj_lists[color][b].append((a, edge.id))

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
    visited_adjs = [False for v in range(G.n_nodes)]
    ordering = []
    while stack != []:
        u = stack[-1]
        visited[u] = True

        if visited_adjs[u] == True:
            stack.pop()
            continue

        added_edge = False
        # Green
        for v, edge_id in G.adj_lists[0][u]:
            if visited[v] == False:
                stack.append(v)
                added_edge = True
        # Yellow
        for v, edge_id in G.adj_lists[1][u]:
            if visited[v] == False:
                # visited[v] = True
                stack.append(v)
                added_edge = True
        # Red
        for v, edge_id in G.adj_lists[2][u]:
            if visited[v] == False:
                # visited[v] = True
                stack.append(v)
                added_edge = True

        if added_edge == False:
            visited_adjs[u] = True
            ordering.append(u)
    
    return ordering


def path_count_recurrence(G, u):
    n_paths = 0

    # Green Paths
    for v, edge_id in G.rev_adj_lists[0]:
        if v == G.target:
            pass
        

def count_paths(G, topological_order):
    green_paths = [0 for _ in range(0, G.n_nodes)]
    yellow_paths = [0 for _ in range(0, G.n_nodes)]
    red_paths = [0 for _ in range(0, G.n_nodes)]

    i = 0
    u = topological_order[i]
    while u != G.target:
        green_paths[u] = 0
        yellow_paths[u] = 0
        red_paths[u] = 0
        i += 1
        if i > len(topological_order) - 1:
            return [0 for _ in range(0, G.n_nodes)]
        u = topological_order[i]

    green_paths[u] = 0
    yellow_paths[u] = 0
    red_paths[u] = 0
    i += 1
    u = topological_order[i]

    for i in range(i, len(topological_order)):
        u = topological_order[i]
        # Green Paths
        for v, edge_id in G.adj_lists[0][u]:
            if v == G.target:
                green_paths[u] += 1
            green_paths[u] += green_paths[v] + yellow_paths[v] + red_paths[v]
        # Yellow Paths
        for v, edge_id in G.adj_lists[1][u]:
            if v == G.target:
                yellow_paths[u] += 1
            yellow_paths[u] += green_paths[v] + yellow_paths[v]
        # Red Paths
        for v, edge_id in G.adj_lists[2][u]:
            if v == G.target:
                red_paths[u] += 1
            red_paths[u] += green_paths[v]
        # i += 1
    n_paths = [g + y + r for g, y, r in zip(green_paths, yellow_paths, red_paths)]
    # print(n_paths)
    # print()
    return n_paths

def parse_input():
    n, m, s, t = map(int, input().split())
    G = Graph(n, m, s, t)

    for i in range(0, m):
        u, v, c = map(int, input().split())
        G.link(u, v, c)

    return G


def main():
    G = parse_input()
    if G.target == G.start:
        print(1)
        return
    # print(G)
    topological_order = topological_ordering(G)
    n_paths = count_paths(G, topological_order)
    print(n_paths[G.start])

if __name__ == "__main__":
    main()
