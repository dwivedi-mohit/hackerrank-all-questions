# Arithmetic Expressions

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 40
- **Success Ratio:** 0.49498224486645054
- **Total Submissions:** 6477
- **Solved Count:** 3206
- **URL:** https://www.hackerrank.com/challenges/arithmetic-expressions

## Problem Statement

5-year-old Shinchan had just started learning mathematics. Meanwhile, one of his studious classmates, Kazama, had already written a basic calculator which supports only three operations on integers: _multiplication $(\times)$, addition $(+)$, and subtraction $(-)$_.  Since he had just learned about these operations, he didn't know about operator precedence, and so, in his calculator, all operators had the same precedence and were left-associative.

As always, Shinchan started to irritate him with his silly questions. He gave Kazama a list of $n$ integers and asked him to insert one of the above operators between each pair of consecutive integers such that the result obtained after feeding the resulting expression in Kazama's calculator is divisible by $101$. At his core, Shinchan is actually a good guy, so he only gave lists of integers for which an answer exists.  

Can you help Kazama create the required expression? If multiple solutions exist, print any one of them.   

## Input Format

The first line contains a single integer $n$ denoting the number of elements in the list. The second line contains $n$ space-separated integers $a_1, a_2, \ldots, a_n$ denoting the elements of the list.

## Output Format

Print a single line containing the required expressoin. You may insert spaces between operators and operands.

**Note**

- You are not allowed to permute the list.
- All operators have the same precedence and are left-associative, e.g., $a+b\times c-d\times e$ is interpreted as $((((a+b)\times c)-d)\times e)$
- Unary plus and minus are not supported, e.g., statements like $-a$, $a\times -b$, or $-a\times b + c$ are invalid.


## Constraints

- $2 \le n \le 10^4$
- $1 \le a_i \le 100$
- The length of the output expression should not exceed $10n$.


## Sample Input

3
22 79 21

## Sample Output

22*79-21

## Explanation

Solution 1: , where , so it is perfectly divisible by .

Solution 2: , which is also divisible by .
