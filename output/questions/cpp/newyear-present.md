# New Year Present

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.6695108077360638
- **Total Submissions:** 1758
- **Solved Count:** 1177
- **URL:** https://www.hackerrank.com/challenges/newyear-present

## Problem Statement

Nina received an odd New Year's present from a student: a set of $n$ unbreakable sticks. Each stick has a length, $l$, and the length of the $i^{th}$ stick is $l_{i-1}$. Deciding to turn the gift into a lesson, Nina asks her students the following:

How many ways can you build a square using *exactly $6$* of these unbreakable sticks? 

*Note:* Two ways are distinct if they use at least one different stick. As there are [$\binom{n}{6}$](https://en.wikipedia.org/wiki/Binomial_coefficient) choices of sticks, we must determine which combinations of sticks can build a square.

  

## Input Format

The first line contains an integer, $n$, denoting the number of sticks.	The second line contains $n$ space-separated integers $l_0, l_1, \ldots, l_{n-2}, l_{n-1}$ describing the length of each stick in the set.




## Output Format

On a single line, print an integer representing the number of ways that $6$ unbreakable sticks can be used to make a square.

**Sample Input 0**

	8
    4 5 1 5 1 9 4 5 

**Sample Output 0**

    3
    
**Sample Input 1**

    6
    1 2 3 4 5 6 


**Sample Output 1**

    0    

## Constraints

* $6 \leq n \leq 3000 $
* $1 \leq l_i \leq 10^7 $

## Sample Input

8
4 5 1 5 1 9 4 5

## Sample Output

3

## Explanation

Sample 0

Given  sticks (), the only possible side length for our square is . We can build square  in  different ways:

-

-

-

In order to build a square with side length  using exactly  sticks,  and  must always build two of the sides. For the remaining two sides, you must choose  of the remaining  sticks of length  ( and ).

Sample 1

We have to use all  sticks, making the largest stick length () the minimum side length for our square. No combination of the remaining sticks can build  more sides of length  (total length of all other sticks is  and we need at least length ), so we print .
