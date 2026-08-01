# Expressions

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 40
- **Success Ratio:** 0.7817836812144212
- **Total Submissions:** 527
- **Solved Count:** 412
- **URL:** https://www.hackerrank.com/challenges/expressions

## Problem Statement

5 year old Shinchan had just started learning Mathematics. Meanwhile, one of his studious classmate, Kazama, had already written a basic calculator which supports only 3 operations on integral numbers: _multiplication $(*)$, addition $(+)$, and subtraction $(-)$_.  Since he had just learnt about these operations, he didn't have knowledge of precedence of operators, and in his calculator all operators had same precedence and left associativity.   

As always Shinchan started to irritate him with his silly question. He gave Kazama a list of $N$ integers and asked him to insert one of the above operators between each pair of consecutive integer such that the result obtained after feeding the resulting expression in Kazama's calculator is divisible by $101$. At core Shinchan is a good guy, so he gave only that list of integers for which the answer always exists.  

Can you help Kazama in creating the required expression? If multiple solutions exists, print any one of them.   




## Input Format

First line contains an integer, $N$, representing the number of elements in the list. In next line there are $N$ space separated integers representing the list.  



## Output Format

Print the resultant expression. You can insert 0 or more spaces between operators and operands.  

## Constraints

- $2 \le N \le 10^4$
- $1 \le element\ of\ list \le 100$
- Length of output expression should not exceed $10\times N$.

**Note**

- You are not allowed to permute the list.
- All operators have same precedence order and left associativity, ie., $a+b*c-d*e \equiv ((((a+b)*c)-d)*e)$
- Unary plus and minus are not supported, ie., statement like $-a$, $a*-b$, $-a*b + c$ are invalid.

## Sample Input

3
22 79 21

## Sample Output

22*79-21

## Explanation

Solution 1: , where  and it is perfectly divisible by 101.

Solution 2: , which is another multiple of 101.
