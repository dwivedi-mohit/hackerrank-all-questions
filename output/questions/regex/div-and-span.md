# Div and Span

- **Domain:** regex
- **Difficulty:** Medium
- **Max Score:** 70
- **Success Ratio:** 0.91875
- **Total Submissions:** 160
- **Solved Count:** 147
- **URL:** https://www.hackerrank.com/challenges/div-and-span

## Problem Statement

Maya is teaching Alex about HyperText Markup Language ([HTML](https://en.wikipedia.org/wiki/HTML)). Alex is confused about *div* and *span* tags, so Maya decides to reduce the concept to a simpler visual by representing *div* tags as square brackets and *span* tags as parentheses. In other words, she represents `<div>` as `[`, `</div>` as `]`, `<span>` as `(`, and `</span>` as `)`.

 We use the following rules to determine the validity of a configuration:

1. The empty string (""), a single pair of square brackets `[]`, and single pair of parentheses `()` are all considered to be valid configurations. We can express each of these as $V$.
2. A valid configuration, $V$, which *does not contain* square brackets is called a *normal* configuration, which we can express as $N$. For example, `()` is *normal*.
3. Two or more consecutive valid configurations (e.g., $VV$) also constitute a valid configuration. For example, `[][]`, `()()`, and `[]()[]` are all valid.
4. The following configurations are also valid: `[V]`, `(N)`. 	
	For example, `[[(())]()]`, `((()))`, and `[(())[]]` are all valid; however, `([])` is *not valid* (you cannot nest a *div* tag inside a *span* tag).

Given some number of distinguishable square brackets, $X$, and some number of distinguishable parentheses, $Y$, how many valid configurations can we build using the above rules? As this answer can be very large, print it modulo $10^9+7$.


## Input Format

The first line contains a single positive integer, $T$, denoting the number of test cases. 		
Each of the $T$ subsequent lines contains $2$ positive space-separated integers describing the respective values of $X$ (the number of distinguishable square brackets) and $Y$ (the number of distinguishable parentheses).

## Output Format

For each test case, print the number of different valid configurations modulo $10^9+7$.

## Constraints

* $1 \leq T \leq 1000$
* $1 \leq X \leq 10^5$
* $1 \leq Y \leq 200$

## Sample Input

1 1
1 2
2 2

## Sample Output

18
160

## Explanation

For the first test case, , , these are  valid configurations:

- []()

- ()[]

- [()]

Thus, we print the result of  on the first line.

For the second test case, if brackets and parentheses were not distinguishable, we would have only  different configurations:

[()]() []()() [](())
()[]() [()()] [(())]
()()[] ()[()] (())[]

However, they are distinguishable, so [](1)(2) is not same as [](2)(1) (where (1) and (2) are the respective first and second pairs of parentheses. For this reason, we have  possible configurations and print the result of  on a new line.
