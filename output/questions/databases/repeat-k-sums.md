# Repetitive K-Sums

- **Domain:** databases
- **Difficulty:** Advanced
- **Max Score:** 150
- **Success Ratio:** 0.7162396873643074
- **Total Submissions:** 4606
- **Solved Count:** 3299
- **URL:** https://www.hackerrank.com/challenges/repeat-k-sums

## Problem Statement

Alice thinks of a non-decreasing sequence of non-negative integers and wants Bob to guess it by providing him the set of all its **K**-sums with repetitions. 

What is this? Let the sequence be {A[1], A[2], ..., A[N]} and **K** be some positive integer that both Alice and Bob know. Alice gives Bob the set of all possible values that can be genereated by this - **A[i<sub>1</sub>] + A[i<sub>2</sub>] + ... + A[i<sub>K</sub>]**, where **1 ≤ i<sub>1</sub> ≤ i<sub>2</sub> ≤ ... ≤ i<sub>K</sub> ≤ N**. She can provide the values generated in any order she wishes to. Bob's task is to restore the initial sequence.

Consider an example. Let **N = 3** and **K = 2**. The sequence is {A[1], A[2], A[3]}. The sequence of its **2**-sums with repetitions is {A[1] + A[1], A[1] + A[2], A[1] + A[3], A[2] + A[2], A[2] + A[3], A[3] + A[3]}. But its elements could be provided in any order. For example any permutation of **{2, 3, 4, 4, 5, 6}** corresponds to the sequence **{1, 2, 3}**.


## Input Format

The first line of the input contains an integer **T** denoting the number of test cases.  
The description of **T** test cases follows.  
The first line of each test case contains two space separated integers **N** and **K**.  
The second line contains the sequence **S**<sub>i</sub> of all **K**-sums with repetitions of the sequence Alice initially thought of.


## Output Format

For each test case, output a single line containing the space separated list of elements of the non-decreasing sequence Alice thinks of. If there are several possible outputs you can output any of them.


## Constraints

+ $1 \le T \le 10^5$  
+ $1 \le N \le 10^5$  
+ $1 \le K \le 10^9$  
+ $2 \le S_i \le 10^{18}$  

**Note**  
The total number of elements in any input sequence does not exceed **10<sup>5</sup>**  
Each element of each input sequence is non-negative integer not exceeding **10<sup>18</sup>**.  
Each input sequence is a correct sequence of all **K**-sums with repetitions of some non-decreasing sequence of non-negative integers.


## Sample Input

3
1 3
3
2 2
12 34 56
3 2
2 3 4 4 5 6

## Sample Output

1
6 28
1 2 3

## Explanation

Sample case #00: When N = 1 and K = 3 the only K-sum is
S[1] = 3 * A[1]. Hence A[1] = S[1] / 3 = 3 / 3 = 1.

Sample case #01: Since 6 + 6 = 12, 6 + 28 = 34, 28 + 28 =
56, then Alice indeed could think of the sequence {6, 28}.

Sample case #02: It corresponds to the example in the problem
statement.
