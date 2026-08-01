# Sherlock and Probability

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 20
- **Success Ratio:** 0.5906003803314317
- **Total Submissions:** 3681
- **Solved Count:** 2174
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-probability

## Problem Statement

Watson gave a string $S$ to Sherlock. It is $N$ characters long and consists of only `1`s and `0`s. Now he asks:  	Given an integer $K$, I'll pick two indices $i$ and $j$ at random between $1$ and $N$, both inclusive. What's the probability that both $S[i]$ and $S[j]$ are `1` and $|i - j| \le K$?

**Input Format**   
First line contains $T$, the number of testcases. Each testcase consists of $N$(the length of $S$) and $K$ in one line and string in second line.     

**Output Format**  
Print the required probability as an irreducible fraction. If required answer is `0`, output `0/1`.   

**Constraints**   
$1 \le T \le 10^5$  
$1 \le N \le 10^5$  
$1 \le K \le N$   
$1 \le \text{Sum of N over all testcases in one file} \le 10^5$    

**Sample input**   

    2
    4 3
    1011
    4 1
    1011
    
**Sample output**   

	9/16
    5/16
    
**Explanation**    
test1: Out of 16 choices, 9 pairs of $(i,j)$ satisfy our condition.  

    (1,1), (1,3), (1,4), (3,1), (3,3), (3,4), (4,1), (4,3), (4,4)      

test2: Out of 16 choices, 5 pairs of $(i,j)$ satisfy our condition.   

    (1,1), (3,3), (4,4), (4,3), (3,4)  

## Input Format

First line contains , the number of testcases. Each testcase consists of (the length of ) and  in one line and string in second line.

## Output Format

Print the required probability as an irreducible fraction. If required answer is 0, output 0/1.

## Constraints

Sample input

2
4 3
1011
4 1
1011

Sample output

9/16
5/16

## Explanation

test1: Out of 16 choices, 9 pairs of  satisfy our condition.

(1,1), (1,3), (1,4), (3,1), (3,3), (3,4), (4,1), (4,3), (4,4)

test2: Out of 16 choices, 5 pairs of  satisfy our condition.

(1,1), (3,3), (4,4), (4,3), (3,4)
