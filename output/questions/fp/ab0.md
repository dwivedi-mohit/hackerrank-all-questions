# Divisibility

- **Domain:** fp
- **Difficulty:** Expert
- **Max Score:** 120
- **Success Ratio:** 0.6881918819188192
- **Total Submissions:** 2168
- **Solved Count:** 1492
- **URL:** https://www.hackerrank.com/challenges/ab0

## Problem Statement

Two positive integers $P$ and $S$ are given.  
$S = \overline{d_1 d_2 \dots d_N}$ is decimal representation of integer $S$.  
Lets define $f(l, r) = \overline{d_l d_{l + 1} \dots d_r}$.

For example, if $S = 9876$:  
$
d_1 = 9, d_2 = 8, d_3 = 7, d_4 = 6\\\\
f(2, 3) = \overline{d_2 d_3} = 87 \\\\
f(1, 3) = \overline{d_1 d_2 d_3} = 987 \\\\
f(4, 4) = \overline{d_4} = 6 \\\\
$

For each query you will be given two integers $b$ and $e$ that define a substring equal to $f(b, e)$.  
Your task is to calculate _divisibility_ of given substring.  
_Divisibility_ of given substring is equal to number of $(i, j)$ pairs such that:  
$b \le i \le j \le e$ and  
$f(i, j)$ is divisible by $P$, assuming that $0$ is divisible by any other integer.


**Timelimits**  

Timelimits for this challenge is given [here](http://hr-testcases.s3.amazonaws.com/4520/checkerlimits.json)

## Input Format

 First line contains two integers $P$ and $Q$ separated by a single space. $Q$ is the number of queries.  
Second line contains a big integer $S$.  
Next $Q$ lines contains two integers $b$ and $e$ separated by a single space each - begin and end points of substring.

**Constraints**  


$
2 \le P \le 10^9\\\\
1000 \le S < 10^{100\\,000}\\\\ 
1 \le Q \le 100\\,000\\\\
1 \le b \le e \le N
$


## Output Format

 Output $Q$ lines, the $i$-th line of the output should contain single integer  _divisibility_ of the $i$-th query substring.


## Sample Input

3 5
4831318
3 5
5 7
1 7
1 2
2 3

## Sample Output

3
9
1
1

## Explanation

In the first query, b = 3 and e = 5. Two such pairs that are divisible by P = 3 are
 f(3, 3) = 3 and f(5, 5). Hence the answer 2.

 In the second query, b = 5 and e = 7. Three such pairs that are divisible by P are
 F(5, 5) = 3, f(6, 7) = 18 and f(5, 7) = 318
