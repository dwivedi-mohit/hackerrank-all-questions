# Synchronous Shopping

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.681894437991999
- **Total Submissions:** 7749
- **Solved Count:** 5284
- **URL:** https://www.hackerrank.com/challenges/synchronous-shopping

## Problem Statement

Bitville is a seaside city that has a number of shopping centers connected by bidirectional roads, each of which has a travel time associated with it.  Each of the shopping centers may have a fishmonger who sells one or more kinds of fish.  Two cats, *Big Cat* and *Little Cat*, are at shopping center $1$ (each of the centers is numbered consecutively from $1$ to $n$).  They have a list of fish they want to purchase, and to save time, they will divide the list between them.  Determine the total travel time for the cats to purchase all of the types of fish, finally meeting at shopping center $n$.  Their paths may intersect, they may backtrack through shopping center $n$, and one may arrive at a different time than the other.  The minimum time to determine is when both have arrived at the destination.  

For example, there are $n = 5$ shopping centers selling $k = 3$ types of fish.  The following is a graph that shows a possible layout of the shopping centers connected by $m = 4$ paths.  Each of the centers is labeled $\texttt{center number/fish types offered/cat(s) that visit(s)}$.  Here $B$ and $L$ represent *Big Cat* and *Little Cat*, respectively.  In this example, both cats take the same path, i.e. $1 \rightarrow 3 \rightarrow 5$ and arrive at time $15 + 5 = 20$ having purchased all three types of fish they want.  Neither cat visits shopping centers $2$ or $4$.  



![image](https://s3.amazonaws.com/hr-assets/0/1544041107-a20059b5a2-SynchronousShoppingExample.png)   

[//]: # (Bitville is a seaside city that has $N$ shopping centers connected via $M$ bidirectional roads. Each road connects exactly two distinct shopping centers and has a travel time associated with it.)

[//]: # (There are $K$ different types of fish sold in Bitville. Historically, any shopping center has a fishmonger selling certain types of fish. Buying any amount of fish from any fishmonger takes no time. )

[//]: # (Our heroes, *Big Cat* and *Little Cat*, are standing at Bitville shopping center number $1$. They have a list of the types of fish sold at each fishmonger, and they want to collectively purchase all $K$ types of fish in a minimal amount of time. To do this, they decide to split the shopping between themselves in the following way:)

[//]: # (- Both cats choose their own paths, starting at shopping center $1$ and ending at shopping center $N$. It should be noted that Little Cat's path is not necessarily the same as Big Cat's.)
[//]: # (- While traveling their respective paths, each cat will buy certain types of fish at certain shops. )
[//]: # (- When the cats reach shopping center $N$, they must have collectively purchased all $K$ types of fish in a minimal amount of time. )
[//]: # (- If one cat finishes shopping before the other, he waits at shopping center $N$ for his partner to finish; this means that the total shopping time is the maximum of Little and Big Cats' respective shopping times.)

[//]: # (It is to be noted that any of the cats can visit the shopping center $N$ in between, but they both *have* to finish their paths at the shopping center $N$.)

[//]: # (Given the layout for Bitville and the list of fish types sold at each fishmonger, what is the minimum amount of time it will take for Big and Little Cat to purchase all $K$ types of fish and meet up at shopping center $N$?")

**Function Description**  

Complete the *shop* function in the editor below.  It should return an integer that represents the minimum time required for their shopping.  

shop has the following parameters:  
- *n*: an integer, the number of shopping centers  
- *k*: an integer, the number of types of fish  
- *centers*: an array of strings of space-separated integers where the first integer of each element is the number of types of fish sold at a center and the remainder are the types sold  
- *roads*: a 2-dimensional array of integers where the first two values are the shopping centers connected by the bi-directional road, and the third is the travel time for that road  

## Input Format

The first line contains $3$ space-separated integers: $n$ (the number of shopping centers), $m$ (the number of roads), and $k$ (the number of types of fish sold in Bitville), respectively.		

Each line $i$ of the $n$ subsequent lines ($1 \le i \le n$) describes a shopping center as a line of space-separated integers. Each line takes the following form:

- The first integer, $t[i]$, denotes the number of types of fish that are sold by the fishmonger at the $i^{th}$ shopping center.
- Each of the $t[i]$ subsequent integers on the line describes a type of fish sold by that fishmonger, denoted by $A[i][z]$, where $1 \leq z \leq t[i]$ going forward.

Each line $j$ of the $m$ subsequent lines ($1 \le j \le m$) contains $3$ space-separated integers that describe a road. The first two integers, $u[j]$ and $v[j]$, describe the two shopping centers it connects. The third integer, $w[j]$, denotes the amount of time it takes to travel the road.

## Output Format

Print the minimum amount of time it will take for the cats to collectively purchase all $k$ fish and meet up at shopping center $n$.

## Constraints

* $2 \leq n \leq 10^3$
* $1 \leq m \leq 2 \times 10^3$
* $1 \leq k \leq 10$
* $0 \leq t[i] \leq k$
* $1 \leq A[i][z] \leq k$
* All $A[i][z]$ are different for every fixed $i$.
* $1 \leq u[j], v[j] \leq N$
* $1 \leq w[j] \leq 10^4$
* Each road connectes $2$ distinct shopping centers (i.e., no road connects a shopping center to itself).
* Each pair of shopping centers is directly connected by no more than $1$ road.
* It is possible to get to any shopping center from any other shopping center.
* Each type of fish is always sold by at least one fishmonger.

## Sample Input

5 5 5
1 1
1 2
1 3
1 4
1 5
1 2 10
1 3 10
2 4 10
3 5 10
4 5 10

## Explanation

represents a location Big Cat visits,  represents a location where Little Cat visits.

Big Cat can travel  and buy fish at all of the shopping centers on his way.

Little Cat can then travel , and buy fish from the fishmonger at the  shopping center only.
