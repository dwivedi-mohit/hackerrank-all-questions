# Bridges and Harbors

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.4129353233830846
- **Total Submissions:** 201
- **Solved Count:** 83
- **URL:** https://www.hackerrank.com/challenges/bridges-and-harbors

## Problem Statement

DestinyLand is a really fun place for kids. It is composed of _N_ islands, numbered from 1 to _N_. The company is planning to divide these _N_ islands into exactly _M_ area, such that, each island will belong to one of the _M_ areas, and each area will contain at least one island.

Now the company is going to build bridges between the islands. Each area should be isolated from another. So the bridges can be built, **only if** both the endpoint islands belong to the same area. That is, in total they will build exactly _n-m_ bridges to maintain connectivity within each area. (Of course, they won't build more than _N-M_  bridges because that cost too much!)

For area to area connections, the company planned to build a harbor to one chosen island in each area. Due to heavy traffic, each of the chosen islands should **NOT** directly connect with more than _K_ bridges. Can you help the company figure out how many bridge and harbor construction layouts are possible?

Note that all harbors are the same, all bridges are the same, but islands are distinct.

**Input Format**

The first line contains an integer _T_ indicating the number of test cases.  
For each test case, there are four space separated integers _N M K MOD_  

**Output Format**

For each test case, print the number of layouts modulo _MOD_

**Constraints**

1 &le; _T_ &le; 10  
1 &le; _N_ &le; 10<sup>9</sup>  
1 &le; _M_ , _K_ &le; min(_N_, 100)  
1 &le; _MOD_ &le; 2\*10<sup>9</sup>  

**Sample Input**

    3
    3 2 1 1000003
    3 1 2 1234567891
    3 1 1 314159

**Sample Output**

    6
    9
    6


## Input Format

The first line contains an integer T indicating the number of test cases.

For each test case, there are four space separated integers N M K MOD

## Output Format

For each test case, print the number of layouts modulo MOD

## Constraints

1 ≤ T ≤ 10

1 ≤ N ≤ 109

1 ≤ M , K ≤ min(N, 100)

1 ≤ MOD ≤ 2*109

## Sample Input

3 2 1 1000003
3 1 2 1234567891
3 1 1 314159

## Sample Output

9
6
