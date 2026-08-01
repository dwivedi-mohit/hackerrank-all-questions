# Circles Math

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.7768595041322314
- **Total Submissions:** 121
- **Solved Count:** 94
- **URL:** https://www.hackerrank.com/challenges/circles-math

## Problem Statement

You are given a set A containing *n* integers from 1 to *n*; A = {1,2,3,...n}.  
Let's call P(A) as a set that contains all [permutations](http://en.wikipedia.org/wiki/Permutation) of A;  
For eg: if A = {1,2}. P(A) = {{1,2},{2,1}}

Can you find the number of elements *a* ∈ P(A) which satisfies following conditions:

+ For every 1 <= i <= n, a[i] ≠ i where a[i] is the i<sup>th</sup> integer in permutation a
+ There exists a set of *k* integers {i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, .... i<sub>k</sub>} such that 
a[i<sub>j</sub>] = i<sub>j+1</sub> ∀ j < k and a[i<sub>k</sub>] = i<sub>1 (cyclic)

**Input Format**  
The first line contains an integer T indicating the number of test-cases.
T lines follow. Each line has two integers n and k separated by a single space.

**Constraints**  
1 <= T <= 100  
1 <= k <= n <= 10<sup>6</sup>

**Output Format**  
Output the remainder of the answer after divided by 1000000007 ie., (10<sup>9</sup>+7)

**Sample Input**
 
    4
    3 2
    4 2
    5 3
    6 2

**Sample Output**

    0
    3
    20
    105

<strong>Hint</strong><br>
10<sup>9</sup>+7 is a <strong>prime number.</strong>

**Explanation**

*note* : Array's are 1 indexed. 

Lets take a look at N = 3 and K = 2

We will get 2 sets of A that satisfy the first property a[i] ≠ i, they are 

+ [3,1,2]
+ [2,3,1]

Now, as K = 2, we can have 6 such elements. 

+ [1,2], [1,3],[2,3], [2,1], [3,1], [3,2]

Lets consider the first element of P(A) -> [3,1,2] 

+ [1,2], a[1] ≠ 2
+ [1,3], a[1] = 3 but a[3] ≠ 1
+ [2,3], a[2] ≠ 3
+ [2,1], a[2] = 1 but a[1] ≠ 2
+ [3,1], a[3] = 1 but a[1] ≠ 3
+ [3,2], a[3] ≠ 2

Lets consider the second element of P(A) -> [2,3,1]

+ [1,2], a[1] = 2 but a[2] ≠ 1
+ [1,3], a[1] ≠ 3
+ [2,3], a[2] = 3 but a[3] ≠ 3
+ [2,1], a[2] ≠ 1
+ [3,1], a[3] = but a[1] ≠ 3
+ [3,2], a[3] ≠ 2

As none of the elements of a satisfy the properties above, hence 0. 

In the second case, n=4,k=2. Here follows all the permutations of 

A={1,2,3,4} we could find that satisfy the two condition above.

2 1 4 3 # (a[2] = 1, a[1] = 2) or (a[4] = 3, a[3] = 4) is ok.

4 3 2 1 # (a[4] = 1, a[1] = 4) or (a[3] = 2, a[2] = 3) is ok.

3 4 1 2 # (a[3] = 1, a[1] = 3) or (a[4] = 2, a[2] = 4) is ok.

**Timelimits**
Timelimits for this challenge is given [here](https://www.hackerrank.com/environment)

## Input Format

The first line contains an integer T indicating the number of test-cases.
T lines follow. Each line has two integers n and k separated by a single space.

## Output Format

Output the remainder of the answer after divided by 1000000007 ie., (109+7)

## Constraints

1 <= T <= 100

1 <= k <= n <= 106

## Sample Input

3 2
4 2
5 3
6 2

## Sample Output

3
20
105

Hint

109+7 is a prime number.

## Explanation

note : Array's are 1 indexed.

Lets take a look at N = 3 and K = 2

We will get 2 sets of A that satisfy the first property a[i] ≠ i, they are

- [3,1,2]

- [2,3,1]

Now, as K = 2, we can have 6 such elements.

- [1,2], [1,3],[2,3], [2,1], [3,1], [3,2]

Lets consider the first element of P(A) -> [3,1,2]

- [1,2], a[1] ≠ 2

- [1,3], a[1] = 3 but a[3] ≠ 1

- [2,3], a[2] ≠ 3

- [2,1], a[2] = 1 but a[1] ≠ 2

- [3,1], a[3] = 1 but a[1] ≠ 3

- [3,2], a[3] ≠ 2

Lets consider the second element of P(A) -> [2,3,1]

- [1,2], a[1] = 2 but a[2] ≠ 1

- [1,3], a[1] ≠ 3

- [2,3], a[2] = 3 but a[3] ≠ 3

- [2,1], a[2] ≠ 1

- [3,1], a[3] = but a[1] ≠ 3

- [3,2], a[3] ≠ 2

As none of the elements of a satisfy the properties above, hence 0.

In the second case, n=4,k=2. Here follows all the permutations of

A={1,2,3,4} we could find that satisfy the two condition above.

2 1 4 3 # (a[2] = 1, a[1] = 2) or (a[4] = 3, a[3] = 4) is ok.

4 3 2 1 # (a[4] = 1, a[1] = 4) or (a[3] = 2, a[2] = 3) is ok.

3 4 1 2 # (a[3] = 1, a[1] = 3) or (a[4] = 2, a[2] = 4) is ok.

Timelimits
Timelimits for this challenge is given here
