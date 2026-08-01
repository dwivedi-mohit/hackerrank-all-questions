# Zombie March***

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.49863387978142076
- **Total Submissions:** 732
- **Solved Count:** 365
- **URL:** https://www.hackerrank.com/challenges/zombie-march

## Problem Statement

Zombies have placed themselves at every junction in Bucharest. Each junction 'i' initially has a presence of ai number of zombies. Every timestep, each zombie randomly chooses one of its neighboring junctions and walks towards it. Each neighboring junction is choosen by the zombie with an equal probability. In order to safegaurd the citizens of Bucharest we need to find out the expected number of zombies at every junction after 'k' timesteps. 

The network of Bucharest is given as an edge list.  

**Input Format**  

 - t - the number of test cases. 't' cases follow.
 - n, m, k - 'n' junctions (nodes) in Bucharest, 'm' roads (edges) and 'k' time steps. 
 - This is followed by m lines containing 1 edge on each line. Each edge is denoted by 2 integers representing the nodes it connects, which can range from 0 to n-1.  All the edges are bidirectional. A node cannot connect itself. 
 - This is followed by n lines, where the i<sup>th</sup> line contains the initial number of Zombies at the location ai.


**Output Format**  
Output the number of zombies (rounded of to its nearest integer) in the 5 most highly populated junctions after 'k' timesteps.


**Constraints**  
1<=t<=5

5<=n<=100000

1<=m<= 200000

1<=k<=10000000

1<=ai<=1000

 

**Sample Input**  

1

10 18 100

0 8 

0 5 

1 2 

1 5 

2 8 

2 4 

2 5 

2 6 

3 5 

4 8 

4 6 

4 7 

5 8 

5 9 

6 8 

6 9 

7 9 

8 9 

1

1

1

1

1

1

1

1

1

1

 

**Sample Output**  
2 2 1 1 1

## Input Format

- t - the number of test cases. 't' cases follow.

- n, m, k - 'n' junctions (nodes) in Bucharest, 'm' roads (edges) and 'k' time steps.

- This is followed by m lines containing 1 edge on each line. Each edge is denoted by 2 integers representing the nodes it connects, which can range from 0 to n-1.  All the edges are bidirectional. A node cannot connect itself.

- This is followed by n lines, where the ith line contains the initial number of Zombies at the location ai.

## Output Format

Output the number of zombies (rounded of to its nearest integer) in the 5 most highly populated junctions after 'k' timesteps.

## Constraints

1<=t<=5

5<=n<=100000

1<=m<= 200000

1<=k<=10000000

1<=ai<=1000

## Sample Input

10 18 100

0 8

0 5

1 2

1 5

2 8

2 4

2 5

2 6

3 5

4 8

4 6

4 7

5 8

5 9

6 8

6 9

7 9

8 9

1

1

1

1

1

1

1

1

1

1

## Sample Output

2 2 1 1 1
