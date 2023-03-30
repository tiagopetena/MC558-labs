class AdjList:
    def __init__(self, n) -> None:
        self.list = [[] for _ in range(0, n)]

    def link(self, a, b):
        self.list[a].append(b)
        self.list[b].append(a)

    def __str__(self) -> str:
        adj_string = []
        for node in self.list:
            adjs = sorted([a+1 for a in node])
            adj_string.append(f"{' '.join(map(str, adjs))}")
        return '\n'.join(adj_string)


class Node:
    def __init__(self, degree, index) -> None:
        self.degree = degree
        self.index = index
        self.adj = []

    def link(self, node):
        self.adj.append(node)

    def __str__(self) -> str:
        return f"{self.index}: {self.degree}"

    def _get_adjs(self):
        return f"{' '.join(map(str, self.adj))}"


class Sequence:
    def __init__(self, degrees):

        self.n = len(degrees)
        self.nodes = []
        for d, idx in zip(degrees, range(0, self.n)):
            new_node = Node(d, idx)
            self.nodes.append(new_node)
        self.adj_list = AdjList(n)

    def link(self, a, b):
        self.adj_list.link(self.nodes[a].index, self.nodes[b].index)

    def pop(self, index):
        node = self.nodes.pop(index)
        return node

    def sort(self):
        sorted_nodes = sorted(self.nodes, key=lambda x: x.degree, reverse=True)
        self.nodes = sorted_nodes

    def __str__(self) -> str:
        string = ""
        for node in self.nodes:
            string += f"{node._get_adjs()}\n"
        return string

    def __len__(self) -> int:
        return len(self.nodes)


def parse_input():

    # First line - (1 < n <= 500)
    # Number of elements in sequence d
    n_line = input()
    n = int(n_line)
    assert 1 <= n <= 500, f"Invalid sequence' size '{n}'. (1 <= n <= 500)."

    # Second line
    # Sequence d
    sequence_line = input()
    sequence = [int(d) for d in sequence_line.split(" ")]
    assert len(sequence) == n, f"n != length of sequence."

    return n, sequence


def is_graphical_sequence(sequence, node=0):
    if len(sequence) == 1:
        if sequence.nodes[0].degree == 0:
            return True
        else:
            return False

    max_degree = sequence.nodes[0].degree
    if max_degree >= len(sequence):
        return False
    for d in range(1, max_degree+1):
        sequence.link(node, d)
    sequence.pop(0)
    for d in range(0, max_degree):
        sequence.nodes[d].degree -= 1


    sequence.sort()

    return is_graphical_sequence(sequence, node)


if __name__ == "__main__":

    n, degrees = parse_input()
    sequence = Sequence(degrees)

    is_graphical = is_graphical_sequence(sequence, node=0)

    if is_graphical:
        print(sequence.adj_list)
    else:
        print("Não é sequência gráfica!")
