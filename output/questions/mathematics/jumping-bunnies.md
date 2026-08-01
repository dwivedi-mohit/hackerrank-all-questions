# Jumping Bunnies

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.9049250535331905
- **Total Submissions:** 2335
- **Solved Count:** 2113
- **URL:** https://www.hackerrank.com/challenges/jumping-bunnies

## Problem Statement

Bunnies are very cute animals who likes to jump a lot. Every bunny has his own range of jump. Lets say there are $N$ bunnies and $i^{th}$ $(i \in [1, N])$ bunny jumps $j_i$ units. Consider a 1-D plane, where initially bunnies are at $0$. All of them starts jumping in forward direction.  

For example, consider the case of $k^{th}$ bunny. Initially he is at $0$. After first jump, he will be at point $j_k$. After second, he will be at $2 \times j_k$ and so on. After $m^{th}$ jump, he will be at point $m \times j_k$.

Two bunnies can only meet each other when they are on the ground. When on the ground, a bunny can wait any amount of time. Being a social animal, all of them decide to meet at the next point where *all* of them will be on the ground. You have to find the nearest point where all the bunnies can meet.  

For example, if there are $N = 3$ bunnies where $j_1 = 2$, $j_2 = 3$, $j_3 = 4$.   Nearest point where all bunnies can meet again is at $12$. First bunny has to jump six times, for second it is $4$ times and for third it is $3$ times.  

Help bunnies to find the nearest point where they can meet again.  

**Input Format**    
First line will contain an integer, $N$, represeting the number of bunnies. Second line will contain $N$ space separated integer, $j_1, j_2, \cdots, j_N$, representing the jumping distance of them.  

**Output Format**  
Print the nearest location where all bunnies can meet again. 

**Constraints**  
$2 \le N \le 10$  
$1 \le j_i \le 10^6$  
For each test case it is guaranteed that solution will not exceed $2 \times 10^{18}$.  

**Sample Input #00**  

    3
    2 3 4

**Sample Output #00**  

    12

**Sample Input #01**  

    2
    1 3

**Sample Output #01**  

    3

**Explanation**  
*Sample Case #00:* This is the same example mentioned in the statement above.  
*Sample Case #01:* First bunny has to jump $3$ times to point $3$, whereas second bunny has to jump only one time to go at point $3$. Point $3$ will serve as their meeting point.


## Input Format

First line will contain an integer, , represeting the number of bunnies. Second line will contain  space separated integer, , representing the jumping distance of them.

## Output Format

Print the nearest location where all bunnies can meet again.

## Constraints

For each test case it is guaranteed that solution will not exceed .

Sample Input #00

3
2 3 4

Sample Output #00

12

Sample Input #01

2
1 3

Sample Output #01

3

## Explanation

Sample Case #00: This is the same example mentioned in the statement above.

Sample Case #01: First bunny has to jump  times to point , whereas second bunny has to jump only one time to go at point . Point  will serve as their meeting point.
