# Subset Sum

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.6491349480968858
- **Total Submissions:** 1445
- **Solved Count:** 938
- **URL:** https://www.hackerrank.com/challenges/subset-sum

## Problem Statement

You are given a list of _N_ positive integers, _A = {a[1], a[2], ..., a[N]}_ and another integer _S_. You have to find whether there exists a non-empty subset of _A_ whose sum is greater than or equal to _S_.  

You have to print the size of minimal subset whose sum is greater than or equal to S. If there exists no such subset then print `-1` instead.

**Input**  
First line will contain an integer, _N_, which is the size of list _A_. Second line contains _N_ space separated integers, representing the elements of list _A_. In third line there is an integer, _T_, which represent the number of test cases to follow. Then follows _T_ lines. Each one of them contains an single integer, _S_.  

**Output**  
For each test case, print the size of minimal subset whose sum is greater than or equal to _S_. If there's no such subset  then print `-1`.

**Constraints**  
1 &le; _N_ &le; 10<sup>5</sup>  
1 &le; a[i] &le; 10<sup>9</sup>  
1 &le; _T_ &le; 10<sup>5</sup>  
1 &le; _S_ &le; 10<sup>15</sup>  

**Note**  
Two subsets are different if there's an element _a[i]_ which exists in one of them and not in other. That is, for set `A = {4, 4}` there are four possible subsets `{}`, `{a[1]}`, `{a[2]}` and `{a[1], a[2]}`.  

**Sample Input**  

    4
    4 8 10 12
    4
    4
    13
    30
    100

**Sample Output**  

    1
    2
    3
    -1

**Explanation**  
*Sample Case #00:* For `S = 4`, we can select any one element of set _A_ as each of them is greater than or equal to 4.  
*Sample Case #01:* There are many possible subsets of size 2 whose sum is not less than _13_. They are `{4, 10}`, `{4, 12}`, `{8, 10}`, `{8, 12}` and `{10, 12}`.  
*Sample Case #02:* Subset `{8, 10, 12}`, with sum 30, is the only subset of size 3 whose sum is not less than `S = 30`.  
*Sample Case #03:* Even after selecting all the elements of _A_, we can't exceed `S = 100`.  


## Constraints

1 ≤ N ≤ 105

1 ≤ a[i] ≤ 109

1 ≤ T ≤ 105

1 ≤ S ≤ 1015

Note

Two subsets are different if there's an element a[i] which exists in one of them and not in other. That is, for set A = {4, 4} there are four possible subsets {}, {a[1]}, {a[2]} and {a[1], a[2]}.

## Sample Input

4 8 10 12
4
4
13
30
100

## Sample Output

2
3
-1

## Explanation

Sample Case #00: For S = 4, we can select any one element of set A as each of them is greater than or equal to 4.

Sample Case #01: There are many possible subsets of size 2 whose sum is not less than 13. They are {4, 10}, {4, 12}, {8, 10}, {8, 12} and {10, 12}.

Sample Case #02: Subset {8, 10, 12}, with sum 30, is the only subset of size 3 whose sum is not less than S = 30.

Sample Case #03: Even after selecting all the elements of A, we can't exceed S = 100.
