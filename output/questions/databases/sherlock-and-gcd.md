# Sherlock and GCD

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.7831054504588875
- **Total Submissions:** 21356
- **Solved Count:** 16724
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-gcd

## Problem Statement

Sherlock is stuck while solving a problem: Given an array $A = \{a_1, a_2, \cdots, a_N \}$, he wants to know if there exists a subset $B$ of this array which follows these statements:

* $B$ is a non-empty subset.
* There exists no integer $x (x > 1)$ which divides all elements of $B$.
* There are no elements of $B$ which are equal to another.

## Input Format

The first line of input contains an integer, $T$, representing the number of test cases. Then $T$ test cases follow.  
Each test case consists of two lines. The first line contains an integer, $N$, representing the size of array $A$. In the second line there are $N$ space-separated integers, $a_1, a_2, \ldots, a_n$, representing the elements of array $A$.

**Constraints**  
$1 \le T \le 10$    
$1 \le N \le 100$    
$1 \le a_i \le 10^5 \text{  } \forall 1\le i \le N$   

## Output Format

Print `YES` if such a subset exists; otherwise, print `NO`.

## Sample Input

3
1 2 3
2
2 4
3
5 5 5

## Sample Output

YES
NO
NO

## Explanation

In the first test case,  are all the possible non-empty subsets, of which the first and the last four satisfy the given condition.

For the second test case, all possible subsets are . For all of these subsets,  divides each element. Therefore, no non-empty subset exists which satisfies the given condition.

For the third test case, the following subsets exist: 123. Because the single element in the first subset is divisible by  and the other two subsets have elements that are equal to another, there is no subset that satisfies every condition.
