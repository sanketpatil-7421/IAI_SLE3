# SLE-3: Architectural Design using Full C4 Model

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Student:** Sanket Subhash Patil  
**System:** BFS and DFS Graph Search System  
**Language:** Python  
**SLE:** 3 – Full C4 Architecture Design

## 1. Aim

To design and document the BFS/DFS graph-search system using all four levels of the C4 Model: Context, Container, Component, and Code.

This SLE-3 continues the BFS/DFS work from SLE-2. The provided guideline recommends continuing the same Search/Maze/Agent system and showing its complete architecture at all four C4 levels.

## 2. System Description

The system accepts a graph and a starting vertex from the user and performs Breadth First Search (BFS) and Depth First Search (DFS). BFS explores vertices level by level using a queue, while DFS explores a branch deeply before backtracking. The system displays the traversal order so that the user can compare the two search strategies.

The graph used in the previous SLE-2 work is:

```text
A -> B, C
B -> A, D, E
C -> A, F, G
D -> B
E -> B
F -> C
G -> C
```

## 3. C4 Model

The C4 model has four levels: Context, Container, Component and Code. All four levels are covered in this repository.

### Level 1 – Context

Shows the complete BFS/DFS system and the external user.

See: [`c4_context.md`](c4_context.md)

### Level 2 – Container

The system is divided into five main containers:

1. Input Module
2. Graph Manager
3. Search Engine
4. Visited/Queue/Stack Manager
5. Output Module

See: [`c4_container.md`](c4_container.md)

### Level 3 – Component

The important **Search Engine** container is decomposed into:

- BFS Traversal
- DFS Traversal
- Start Vertex Validator
- Traversal Controller

See: [`c4_component.md`](c4_component.md)

### Level 4 – Code

The code-level view lists the main functions and their responsibilities without including large source code.

See: [`c4_code.md`](c4_code.md)

## 4. Implementation

- `bfs_dfs.py` – BFS and DFS implementation.
- `graph.svg` – graph visualization.

## 5. Design Decisions

- BFS and DFS are kept inside one Search Engine because both solve the same graph traversal problem.
- The graph representation is kept separate from traversal logic so both algorithms can operate on the same input graph.
- Visited tracking prevents repeated processing of vertices.
- Input and output are separated from search logic to keep the architecture simple and readable.

## 6. AI Contribution Note

**AI tools used:** ChatGPT  
**What AI helped with:** Structuring the C4 architecture, drafting concise explanations, README organization, and checking that the repository covers Context → Container → Component → Code.  
**What I did myself:** Selected the BFS/DFS system, used the graph from the previous SLE work, reviewed the architecture, and verified the Python implementation and traversal logic.

## 7. Files

| File | Purpose |
|---|---|
| `README.md` | Project overview and C4 documentation |
| `CONTRIBUTION_LOG.md` | Contribution/work log |
| `c4_context.md` | Level 1 – Context diagram |
| `c4_container.md` | Level 2 – Container diagram |
| `c4_component.md` | Level 3 – Component diagram |
| `c4_code.md` | Level 4 – Code-level overview |
| `bfs_dfs.py` | BFS and DFS implementation |
| `graph.svg` | Graph visualization |

## 8. Conclusion

The C4 model makes the BFS/DFS system easier to understand from a high-level user view down to individual functions. The four levels show who interacts with the system, its main containers, the internal parts of the search engine, and the important code functions.
