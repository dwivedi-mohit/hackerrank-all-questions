# Permutation Equations

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 120
- **Success Ratio:** 0.7055837563451777
- **Total Submissions:** 197
- **Solved Count:** 139
- **URL:** https://www.hackerrank.com/challenges/permutation-equations

## Problem Statement



Let *N* be a positive integer. Let's define a mapping *f* on the set
of permutations of integers from *1* to *N*, inclusive.
 Let *x = (x[1], ..., x[N])* be a permutation of integers from *1*
to *N*, inclusive.
 We define the permutation *y = (y[1], ..., y[N])* as follows.

-   *y[1] = 1*.
-   For *i \> 1* we consider number *z = x[y[i-1]]*.
    -   If *z* does not equal any of the numbers *y[1], ...,
        y[i-1]* then we set *y[i] = z*.
    -   Otherwise *y[i]* is defined as the smallest integer from *1*
        to *N* (inclusive) that does not equal any of the numbers
        *y[1], ..., y[i-1]*.

We consider permutation *y* as an image of *x* when mapping *f* is
applied to *x*. That is, we set *f(x) = y*.

Denote by *g(y)* the number of solutions of the equation *f(x) = y*.
That is, *g(y)* is the number of permutations *x* of integers from
*1* to *N*, inclusive, such that *f(x) = y*. 

**Challenge**  
For the given non-negative integers *L* and *R*, find the number of
permutations *y* of integers from *1* to *N*, inclusive, such that
*L ≤ g(y) ≤ R*. Since this number can be quite large output it modulo (*10<sup>9</sup> + 7*).

**Input Format**  
The first line contains an integer *T* denoting the
number of test cases. *T* test cases follow.  
Each test case consists of one line which contains three space-separated integers *N, L* and *R*.

**Output Format**  
For each test case, output a single line containing P *mod* (10<sup>9</sup>+7), where P is the required number of permutations.

**Constraints**

1 &le; T &le; 1000  
1 &le; N &le; 200,000  
0 &le; L, R &le; 10<sup>18</sup>


**Sample Input**  

    4  
    2 0 0  
    3 2 2  
    3 0 10  
    10 2 1  

**Sample Output**  

    1  
    1  
    6  
    0  

**Explanation**

**Example case 1.** The only permutation *y* for which equation *f(x)
= y* has no solutions is *y = (2, 1)*.

**Example case 2.** The only permutation *y* for which equation *f(x)
= y* has *2* solutions is *y = (1, 3, 2)*.
 The solutions are *x = (3, 2, 1)* and *x = (3, 1, 2)*.

**Example case 3.** For all *6* permutations *y* of numbers *{1, 2,
3}* we have *0 &le; g(y) &le; 10*.

**Example case 4.** Be careful, *L* could be greater than *R*. In
this case the answer is zero.


## Input Format

The first line contains an integer T denoting the
number of test cases. T test cases follow.

Each test case consists of one line which contains three space-separated integers N, L and R.

## Output Format

For each test case, output a single line containing P mod (109+7), where P is the required number of permutations.

## Constraints

1 ≤ T ≤ 1000

1 ≤ N ≤ 200,000

0 ≤ L, R ≤ 1018

## Sample Input

2 0 0
3 2 2
3 0 10
10 2 1

## Sample Output

1
6
0

## Explanation

Example case 1. The only permutation y for which equation f(x)
= y has no solutions is y = (2, 1).

Example case 2. The only permutation y for which equation f(x)
= y has 2 solutions is y = (1, 3, 2).
 The solutions are x = (3, 2, 1) and x = (3, 1, 2).

Example case 3. For all 6 permutations y of numbers {1, 2,
3} we have 0 ≤ g(y) ≤ 10.

Example case 4. Be careful, L could be greater than R. In
this case the answer is zero.
