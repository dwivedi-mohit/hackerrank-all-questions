# Yet Another KMP Problem

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.6606153846153846
- **Total Submissions:** 3250
- **Solved Count:** 2147
- **URL:** https://www.hackerrank.com/challenges/kmp-problem

## Problem Statement

This challenge uses the famous [KMP algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm). It isn't really important to understand how KMP works, but you should understand what it calculates.

A KMP algorithm takes a string, $S$, of length $N$ as input. Let's assume that the characters in $S$ are indexed from $1$ to $N$; for every prefix of $S$, the algorithm calculates the length of its longest valid [border](http://algorithmsforcontests.blogspot.com/2012/08/borders-of-string.html) in linear complexity. In other words, for every $i$ (where $1 \le i \le N$) it calculates the largest $l$ (where $0 \le l \le i-1$) such that for every $p$ (where $1 \le p \le l$) there is $S[p]=S[i-l+p]$.

Here is an implementation example of KMP:

```cpp
kmp[1] = 0;
for (i = 2; i <= N; i = i + 1){
    l = kmp[i - 1];
    while (l > 0 && S[i] != S[l + 1]){
        l = kmp[l];
    }
    if (S[i] == S[l + 1]){
        kmp[i] = l + 1;
    }
    else{
        kmp[i] = 0;
    }
}
```

Given a sequence $x_1,x_2, \ldots, x_{26}$, construct a string, $S$, that meets the following conditions:

1. The frequency of letter '$a$' in $S$ is exactly $x_1$, the frequency of letter '$b$' in $S$ is exactly $x_2$, and so on.
2. Let's assume characters of $S$ are numbered from $1$ to $N$, where $\sum\limits_{i=1}^n x_{i}=N$. We apply the KMP algorithm to $S$ and get a table, $kmp$, of size $N$. You must ensure that the sum of $kmp[i]$ for all $i$ is minimal.

If there are multiple strings which fulfill the above conditions, print the [lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) smallest one.



## Input Format

A single line containing $26$ space-separated integers describing sequence $x$. 

## Output Format

Print a single string denoting $S$.

## Constraints

- The sum of all $x_i$ will be a positive integer $\le 10^6$.

## Sample Input

2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

## Sample Output

aabb

## Explanation

The output string must have two '' and two ''. There are several such strings but we must ensure that sum of  for all  is minimal. See the figure below:

The minimum sum is . Among all the strings that satisfy both the condition, "aabb" is the lexicographically smallest.
