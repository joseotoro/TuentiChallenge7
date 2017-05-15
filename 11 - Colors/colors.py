import networkx as nx


def main():
    with open('submitInput.txt', 'r') as f:
        cases = int(f.readline())
        with open('output.txt', 'w') as out:
            for case in range(cases):
                print('Case {}/{}'.format(case + 1, cases))
                number_colors = int(f.readline())
                colors = {}
                max_color = 0
                for c in range(number_colors):
                    color_description = f.readline().split()
                    color_name = color_description[0]
                    number_components = int(color_description[1])
                    color_components = set(color_description[2:])
                    if number_components == 0:
                        colors[color_name] = 1 << (c + 1)
                        max_color += 1
                    else:
                        result = 0
                        for base in color_components:
                            result |= colors[base]
                        colors[color_name] = result
                max_color = 1 << (max_color + 1)

                # Create graph
                gr = nx.MultiDiGraph()
                number_galaxies = int(f.readline())

                # Same galaxy inner links
                for g in range(number_galaxies):
                    for x in range(max_color):
                        c_id = '{0:010b}'.format(x)
                        gr.add_node('{}{}'.format(g, c_id))
                    number_colors = int(f.readline())
                    for c in range(number_colors):
                        color, time = f.readline().split()
                        cc = colors[color]
                        for x in range(max_color):
                            r = cc | x
                            if r != x:
                                src_id = '{0:010b}'.format(x)
                                dst_id = '{0:010b}'.format(r)
                                src = '{}{}'.format(g, src_id)
                                dst = '{}{}'.format(g, dst_id)
                                gr.add_edge(src, dst, weight=int(time))

                number_wormholes = int(f.readline())
                for _ in range(number_wormholes):
                    color, src, dst = f.readline().split()
                    c = colors[color]
                    for x in range(max_color):
                        if c & x == c:
                            r = c ^ x
                            src_id = '{0:010b}'.format(x)
                            dst_id = '{0:010b}'.format(r)
                            s = '{}{}'.format(src, src_id)
                            d = '{}{}'.format(dst, dst_id)
                            gr.add_edge(s, d, weight=0)

                x = '0{0:010b}'.format(0)
                result = nx.single_source_dijkstra_path_length(gr, x)
                res = []
                for x in range(number_galaxies):
                    val = None
                    for y in range(max_color):
                        c_id = '{0:010b}'.format(y)
                        node = '{}{}'.format(x, c_id)
                        if node in result:
                            if val is None:
                                val = result[node]
                            else:
                                val = min(val, result[node])
                    if val is None:
                        res.append('-1')
                    else:
                        res.append(str(val))

                out.write('Case #{}: {}\n'.format(case + 1, ' '.join(res)))


if __name__ == "__main__":
    main()
