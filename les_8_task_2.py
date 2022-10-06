# Задание 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijkstra_vertexes(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    vertex_list = [[0] for j in range(length)]
    input_start = start

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i, c in enumerate(cost):
        if (c != input_start) and (c < float('inf')):
            if (vertex_list[i][input_start] != parent[i]):
                vertex_list[i].append(parent[i])

            vertex_list[i].append(i)

        elif c == float('inf'):
            vertex_list[i] = None

    for i in vertex_list:
        if len(i) > 2:
            for j in range(1, (len(i) - 1)):
                spam = i[j]

    result = {i: vertex_list[i] for i in range(len(vertex_list))}
    return result

s = int(input('От какой вершины идти: '))
print(dijkstra_vertexes(g, s))
