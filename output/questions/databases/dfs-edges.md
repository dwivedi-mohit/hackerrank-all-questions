# DFS Edges

- **Domain:** databases
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8054768649669499
- **Total Submissions:** 2118
- **Solved Count:** 1706
- **URL:** https://www.hackerrank.com/challenges/dfs-edges

## Problem Statement

Let $G$ be a connected, directed graph with vertices numbered from $1$ to $n$ such that any vertex is reachable from vertex $1$. In addition, any two distinct vertices, $u$ and $v$, are connected by *at most* one edge $(u, v)$.

Consider the standard *DFS* (Depth-First Search) algorithm starting from vertex $1$. As every vertex is reachable, each edge $(u, v)$ of $G$ is classified by the algorithm into one of four groups:

1. *tree edge*: If $v$ was discovered for the first time when we traversed $(u, v)$.
2. *back edge*: If $v$ was already on the stack when we tried to traverse $(u, v)$.
3. *forward edge*: If $v$ was already discovered *while* $u$ was on the stack.
4. *cross edge*: Any edge that is not a *tree*, *back*, or *forward* edge.

To better understand this, consider the following C++ pseudocode:

```cpp
// initially false
bool discovered[n]; 

// initially false
bool finished[n];   

vector<int> g[n];

void dfs(int u) {
    // u is on the stack now
    discovered[u] = true;
    for (int v: g[u]) {
        if (finished[v]) {
            // forward edge if u was on the stack when v was discovered
            // cross edge otherwise
            continue;
        }
        if (discovered[v]) {
            // back edge
            continue;
        }
        // tree edge
        dfs(v);
    }
    finished[u] = true;
    // u is no longer on the stack
}
```

Given four integers, $t$, $b$, $f$, and $c$, construct any graph $G$ having exactly $t$ *tree edges*, exactly $b$ *back edges*, exactly $f$ *forward edges*, and exactly $c$ *cross edges*. Then print $G$ according to the *Output Format* specified below.

## Input Format

A single line of four space-separated integers describing the respective values of $t$, $b$, $f$, and $c$.

## Output Format

If there is no such graph $G$, print `-1`; otherwise print the following:

1. The first line must contain an integer, $n$, denoting the number of vertices in $G$.
2. Each line $i$ of the $n$ subsequent lines must contain the following space-separated integers:
	- The first integer is the [outdegree](https://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree), $d_i$, of vertex $i$.
    - This is followed by $d_i$ distinct numbers, $v_{i,j}$, denoting edges from $u$ to $v_{i,j}$ for $1 \le j \le d_i$. The order of each $v_{i,j}$ should be the order in which a *DFS* considers edges.

## Constraints

- $0 \le t, b, f, c \le 10^5$

## Sample Input

3 1 1 1

## Sample Output

4
3 2 4 3
1 3
1 1
1 2

## Explanation

The DFS traversal order is: . Thus, ,  and  are tree edges;  is a back edge;  is a forward edge; and  is a cross edge. This is demonstrated by the diagram below, in which tree edges are black, forward edges are blue, back edges are red, and cross edges are green.
