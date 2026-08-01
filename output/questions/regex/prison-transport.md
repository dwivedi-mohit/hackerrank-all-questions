# Prison Transport

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7556053811659192
- **Total Submissions:** 892
- **Solved Count:** 674
- **URL:** https://www.hackerrank.com/challenges/prison-transport

## Problem Statement

There are *N* inmates numbered between _[1, N]_ in a prison. These inmates have superhuman strength because they have drunk a special concoction made by Dr. Evil. They have to be transported by some buses to a new facility. But they are bound by special chains which are made from strong carbon fibres. Each inmate is either chained alone or is chained in a group along with one or more inmates. A group of inmates are those who are directly or indirectly connected to each other. Only one group can be transported per bus.  

There are buses which will charge fixed amount bucks for transferring inmates. Charges are directly proportional to the capacity of bus. If a bus charge _K_ bucks then it can carry upto _K<sup>2</sup>_ inmates at one time. Buses are available for all positive integral cost ranging from _[1, 2, 3, ...]_. A bus can be used multiple times, and each time it will charge. Note that a bus can *also* transfer less number of inmates than it's capacity.  

Find the minimal cost to transport all the inmates.

**Input**  
The first line contains *N* representing the number of inmates. Second line contains another integer, _M_, number of pairs of inmates who are handcuffed together. Then follows _M_ lines. Each of these lines contains two integers, _P Q_, which means inmate numbered _P_ is handcuffed to inmate numbered _Q_.  

**Output**  
For the given arrangement, print the minimal cost which can be incurred while transferring inmates.

**Constraints**  
2 &le; *N* &le; 100000  
1 &le; *M* &le; min(N\*(N-1)/2, 100000)  
1 &le; *P, Q* &le; N  
*P* &ne; _Q_  


**Sample Input**

    4
    2
    1 2
    1 4
    
**Sample Output**  

	3
    
**Explanation**  
Inmates _#1_, _#2_, _#4_ are connected to each other (`1--2--4`) so they lies in a single group. So a bus of cost _2_ (with capacity 2<sup>2</sup> = 4) is required to carry them. Inmate #3 is not handcuffed with anyother. So he can be transported in a bus of cost 1 (with capacity 1<sup>2</sup> = 1).


## Constraints

2 ≤ N ≤ 100000

1 ≤ M ≤ min(N*(N-1)/2, 100000)

1 ≤ P, Q ≤ N

P ≠ Q

## Sample Input

2
1 2
1 4

## Explanation

Inmates #1, #2, #4 are connected to each other (1--2--4) so they lies in a single group. So a bus of cost 2 (with capacity 22 = 4) is required to carry them. Inmate #3 is not handcuffed with anyother. So he can be transported in a bus of cost 1 (with capacity 12 = 1).
