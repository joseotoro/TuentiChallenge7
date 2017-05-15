import networkx as nx


class Shortcut:
    def __init__(self, src, dst, time):
        self.src = src
        self.dst = dst
        self.time = time


def distance(a, b):
    b -= 1
    return ((b - a) + 1) * (a + b) // 2


with open('submitInput.txt', 'rb') as f:
    cases = int(f.readline())

    with open('output.txt', 'w') as out:
        for case in range(cases):
            print('Case {}/{}'.format(case + 1, cases))
            num_floors, num_shortcuts = map(int, f.readline().split())
            shortcuts = []

            node_numbers = set()
            node_numbers.add(1)
            node_numbers.add(num_floors)
            for _ in range(num_shortcuts):
                src, dst, time = map(int, f.readline().split())
                if time < distance(src, dst):
                    shortcuts.append(Shortcut(src, dst, time))
                    node_numbers.add(src)
                    node_numbers.add(dst)

            node_numbers = list(node_numbers)
            node_numbers.sort()

            g = nx.MultiDiGraph()
            g.add_nodes_from(node_numbers)
            for index in range(1, len(node_numbers)):
                first = node_numbers[index - 1]
                second = node_numbers[index]
                g.add_edge(first, second, weight=distance(first, second))
                g.add_edge(second, first, weight=0)

            for s in shortcuts:
                g.add_edge(s.src, s.dst, weight=s.time)

            result = nx.shortest_path_length(g, 1, node_numbers[-1], 'weight')
            g.clear()
            out.write('Case #{}: {}\n'.format(case + 1, result))
