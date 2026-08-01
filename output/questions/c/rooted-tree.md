# Rooted Tree

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 150
- **Success Ratio:** 0.8146201624462494
- **Total Submissions:** 2093
- **Solved Count:** 1705
- **URL:** https://www.hackerrank.com/challenges/rooted-tree

## Problem Statement

You are given a rooted [tree](http://en.wikipedia.org/wiki/Tree_(graph_theory)) with _N_ nodes and the root of the tree, _R_, is also given. Each node of the tree contains a value, that is initially empty. You have to mantain the tree under two operations:

1. Update Operation
2. Report Operation

**Update Operation**  
Each Update Operation begins with the character `U`. Character `U` is followed by 3 integers _T, V and K_. For every node which is the descendent of the node _T_, update it's value by adding _V + d\*K_, where _V_ and _K_ are the parameters of the query and _d_ is the distance of the node from _T_. Note that _V_ is added to node _T_.  

**Report Operation**  
Each Report Operation begins with the character `Q`. Character `Q` is followed by 2 integers, _A_ and _B_. Output the sum of values of nodes in the path from _A_ to _B_ modulo _(10<sup>9</sup> + 7)_  

**Input Format**  
The first Line consists of 3 space separated integers, _N E R_, where _N_ is the number of nodes present, _E_ is the total number of queries (update + report), and _R_ is root of the tree.  

Each of the next _N-1_ lines contains 2 space separated integers, _X_ and _Y_ (_X_ and _Y_ are connected by an edge).

Thereafter, _E_ lines follows: each line can represent either the Update Operation or the Report Operation.<br>

- _Update Operation_ is of the form : _U T V K_.
- _Report Operation_ is of the form : _Q A B_.

**Output Format**  
Output the answer for every given report operation.

**Constraints**  

1 &le; N, E &le; 10<sup>5</sup>  
1 &le; E &le; 10<sup>5</sup>  
1 &le; R, X, Y, T, A, B &le; N  
1 &le; V, K &le; 10<sup>9</sup>  
X &ne; Y

**Sample Input**

    7 7 1
    1 2
    2 3
    2 4
    2 5
    5 6
    6 7
    U 5 10 2
    U 4 5 3
    Q 1 7
    U 6 7 4
    Q 2 7
    Q 1 4
    Q 2 4

**Sample Output**

    36
    54
    5
    5

**Explanation**  

- Values of Nodes after `U 5 10 2`: `[0 0 0 0 10 12 14]`.
- Values of Nodes after `U 4 5 3`: `[0 0 0 5 10 12 14]`. 
- Sum of the Nodes from 1 to 7: 0 + 0 + 10 + 12 + 14 = 36.
- Values of Nodes after `U 6 7 4`: [0 0 0 5 10 19 25].  
- Sum of the Nodes from 2 to 7: 0 + 10 + 19 + 25 = 54. 
- Sum of the Nodes from 1 to 4: 0 + 0 + 5 = 5.
- Sum of the Nodes from 2 to 4: 0 + 5 = 5.

## Input Format

The first Line consists of 3 space separated integers, N E R, where N is the number of nodes present, E is the total number of queries (update + report), and R is root of the tree.

Each of the next N-1 lines contains 2 space separated integers, X and Y (X and Y are connected by an edge).

Thereafter, E lines follows: each line can represent either the Update Operation or the Report Operation.

- Update Operation is of the form : U T V K.

- Report Operation is of the form : Q A B.

## Output Format

Output the answer for every given report operation.

## Constraints

1 ≤ N, E ≤ 105

1 ≤ E ≤ 105

1 ≤ R, X, Y, T, A, B ≤ N

1 ≤ V, K ≤ 109

X ≠ Y

## Sample Input

7 7 1
1 2
2 3
2 4
2 5
5 6
6 7
U 5 10 2
U 4 5 3
Q 1 7
U 6 7 4
Q 2 7
Q 1 4
Q 2 4

## Sample Output

54
5
5

## Explanation

- Values of Nodes after U 5 10 2: [0 0 0 0 10 12 14].

- Values of Nodes after U 4 5 3: [0 0 0 5 10 12 14].

- Sum of the Nodes from 1 to 7: 0 + 0 + 10 + 12 + 14 = 36.

- Values of Nodes after U 6 7 4: [0 0 0 5 10 19 25].

- Sum of the Nodes from 2 to 7: 0 + 10 + 19 + 25 = 54.

- Sum of the Nodes from 1 to 4: 0 + 0 + 5 = 5.

- Sum of the Nodes from 2 to 4: 0 + 5 = 5.
