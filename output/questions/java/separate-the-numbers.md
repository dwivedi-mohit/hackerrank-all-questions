# Separate the Numbers

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9061864531141904
- **Total Submissions:** 47701
- **Solved Count:** 43226
- **URL:** https://www.hackerrank.com/challenges/separate-the-numbers

## Problem Statement

A numeric string, $s$, is *beautiful* if it can be split into a sequence of two or more positive integers, $a[1],a[2], \ldots ,a[n]$, satisfying the following conditions:

1. $a[i]-a[i-1]=1$ for any $1 < i \le n$ (i.e., each element in the sequence is $1$ more than the previous element).
2. *No $a[i]$ contains a leading zero.* For example, we can split $s = 10203$ into the sequence $\{1, 02, 03\}$, but it is *not* beautiful because $02$ and $03$ have leading zeroes.
3. *The contents of the sequence cannot be rearranged.* For example, we can split $s = 312$ into the sequence $\{3, 1, 2\}$, but it is not beautiful because it breaks our first constraint (i.e., $1 - 3 \ne 1$).

The diagram below depicts some beautiful strings:

![image](https://s3.amazonaws.com/hr-assets/0/1486398483-1b25a912c1-Separate.png)

Perform $q$ queries where each query consists of some integer string $s$. For each query, print whether or not the string is beautiful on a new line. If it is beautiful, print ``YES x``, where $x$ is the first number of the increasing sequence.  If there are multiple such values of $x$, choose the smallest.  Otherwise, print `NO`.  

**Function Description**  

Complete the *separateNumbers* function in the editor below.  

separateNumbers has the following parameter:  

- *s*: an integer value represented as a string   

**Prints**   
- *string:*  Print a string as described above. Return nothing.  

## Input Format

The first line contains an integer $q$, the number of strings to evaluate. 	
Each of the next $q$ lines contains an integer string $s$ to query.

## Output Format

  

## Constraints

* $1 \le q \le 10$
* $1 \le |s| \le 32$
* $s[i] \in [0-9]$

## Sample Input

7
1234
91011
99100
101103
010203
13
1

## Sample Output

YES 1
YES 9
YES 99
NO
NO
NO
NO

## Explanation

The first three numbers are beautiful (see the diagram above). The remaining numbers are not beautiful:

- For , all possible splits violate the first and/or second conditions.

- For , it starts with a zero so all possible splits violate the second condition.

- For , the only possible split is , which violates the first condition.

- For , there are no possible splits because  only has one digit.
