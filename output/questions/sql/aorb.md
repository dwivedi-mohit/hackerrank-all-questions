# A or B

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7494110718492344
- **Total Submissions:** 3396
- **Solved Count:** 2545
- **URL:** https://www.hackerrank.com/challenges/aorb

## Problem Statement

Consider four numbers: $A$, $B$, $C$, and $K$. You must change *at most* $K$ bits in $A$ and $B$ to form the numbers $A'$ and $B'$ satisfying the equation $A'\ |\ B'  = C$. Here, the | symbol denotes the *bitwise OR* operation.

Given $Q$ sets of the numbers defined above, find and print the respective values of $A'$ and $B'$ on new lines; if no such value exists, print $-1$ instead. If there are multiple solutions, make $A'$ as small as possible; if there are still multiple solutions, make $B'$ as small as possible. 

**Notes:** 

* $A$, $B$, and $C$ are given in [Hexadecimal (base 16)](https://en.wikipedia.org/wiki/Hexadecimal), and $K$ is given in decimal (base 10).
* If the number of bits changed in $A$ is $k_{a}$ and the number of bits changed in B is $k_{b}$, then $k_{a}+k_{b}$ must be $\le K$.

## Input Format

The first line contains an integer, $Q$, denoting the number of queries. The subsequent lines describe each respective query as follows:
	
- The first line contains a single integer denoting the value of $K$.
- Each of the next $3$ lines contains a [Hexadecimal (base 16)](https://en.wikipedia.org/wiki/Hexadecimal) number describing the respective values of $A$, $B$, and $C$.

## Output Format

Print two lines of output for each query:

1. The first line should contain a [Hexadecimal (base 16)](https://en.wikipedia.org/wiki/Hexadecimal) number denoting the value of $A'$.
2. The second line must contain a [Hexadecimal (base 16)](https://en.wikipedia.org/wiki/Hexadecimal) number denoting the value of $B'$. 

If no valid answer exists, you must instead print one line of output with the integer $-1$.

**Note**: The letters in Hexadecimal numbers must be in uppercase.

## Constraints

* $1 \le Q \le 5$
* $0 \le K \le 5 \times 10^5$
* $0 \lt A, B, C \lt 16^{5 \times 10^4}$



## Sample Input

8
2B
9F
58
5
B9
40
5A
2
91
BE
A8

## Sample Output

58
18
42
-1

## Explanation

Query 0:

In this query, .

Change  to .  bits are changed.

Change B =  to .  bits are changed.

Query 1:

In this query, .

Change  to .  bits are changed.

Change  to . Only  bit is changed.

Query 2:

There is no valid answer, so we print .
