# Determining DNA Health

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.4005529444290849
- **Total Submissions:** 36170
- **Solved Count:** 14488
- **URL:** https://www.hackerrank.com/challenges/determining-dna-health

## Problem Statement

[DNA](https://en.wikipedia.org/wiki/DNA) is a nucleic acid present in the bodies of living things. Each piece of DNA contains a number of *genes*, some of which are beneficial and increase the DNA's *total health*. Each gene has a *health value*, and the *total health* of a DNA is the sum of the health values of all the beneficial genes that occur as a substring in the DNA. We represent genes and DNA as non-empty strings of lowercase English alphabetic letters, and the same gene may appear multiple times as a susbtring of a DNA.

Given the following:

- An array of beneficial gene strings, $genes = [g_0, g_1, \ldots, g_{n-1}]$. Note that these gene sequences are *not* guaranteed to be distinct.
- An array of gene health values, $health = [h_0, h_1, \ldots, h_{n-1}]$, where each $h_i$ is the health value for gene $g_i$.
- A set of $s$ DNA strands where the definition of each strand has three components, $start$, $end$, and $d$, where string $d$ is a DNA for which genes $g_{start}, \ldots, g_{end}$ are healthy.

Find and print the respective total healths of the *unhealthiest* (minimum total health) and  *healthiest* (maximum total health) strands of DNA as two space-separated values on a single line.

## Input Format

The first line contains an integer, $n$, denoting the total number of genes. 	
The second line contains $n$ space-separated strings describing the respective values of $g_0, g_1, \ldots, g_{n-1}$ (i.e., the elements of $genes$).		
The third line contains $n$ space-separated integers describing the respective values of $h_0, h_1, \ldots, h_{n-1}$ (i.e., the elements of $health$).		
The fourth line contains an integer, $s$, denoting the number of strands of DNA to process.		
Each of the $s$ subsequent lines describes a DNA strand in the form `start end d`, denoting that the healthy genes for DNA strand $d$ are $g_{start}, \ldots, g_{end}$ and their respective correlated health values are $h_{start}, \ldots, h_{end}$.

## Output Format

Print two space-separated integers describing the respective total health of the *unhealthiest* and the *healthiest* strands of DNA.

## Constraints

+ $1 \le n, s \le 10^{5}$   
+ $0 \le h_i \le 10^{7}$  
+ $0 \le first \le last \lt n$  
+ $1 \le$ the sum of the lengths of all genes and DNA strands $\le 2 \times 10^{6}$  
- It is guaranteed that each $g_i$ consists of lowercase English alphabetic letters only (i.e., `a` to `z`).

## Sample Input

6
a b c aa d b
1 2 3 4 5 6
3
1 5 caaab
0 4 xyz
2 4 bcdybc

## Sample Output

0 19

## Explanation

In the diagrams below, the ranges of beneficial genes for a specific DNA on the left are highlighed in green and individual instances of beneficial genes on the right are bolded. The total healths of the  strands are:

-

The total health of caaab is .

-

The total health of xyz is , because it contains no beneficial genes.

-

The total health of bcdybc is .

The unhealthiest DNA strand is xyz with a total health of , and the healthiest DNA strand is caaab with a total health of . Thus, we print 0 19 as our answer.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
