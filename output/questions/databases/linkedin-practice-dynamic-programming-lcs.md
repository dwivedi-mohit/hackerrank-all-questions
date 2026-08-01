# The Longest Common Subsequence (LCS)

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 75
- **Success Ratio:** 0.747716894977169
- **Total Submissions:** 3504
- **Solved Count:** 2620
- **URL:** https://www.hackerrank.com/challenges/linkedin-practice-dynamic-programming-lcs

## Problem Statement

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.  Longest common subsequence (_LCS_) of 2 sequences is a subsequence, with maximal length, which is common to both the sequences.   
<br>
Given two sequence of integers, $A = [a_1, a_2,\ldots, a_n]$ and $B = [b_1, b_2,\ldots,b_m ]$, find **any one** longest common subsequence. 

In case multiple solutions exist, print any of them. It is guaranteed that at least one non-empty common subsequence will exist.

## Input Format

First line contains two space separated integers, $n$ and $m$, where $n$ is the size of sequence $A$, while $m$ is size of sequence $B$.   In next line there are $n$ space separated integers representing sequence $A$, and in third line there are $m$ space separated integers representing sequence $B$.

<pre>
n m
A<sub>1</sub> A<sub>2</sub> … A<sub>n</sub> 
B<sub>1</sub> B<sub>2</sub> … B<sub>m</sub>  
</pre>

**Constraints**  

$1 \le n \le 100$  
$1 \le m \le 100$  
$0 \le a_i < 1000, where\ i \in [1, n]$  
$ 0 \le b_j < 1000, where\ j \in [1,m]$  

## Output Format

Print the longest common subsequence and each element should be separated by at least one white-space. In case of multiple answers, print any one of them.

## Sample Input

5 6
1 2 3 4 1
3 4 1 2 1 3

## Sample Output

1 2 3

## Explanation

There is no common subsequence with length larger than 3. And "1 2 3",  "1 2 1", "3 4 1" are all correct answers.
