# Filter Elements

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.8294817927170869
- **Total Submissions:** 2856
- **Solved Count:** 2369
- **URL:** https://www.hackerrank.com/challenges/filter-elements

## Problem Statement


Given a list of _N_ integers _A = [a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>N</sub>]_, you have to find those integers which are repeated at least _K_ times. In case no such element exists you have to print `-1`.  

If there are multiple elements in _A_ which are repeated at least _K_ times, then print these elements ordered by their first occurrence in the list.  

Let's say _A = [4, 5, 2, 5, 4, 3, 1, 3, 4]_ and _K = 2_. Then the output is

    4 5 3

because these numbers have appeared at least 2 times.  
Among these numbers,   
_4_ has appeared first at position _1_,  
_5_ has appeared next at position _2_,  
and _3_ has appeared thereafter at position _6_.  
That's why, we print in the order _4_, _5_ and finally _3_.

**Input**  
First line contains an integer, _T_, the number of test cases. Then _T_ test cases follow.  
Each test case consist of two lines. First line will contain two space separated integers, _N_ and _K_, where _N_ is the size of list _A_, and _K_ represents the repetition count. In the second line, there are _N_ space separated integers which represent the elements of list _A = [a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>N</sub>]_.

**Output**  
For each test case, you have to print all those integers which have appeared in the list at least _K_ times in the order of their first appearance, separated by space. If no such element exists, then print `-1`.

**Constraints**  
1 <= _T_ <= 10  
1 <= _N_ <= 10000  
1 <= _K_ <= N  
1 <= _a<sub>i</sub>_ <= 10<sup>9</sup>  

**Sample Input**

    3
    9 2
    4 5 2 5 4 3 1 3 4
    9 4
    4 5 2 5 4 3 1 3 4
    10 2
    5 4 3 2 1 1 2 3 4 5

**Sample Output**

    4 5 3
    -1
    5 4 3 2 1

**Explanation**  
*Sample Case #01:* This is the same example mentioned in the problem statement above.  
*Sample Case #02:* As no elements repeats more than 3 times, we don't have any elements satisfying the criteria of minimum _K_ times.  
*Sample Case #03:* All elements are repeated 2 times. So we print all of them according to their order of occurance, which is 5 -> 4 -> 3 -> 2 -> 1.


## Constraints

1 <= T <= 10

1 <= N <= 10000

1 <= K <= N

1 <= ai <= 109

## Sample Input

9 2
4 5 2 5 4 3 1 3 4
9 4
4 5 2 5 4 3 1 3 4
10 2
5 4 3 2 1 1 2 3 4 5

## Sample Output

4 5 3
-1
5 4 3 2 1

## Explanation

Sample Case #01: This is the same example mentioned in the problem statement above.

Sample Case #02: As no elements repeats more than 3 times, we don't have any elements satisfying the criteria of minimum K times.

Sample Case #03: All elements are repeated 2 times. So we print all of them according to their order of occurance, which is 5 -> 4 -> 3 -> 2 -> 1.
