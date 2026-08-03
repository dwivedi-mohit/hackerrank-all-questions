# Watson and DAG

---

| Field | Value |
|---|---|
| **Slug** | `watson-and-dag` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 65 |
| **Contest** | 101hack47 |
| **URL** | https://www.hackerrank.com/challenges/watson-and-dag |

---

## Preview

Help Watson solve a DAG problem.

## Problem Statement

Watson is excited about [directed acyclic graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG). Today he's learning how to [topologically sort](https://en.wikipedia.org/wiki/Topological_sorting) a DAG. He has written his own version of the algorithm, with a single parameter $k$, as follows:


```c++
// Notes:
// n is the number of nodes
// the nodes are indexed 0, 1, ... n-1.
// "[]" denotes an empty array.
// "{}" denotes an empty set.
// "x.append(v)" appends "v" at the end of array "x".

// k is a natural number.
def TopoSort(k):
    ans = []        // array which will contain the output
    in_deg = []     // in_deg[i] denotes the number of incoming edges at node i
    open_nodes = {} // a set of nodes
  

    // initialize "in_deg"
    for i = 0 to n-1:
        in_deg.append(0)
  

    for each edge (u -> v):
        in_deg[v]++
  

    // add nodes with indegree 0 to the set
    for i = 0 to n-1:
        if in_deg[i] == 0:
            open_nodes.add(i)
          

    while open_nodes is not empty:
        p = min(k, open_nodes.size())
        u = (the p^th smallest value from open_nodes)
        remove u from open_nodes
      

        ans.append(u)
      

        for each edge (u -> v) that begins at node u:
            in_deg[v]--
            if in_deg[v] == 0:
                open_nodes.add(v)
      

    return ans
```

This algorithm correctly computes a *topological ordering* of the DAG for any positive $k$. For two given topological orderings $a = [a_0, a_1, \ldots, a_{n-1}]$ and $b = [b_0, b_1, \ldots, b_{n-1}]$, we define the $\textrm{LCP}(a,b)$ as the length of the *longest common prefix* of $a$ and $b$. We can formally define it as the maximum value $i$ such that $i \le n$ and $a_j = b_j$ for all $0 \le j < i$. 


Here are three examples showing the common prefix in red:

$$\begin{array}{c|ccc}
 & \text{Example 1} & \text{Example 2} & \text{Example 3} \\\
\hline
a & [\mathbf{\color{red}{1,3,0}},4,2,5] & [\mathbf{\color{red}{0,1,3,2,4,5}}] & [1,0,3,4,2,5] \\\
b & [\mathbf{\color{red}{1,3,0}},5,2,4] & [\mathbf{\color{red}{0,1,3,2,4,5}}] & [0,3,1,4,2,5] \\\
\textrm{LCP}(a,b) & 3 & 6 & 0 \\\
\end{array}$$

Watson has a DAG with $n$ nodes numbered from $0$ to $n-1$ and $m$ edges, and Watson wants to compute the sum $\sum_{i=1}^{n} \sum_{j=1}^{n} \textrm{LCP}(\textrm{TopoSort}(i), \textrm{TopoSort}(j))$. For an explanation of a double series, refer to [this](http://mathworld.wolfram.com/DoubleSeries.html).

## Input Format

The first line contains two space-separated integers $n$ (the number of nodes), and $m$  (the number of edges). 


The next $m$ lines each contain two space-separated integers $u$ and $v$ denoting a directed edge from node $u$ to node $v$.

## Output Format

Print a single integer denoting the answer.

## Constraints

- $1 \le n \le 5\times 10^5$ 

- $1 \le m \le 10^6$   

- $m \le \frac{n(n-1)}{2}$  

- $0 \le u, v < n$
- There are no cycles.
- Each edge appears at most once.

**Subtasks** 


For $\text{40%}$ of the maximum score,

- $1 \le n \le 10^3$
- $1 \le m \le 10^5$

## Sample Tests

### Test 1

```
// Notes:
// n is the number of nodes
// the nodes are indexed 0, 1, ... n-1.
// "[]" denotes an empty array.
// "{}" denotes an empty set.
// "x.append(v)" appends "v" at the end of array "x".
// k is a natural number.
def
TopoSort
(
k
)
:
ans
=
[]
// array which will contain the output
in_deg
=
[]
// in_deg[i] denotes the number of incoming edges at node i
open_nodes
=
{}
// a set of nodes
// initialize "in_deg"
for
i
=
0
to
n
-
1
:
in_deg
.
append
(
0
)
for
each
edge
(
u
->
v
)
:
in_deg
[
v
]
++
// add nodes with indegree 0 to the set
for
i
=
0
to
n
-
1
:
if
in_deg
[
i
]
==
0
:
open_nodes
.
add
(
i
)
while
open_nodes
is
not
empty
:
p
=
min
(
k
,
open_nodes
.
size
())
u
=
(
the
p
^
th
smallest
value
from
open_nodes
)
remove
u
from
open_nodes
ans
.
append
(
u
)
for
each
edge
(
u
->
v
)
that
begins
at
node
u
:
in_deg
[
v
]
--
if
in_deg
[
v
]
==
0
:
open_nodes
.
add
(
v
)
return
ans
```

### Test 2

```
4 4
0 1
2 3
1 3
0 2
```

### Test 3

```
46
```
