import sys


def get_from_file(path):
    f = open(path, "r")

    node = {}
    zeros = []
    i = 0
    j = 0
    while 1:
        char = f.read(1)
        if not char:
            break

        if char >= '0' and char <= '9':
            node[(i, j)] = int(char)
            if char == '0':
                zeros.append((i, j))
            j += 1
        else:
            i += 1
            j = 0

    size = (i+1, j)
    return node, size, zeros


def make_graph(nodes, size):
    graph = {}
    for node in nodes.keys():
        neighbours = {}
        if node[0]+1 < size[0]:
            neighbours[(node[0]+1, node[1])] = nodes[(node[0]+1, node[1])]
        if node[0]-1 >= 0:
            neighbours[(node[0]-1, node[1])] = nodes[(node[0]-1, node[1])]
        if node[1]+1 < size[1]:
            neighbours[(node[0], node[1]+1)] = nodes[(node[0], node[1]+1)]
        if node[1]-1 >= 0:
            neighbours[(node[0], node[1]-1)] = nodes[(node[0], node[1]-1)]
        graph[node] = neighbours
    return graph


def draw(nodes_list, nodes, size):
    for i in range(size[0]):
        string = ''
        for j in range(size[1]):
            if (i, j) in nodes_list:
                string += str(nodes[(i, j)])
            else:
                string += ' '
        print(string)


def dijkstra(graph, zeros):
    current_node = zeros[0]
    cost = {}
    previous = {}
    q = list(graph.keys())
    s = []

    for key in graph.keys():
        cost[key] = float('inf')
        previous[key] = -1

    cost[current_node] = 0

    def key_fun(node):
        return cost[node]

    while len(q) != 0:
        node = min(q, key=key_fun)

        q.remove(node)
        s.append(node)

        neighbours = graph[node]
        for neighbour in neighbours.keys():
            if cost[neighbour] > cost[node] + neighbours[neighbour]:
                cost[neighbour] = cost[node] + neighbours[neighbour]
                previous[neighbour] = node

    current_node = zeros[1]
    previous_list = [current_node]
    while current_node != zeros[0]:
        previous_list.append(previous[current_node])
        current_node = previous[current_node]
    return previous_list


def main():
    file_name = sys.argv[1]
    nodes, size, zeros = get_from_file(file_name)
    graph = make_graph(nodes, size)
    previous_list = dijkstra(graph, zeros)
    draw(previous_list, nodes, size)


if __name__ == "__main__":
    main()
