# Trilhas Coloridas - MC558 UNICAMP 1s2023
# Tiago Petena RA187700

# 1st street may be red or blue
# Street colors must be alternated
# Can only go through one street at a time
# Must return to start node

# Find alternating Eulirian circuit
# Every vertex has even degree 



class AdjList(object):
    def __init__(self, n) -> None:
        self.list = [[] for _ in range(0, n)]
        self.degrees = [0 for _ in range(0, n)]

    def link(self, a, b):
        self.list[a].append(b)
        self.list[b].append(a)

        self.degrees[a] += 1
        self.degrees[b] += 1

    def set_color(self, u, color):
        self.colors[u] = color

    def __str__(self) -> str:
        adj_string = []
        for node in self.list:
            adjs = sorted([a+1 for a in node])
            adj_string.append(f"{' '.join(map(str, adjs))}")
        return '\n'.join(adj_string)

def has_even_degrees(adj_list):
    for d in adj_list.degrees:
        if d % 2 != 0:
            return False    
    return True


def has_colorful_trail(adj_list):
    if not has_even_degrees(adj_list):
        return None
    return ""


def parse_input():

    # First line - (1 < n <= 500)
    # Number of elements in sequence d
    n_nodes, m_edges = map(int, input().split(' '))

    adj_list = AdjList(n_nodes)
    degree_list = [0 for _ in range(0, n_nodes)]
    for i in range(0, m_edges):
        u, v, c = map(int, input().split(' '))

        adj_list.link(u,v)
    
    return adj_list


def main():
    adj_list = parse_input()
    trail = has_colorful_trail(adj_list)

    if trail == None:
        print("Não possui trilha Euleriana alternante")



if __name__ == "__main__":
    main()