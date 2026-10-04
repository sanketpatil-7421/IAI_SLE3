# C4 Level 2 – Container Diagram

## BFS and DFS Graph Search System

```mermaid
flowchart LR
    U[User]
    I[Input Module]
    G[Graph Manager]
    S[Search Engine]
    M[Visited / Queue / Stack Manager]
    O[Output Module]

    U -->|Graph + start vertex| I
    I --> G
    G --> S
    S <--> M
    S --> O
    O -->|Traversal result| U
```

## Container Responsibilities

| Container | Responsibility |
|---|---|
| Input Module | Accepts graph, starting vertex and search choice from the user. |
| Graph Manager | Stores and provides the graph/adjacency representation. |
| Search Engine | Runs BFS or DFS according to the selected search method. |
| Visited / Queue / Stack Manager | Maintains visited vertices and the data structures required during traversal. |
| Output Module | Formats and displays the BFS/DFS traversal result. |

The design uses five containers, keeping the diagram within the recommended 4–7 boxes for readability.
