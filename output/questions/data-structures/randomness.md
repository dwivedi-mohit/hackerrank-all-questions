# Randomness

- **Domain:** data-structures
- **Difficulty:** Advanced
- **Max Score:** 120
- **Success Ratio:** 0.38811881188118813
- **Total Submissions:** 505
- **Solved Count:** 196
- **URL:** https://www.hackerrank.com/challenges/randomness

## Problem Statement

You're given a string $S$ of $N$ characters. It's known that the string consists of lowercase Latin letters. The string is generated randomly. That means that every symbol is chosen randomly and independently from others from the set {'a', 'b', ..., 'z'}. All the letters have equal probability to appear.

You're given $Q$ queries on this string. Each query is of the form `P C`, where $P$ is an integer between $1$ and $N$ (both inclusive) and $C$ is a character from the set {'a', 'b', ..., 'z'}. Both $P$ and $C$ were chosen at random and independently from other queries. 

When you have a query of the form `P C` you have to change the $P$<sup>$th$</sup> symbol of $S$ to $C$. After every change we ask you to output the number of distinct nonempty sub-strings of $S$.

## Input Format

The first line of input consists of two single space-separated integers $N$ and $Q$, the length of the string $S$ and the number of queries, respectively.

The second line contains string $S$.

The following $Q$ lines describe the queries in the form `P C`, where $P$ and $C$ are also separated with a single space.

**Constraints**  
$4 \le N \le 75000$  
$4 \le Q \le 75000$ 

## Output Format

Output $Q$ lines. Output the number of distinct substrings of $S$ after the $i$<sup>$th$</sup> query on the $i$<sup>$th$</sup> line of the output.

## Sample Input

4 4
aaab
1 a
2 b
3 c
4 d

## Sample Output

7
9
10

## Explanation

After replacing the character at the first index with a, we still have the original string aaab. The total non empty substrings of aaab are

a b aa ab aaa aab aaab

hence 7.

After replacing the character at the second index with b, we have the string abab. The non-empty substrings of abab are

a b ab ba aba bab abab

hence 7.

After replacing the character at the third index with c, we have the string abcb. The total non empty substrings of abcb are

a b c ab bc cb abc bcb abcb

hence 9.

After replacing the character at the fourth index with d, we have the string abcd. The total non empty substrings of abcd are

a b c d ab bc cd abc bcd abcd

hence 10.

Scoring

There are 12 test cases.

The first four test cases N = 100 and Q = 500

The next four test cases N = 75000 and Q = 10

The last four test cases N = 75000 and Q = 75000
