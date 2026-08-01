# Alex vs Fedor

- **Domain:** databases
- **Difficulty:** Expert
- **Max Score:** 150
- **Success Ratio:** 0.8775448192038894
- **Total Submissions:** 3291
- **Solved Count:** 2888
- **URL:** https://www.hackerrank.com/challenges/alex-vs-fedor

## Problem Statement

In order to entertain themselves during the long flight, Alex and Fedor invented the following very simple two players game. The game is:  

- First, Alex draws some graph with bidirectional weighted edges. There are possibly multiple edges (probably, with different or same weights) in this graph.

- Then Fedor picks some spanning tree of this graph. If the tree appears to be the minimal spanning tree, then the winner is Fedor. Otherwise, the winner is Alex.  

We consider two trees different if the sets of the numbers of edges that are included in these trees are different. We consider two sets $A$ and $B$ different if there is at least one element that is present in $A$ and not present in $B$ or vice versa.  

We should also mention that the graphs with enormous number of spanning trees upset Alex, as well as Fedor, so they will never have a graph that has more than $10^{18}$ spanning trees.  

At some point, Fedor became too lazy to look for minimal spanning trees and now he just picks some arbitrary spanning tree from the Alex's graph. Each spanning tree has equal probability to be picked by Fedor. What is the probability of Fedor's victory now?   

## Input Format

The first line of input consists of two single space separated integers $N$ and $M$ - the number of nodes in Alex's graph and the number of edges in that graph, respectively.  

Then there are $M$ lines, where the $i^{th}$ line has three numbers $X_i \ Y_i \ Z_i$ with the meaning that the edge with the number $i$ connects the nodes $X_i$ and $Y_i$ and has the weight of $Z_i$.  

## Output Format

Output the probability of Fedor's victory, if he picks the spanning tree randomly, as an irreducible fraction.

## Constraints

- The graph is always connected.  
- $1 \le N, M \le 100$  
- $1 \le weight \lt 2^{31}$ 

## Sample Input

4 4
1 2 1
2 3 4
3 4 3
4 1 2

## Sample Output

1/4
