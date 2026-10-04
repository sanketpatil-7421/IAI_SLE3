# C4 Level 4 – Code Level Overview

The code level shows the main Python functions only. Large source-code blocks are intentionally not included.

| Code element | Responsibility |
|---|---|
| `build_graph()` | Creates or stores the graph adjacency representation. |
| `bfs(graph, start)` | Performs Breadth First Search using a queue. |
| `dfs(graph, start)` | Performs Depth First Search using recursion/stack. |
| `validate_start(graph, start)` | Checks whether the start vertex is present. |
| `display_result(order)` | Displays the traversal order. |
| `main()` | Controls input, algorithm selection and output. |

## Code Flow

```text
main()
  -> build_graph()
  -> validate_start()
  -> bfs() / dfs()
  -> display_result()
```
