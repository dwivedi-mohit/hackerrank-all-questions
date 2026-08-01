# Cyclic Quadruples

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.803030303030303
- **Total Submissions:** 396
- **Solved Count:** 318
- **URL:** https://www.hackerrank.com/challenges/cyclicquadruples

## Problem Statement



You need to count the number of quadruples of integers _(X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, X<sub>4</sub>)_,
such that _L<sub>i</sub> &le; X<sub>i</sub> &le; R<sub>i</sub>_ for `i = 1, 2, 3, 4`
and _X<sub>1</sub> &ne; X<sub>2</sub>_, _X<sub>2</sub> &ne; X<sub>3</sub>_,
_X<sub>3</sub> &ne; X<sub>4</sub>_, _X<sub>4</sub> &ne; X<sub>1</sub>_.


The answer could be quite large.  
Hence you should output it modulo _(10<sup>9</sup> + 7)_.  
That is, you need to find the remainder of the answer by _(10<sup>9</sup> + 7)_.


**Input Format**  
The first line of the input contains an integer _T_ denoting the number of test cases.
The description of _T_ test cases follows.
The only line of each test case contains 8 space-separated integers
_L<sub>1</sub>, R<sub>1</sub>, L<sub>2</sub>, R<sub>2</sub>, L<sub>3</sub>, R<sub>3</sub>, L<sub>4</sub>, R<sub>4</sub>_, in order.

**Output Format**  
For each test case, output a single line containing the number of required quadruples modulo _(10<sup>9</sup> + 7)_.

**Constraints**  
1 &le; _T_ &le; 1000  
1 &le; _L<sub>i</sub>_ &le; _R<sub>i</sub>_ &le; 10<sup>9</sup>

**Sample Input**

    5
    1 4 1 3 1 2 4 4
    1 3 1 2 1 3 3 4
    1 3 3 4 2 4 1 4
    1 1 2 4 2 3 3 4
    3 3 1 2 2 3 1 2

**Sample Output**  

    8
    10
    23
    6
    5
    
**Explanation**  
**Example case 1.** All quadruples in this case are

    1 2 1 4
    1 3 1 4
    1 3 2 4
    2 1 2 4
    2 3 1 4
    2 3 2 4
    3 1 2 4
    3 2 1 4

**Example case 2.** All quadruples in this case are

    1 2 1 3
    1 2 1 4
    1 2 3 4
    2 1 2 3
    2 1 2 4
    2 1 3 4
    3 1 2 4
    3 1 3 4
    3 2 1 4
    3 2 3 4

**Example case 3.** All quadruples in this case are

    1 3 2 3
    1 3 2 4
    1 3 4 2
    1 3 4 3
    1 4 2 3
    1 4 2 4
    1 4 3 2
    1 4 3 4
    2 3 2 1
    2 3 2 3
    2 3 2 4
    2 3 4 1
    2 3 4 3
    2 4 2 1
    2 4 2 3
    2 4 2 4
    2 4 3 1
    2 4 3 4
    3 4 2 1
    3 4 2 4
    3 4 3 1
    3 4 3 2
    3 4 3 4

**Example case 4.** All quadruples in this case are

    1 2 3 4
    1 3 2 3
    1 3 2 4
    1 4 2 3
    1 4 2 4
    1 4 3 4

**Example case 5.** All quadruples in this case are

    3 1 2 1
    3 1 3 1
    3 1 3 2
    3 2 3 1
    3 2 3 2


## Input Format

The first line of the input contains an integer T denoting the number of test cases.
The description of T test cases follows.
The only line of each test case contains 8 space-separated integers
L1, R1, L2, R2, L3, R3, L4, R4, in order.

## Output Format

For each test case, output a single line containing the number of required quadruples modulo (109 + 7).

## Constraints

1 ≤ T ≤ 1000

1 ≤ Li ≤ Ri ≤ 109

## Sample Input

1 4 1 3 1 2 4 4
1 3 1 2 1 3 3 4
1 3 3 4 2 4 1 4
1 1 2 4 2 3 3 4
3 3 1 2 2 3 1 2

## Sample Output

10
23
6
5

## Explanation

Example case 1. All quadruples in this case are

1 2 1 4
1 3 1 4
1 3 2 4
2 1 2 4
2 3 1 4
2 3 2 4
3 1 2 4
3 2 1 4

Example case 2. All quadruples in this case are

1 2 1 3
1 2 1 4
1 2 3 4
2 1 2 3
2 1 2 4
2 1 3 4
3 1 2 4
3 1 3 4
3 2 1 4
3 2 3 4

Example case 3. All quadruples in this case are

1 3 2 3
1 3 2 4
1 3 4 2
1 3 4 3
1 4 2 3
1 4 2 4
1 4 3 2
1 4 3 4
2 3 2 1
2 3 2 3
2 3 2 4
2 3 4 1
2 3 4 3
2 4 2 1
2 4 2 3
2 4 2 4
2 4 3 1
2 4 3 4
3 4 2 1
3 4 2 4
3 4 3 1
3 4 3 2
3 4 3 4

Example case 4. All quadruples in this case are

1 2 3 4
1 3 2 3
1 3 2 4
1 4 2 3
1 4 2 4
1 4 3 4

Example case 5. All quadruples in this case are

3 1 2 1
3 1 3 1
3 1 3 2
3 2 3 1
3 2 3 2
