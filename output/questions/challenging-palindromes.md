# Build a Palindrome

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.6144667655386274
- **Total Submissions:** 14834
- **Solved Count:** 9115
- **URL:** https://www.hackerrank.com/challenges/challenging-palindromes

## Problem Statement

You have two strings, $a$ and $b$. Find a string, $s$, such that:

* $s$ can be expressed as $s =s_a + s_b$ where $s_a$ is a non-empty [substring](https://en.wikipedia.org/wiki/Substring) of $a$ and $s_b$ is a non-empty substring of $b$.
* $s$ is a [palindromic](https://en.wikipedia.org/wiki/Palindrome) string.
* The length of $s$ is as long as possible.

For each of the $q$ pairs of strings ($a_i$ and $b_i$) received as input, find and print string $s_i$ on a new line. If you're able to form more than one valid string $s_i$, print whichever one comes first alphabetically. If there is no valid answer, print $-1$ instead.

## Input Format

The first line contains a single integer, $q$, denoting the number of queries. The subsequent lines describe each query over two lines:

1. The first line contains a single string denoting $a$.
2. The second line contains a single string denoting $b$.

## Output Format

For each pair of strings ($a_i$ and $b_i$), find some $s_i$ satisfying the conditions above and print it on a new line. If there is no such string, print $-1$ instead.

## Constraints

* $1 \le q \le 10$  
* $1 \le |a|, |b| \le 10^5$  
* $a$ and $b$ contain only lowercase English letters.
* Sum of |a| over all queries does not exceed $2 \times 10^5$
* Sum of |b| over all queries does not exceed $2 \times 10^5$


## Sample Input

bac
bac
abc
def
jdfh
fds

## Sample Output

aba
-1
dfhfd

## Explanation

We perform the following three queries:

- Concatenate  with  to create .

- We're given  and ; because both strings are composed of unique characters, we cannot use them to form a palindromic string. Thus, we print .

- Concatenate  with  to create . Note that we chose these particular substrings because the length of string  must be maximal.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
