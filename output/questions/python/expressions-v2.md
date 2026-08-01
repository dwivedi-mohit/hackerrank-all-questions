# Expressions V2

- **Domain:** python
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8631239935587761
- **Total Submissions:** 621
- **Solved Count:** 536
- **URL:** https://www.hackerrank.com/challenges/expressions-v2

## Problem Statement

Once Kazama had written a basic calculator, he read further about other operators and operator precedence. Now he is writing a new calculator with following details: 

* _Binary addition:_ $x+y$.
*  _Binary subtraction:_ $x-y$
* _Multiplication:_ $x\times y$
* _Division:_ $\frac{x}{y}$
* _Unary operators:_ $+x$ and $-x$
* _Brackets:_ $(\ldots)$

###Operator precedence
$(\textit{Unary Operators, Brackets}) \gt (\textit{Multiplication, Division}) \gt (\textit{Binary  addition, Binary subtraction})$

###Associativity 
Now all operators are _right associative_. That is $p - q - r  \equiv p-(q-r)$, or $p/q/r  \equiv p/(q/r)$

Formally it has following grammar:

	 Expression ::= Term [+-] Expression
	              | Term
	
	 Term       ::= Factor [*/] Term
	              | Factor
	
	 Factor     ::= Number
	              | [+-] Factor
	              | '(' Expression ')'
<br>
He needs your help to verify it. He wants you to solve some expressions for him using the above grammar and he will cross check the results. Since you are also lazy, you will write another computer program which will solve the expressions. Since the output value can be too large, you have to tell output modulo $1000000007 (=10^9+7)$.  

**Note:**

- $10^9+7$ is a prime.
- $1/b\equiv  b^{-1} \equiv  b^{p-2} (mod\ p), where\ p\ is\ prime\ and\ b < p$

## Input Format

Input will contain a valid expression.

## Output Format

Print the result of expression modulo $(10^9+7)$<br>

**Sample Input 0**  

	22 * 79 - 21
	
**Sample Output 0**

	1717

**Sample Input 1** 

	4/-2/2 + 8

**Sample Output 1**  

	4
 
**Sample Input 2**

	55+3-45*33-25

**Sample Output 2**

	999998605

**Sample Input 3**  

	4/-2/(2 + 8)

**Sample Output 3**  

	999999987





## Constraints

- Length of expression will not exceed $10^5$.
- $1 \le number \le 10^9$
- There can be $0$ or more whitespaces between operators/operands.
- Tests are designed such that there will be no _divide by zero_ case. 
- Each factor will be accompanied by at-most one unary operator. That is *"$-+-4$"* is an invalid case.

## Sample Input

22 * 79 - 21

## Sample Output

1717

## Explanation

Sample Case 0:

 .

Sample Case 1:

Sample Case 2:

Sample Case 3:
