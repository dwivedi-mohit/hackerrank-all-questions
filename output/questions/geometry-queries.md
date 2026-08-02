# Geometry Queries

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.5450236966824644
- **Total Submissions:** 211
- **Solved Count:** 115
- **URL:** https://www.hackerrank.com/challenges/geometry-queries

## Problem Statement

There are $N$ lines. Each line has an index between $1$ and $N$. The slope of each line is negative, i.e. it goes from upper-left to lower-right.

There are $Q$ queries. Each of them is in the format `L R x y`, and you should output whether there is any line with index between $L$ and $R$ and the point $(x, y)$ is under it. If there is, then the answer is `YES`, otherwise `NO`.

As you know, any line splits an infinite plane into two regions. The point $(x,y)$ is under the line if that point is at the same region with point $(-\infty, -\infty)$. If the point lies on the line it does not count.

**Input Format**  
The first line contains $N$, the number of lines. The following $N$ lines each contains two integers $m$ and $n$ that describes the line $mx + n = y$.  

The next line contains $Q$, the number of queries. Each subsequent line contains 4 integers $L, R, x, y$.  

**Output Format**  
For each query, output one line containing either `YES` or `NO`.  

**Constraints**  
$1 \leq  N \leq  10^5$ (Number of lines)  
$1 \leq  Q \leq  10^5$ (Number of queries)  
$-10^9 \leq  x \leq  10^9$  
$-10^9 \leq  y \leq  10^9$  
$-10^9 \leq  m < 0$  
$-10^9 \leq  n \leq  10^9$  
$1 \leq  L \leq  R \leq  N$  

**Sample Input**  

    2
    -1 3
    -2 -4
    3
    1 2 0 0
    1 1 0 0
    2 2 0 0

**Sample Output**  

    YES
    YES
    NO

**Explanation**   
The image shows the two lines of the sample input.

<a href="http://hizliresim.com/JEYqEQ"><img src="http://i.hizliresim.com/JEYqEQ.png" /></a>

<sub>Time Limits: C/C++ 1 sec, Java/C# 2 sec, other languages follow standard TL given in [Environment](https://hackerrank.com/environment)</sub>


## Input Format

The first line contains , the number of lines. The following  lines each contains two integers  and  that describes the line .

The next line contains , the number of queries. Each subsequent line contains 4 integers .

## Output Format

For each query, output one line containing either YES or NO.

## Constraints

(Number of lines)

 (Number of queries)

## Sample Input

-1 3
-2 -4
3
1 2 0 0
1 1 0 0
2 2 0 0

## Sample Output

YES
YES
NO

## Explanation

The image shows the two lines of the sample input.

Time Limits: C/C++ 1 sec, Java/C# 2 sec, other languages follow standard TL given in Environment

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
