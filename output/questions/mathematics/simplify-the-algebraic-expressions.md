# Simplify the Algebraic Expressions

- **Domain:** mathematics
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.9153318077803204
- **Total Submissions:** 437
- **Solved Count:** 400
- **URL:** https://www.hackerrank.com/challenges/simplify-the-algebraic-expressions

## Problem Statement

A simplified algebraic expression is an expression which has been reduced to a simpler, more compact form *without changing the expression's value*. To a great extent, this largely involves collecting and combining 'like' terms. 

For example:  

- $x^2 + 2x + 2x^2 + 2 + 4x + 6$ can be simplified to $3x^2 + 6x + 8$. 
- $5x + 2(x – 4)$ can be simplified to $7x - 8$
- $5x \times (2 + 3^2) + 51 \times \frac{(x – 4)}{(5 + 6 \times 2)}$ reduces to $5x \times 11 + 3 \times (x-4)$, which reduces to $58x - 12$ 

**Task**  	
Given an algebraic expression, reduce the expression to a simplified form meeting the following criteria:

- All terms are in *descending* order of the power of variable $x$.
- Coefficients should be concatenated immediately to the left of your variable (e.g.: $5 \times x$ should be printed as `5x`).
- There are exactly $3$ characters between any $2$ consecutive terms of the expression: a space, followed by a $+$ or $-$ sign, followed by another space.
- In case there is no operator between expressions, assume that it implies multiplication. e.g. `(5x+2)(x+2)` should be treated as `(5x+2)*(x+2)`, `5(x+1)` should be treated as `5*(x+1)`.
- The simplified expression must not contain any parentheses.   
- $1$-coefficients and $1$-powers are implied; if the coefficient or power of a certain $x$ term is $1$, do not output $1$ (e.g.: $1x$ or $1 \times x$ simplifies to $x$, and $x^1$ simplifies to $x$).
- Do not print the powers of $x$ having a coefficient of $0$ (e.g.: output `5x^2 - 3`, *not* `5x^2 + 0x - 3`).  



## Input Format

The first line contains an integer, $T$, denoting the number of test cases.		
The $T$ subsequent lines of test cases each contain an expression that you must reduce.

## Output Format

For each test case, print the simplified expression on a new line. Your reduced expression should meet the criteria set forth in the *Problem Statement* above. 

## Constraints

- $1 \le T \le 10$
- Each expression will only use a single variable, $x$, and may contain parentheses (`(`,`)`), addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and exponentiation (`^`) symbols. The role of exponentation symbols will be limited to representing powers of $x$ or integers. You will not encounter terms such as $(x-5)^2$. You may encounter terms like 3^(1+4) and so on.  
- There may be one or more spaces between any consecutive terms, operators, or operands (so you must account for and remove these in your code).
- No divisor will contain a term involving $x$, and all divisors are integers.
- All coefficients in the final expression are integers (e.g.: $5x^2, 4x, x$). You will not encounter something like $2.5x$ or $1.25x^2$.  
- There may be multiple levels of nested parentheses.
- The original expression will not contain more than $100$ characters (including spaces).
- The expression will not evaluate to a polynomial of an order higher than $5$. 
- You will not encounter an integer exeeding $1000$ either while parsing the original expression or in the final coefficients of your simplified expressions.  
- Expressions not containing a variable ($x$) simply require you to calculate the expression's result.

## Sample Input

10x + 2x - (3x + 6)/3
18*(2x+2) - 5
((9x + 81)/3 + 27)/3  - 2x
18x + (12x + 10)*(2x+4)/2 - 5x
(2x+5) * (x*(9x + 81)/3 + 27)/(1+1+1)  - 2x
(2x+5) * (x*(9x^3 + 81)/3 + 27)/(1+1+1)  - 2x

## Sample Output

11x - 2
36x + 31
-x + 18
12x^2 + 47x + 20
2x^3 + 23x^2 + 61x + 45
2x^5 + 5x^4 + 18x^2 + 61x + 45

## Explanation

Observe that the original expressions have been expanded and their like terms collected, thus resulting in the printed simplified expressions.
