# Black Hole

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.3389830508474576
- **Total Submissions:** 236
- **Solved Count:** 80
- **URL:** https://www.hackerrank.com/challenges/demidenko-black-hole

## Problem Statement

Given integers $n$, $a$, $b$ and $M$, calculate the value $\sum \limits_{k=0}^{n} k^a b^k $ modulo $M$.

**Input Format**  
The first line contains the number of test cases $T$.   
Each of the next $T$ lines contains four space-separated integers $n$, $a$, $b$ and $M$. 

**Output Format**  
For each test case output one integer: the value of the sum.

**Note** In this problem we take $0^0 = 1$  

**Constraints**  
$1 \le T \le 6^6+6$  
$0 \le n \le 10^{18}$  
$0 \le a \le 777$  
$0 \le |b| \le 10^{18}$  
$1 \le M \le 10^9$  
The sum of all $a$ in one test file doesn't exceed 1000

**Sample input**  

    5
    3 1 1 100
    3 0 1 100
    3 1 0 100
    44 44 4 444
    77 7 47 747

**Sample Output**  

    6
    4
    0
    288
    288

**Explanation**  

$0^1\times 1^0~ + ~ 1^1 \times 1^1~ + ~2^1\times 1^2 ~ + ~3^1\times 1^3 = 0 + 1 + 2 + 3 = 6$  
$0^0 \times 1^0 ~ + ~ 1^0 \times 1^1 ~ + ~ 2^0\times 1^2 ~ + ~ 3^0\times 1^3 = 1 + 1 + 1 + 1 = 4$  
$0^1\times 0^0 ~ + ~ 1^1\times 0^1 ~ + ~ 2^1\times 0^2 ~ + ~ 3^1\times 0^3 = 0 + 0 + 0 + 0 = 0$

## Input Format

The first line contains the number of test cases .

Each of the next  lines contains four space-separated integers , ,  and .

## Output Format

For each test case output one integer: the value of the sum.

Note In this problem we take

## Constraints

The sum of all  in one test file doesn't exceed 1000

Sample input

5
3 1 1 100
3 0 1 100
3 1 0 100
44 44 4 444
77 7 47 747

## Sample Output

4
0
288
288
