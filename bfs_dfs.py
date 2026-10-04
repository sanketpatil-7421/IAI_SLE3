from collections import deque


def build_graph():
    return {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
        "G": ["C"],
    }


def validate_start(graph, start):
    return start in graph


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def dfs(graph, start):
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def display_result(name, order):
    print(f"{name}: {' -> '.join(order)}")


def main():
    graph = build_graph()
    start = input("Enter starting vertex (A-G): ").strip().upper()

    if not validate_start(graph, start):
        print("Invalid starting vertex.")
        return

    display_result("BFS", bfs(graph, start))
    display_result("DFS", dfs(graph, start))


if __name__ == "__main__":
    main()
