# adapted from https://gist.github.com/kachayev/5910538
from collections import deque
GRAY, BLACK = 0, 1


def topological(graph):
    order, enter, state = deque(), set(graph), {}

    dot = "digraph X {\r\n"
    for item in graph.keys():
        dep = graph[item]
        for d in dep:
            dot += item + " -> " + str(d) + '\r\n'
    dot += "}"
    print(dot)

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY:
                raise ValueError("cycle")
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        #order.appendleft(node)  # show highest to lowest
        order.append(node)  # show lowest to highest
        state[node] = BLACK
    while enter:
        dfs(enter.pop())
    return order


def main():
    graph = {
        '1': ['2'],
        '2': ['4'],
        '3': ['4'],
        '4': ['5', '6'],
        '6': ['7'],
    }
    try:
        print(topological(graph))
    except ValueError:
        print("Cycle!")


if __name__ == "__main__":
    main()
