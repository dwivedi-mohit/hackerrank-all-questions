# Calculate the Nth term

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9744527647927764
- **Total Submissions:** 312754
- **Solved Count:** 304764
- **URL:** https://www.hackerrank.com/challenges/recursion-in-c

## Problem Statement

**Objective**	
This challenge will help you learn the concept of recursion.

A function that calls itself is known as a recursive function. The C programming language supports recursion. But while using recursion, one needs to be careful to define an exit condition from the function, otherwise it will go into an infinite loop.

To prevent infinite recursion, $if...else$ statement (or similar approach) can be used where one branch makes the recursive call and other doesn't.
```c
void recurse() {
    .....
    recurse()  //recursive call
    .....
}
int main() {
    .....
    recurse(); //function call
    .....
}
```


**Task**

There is a series, $S$, where the next term is the sum of pervious three terms. Given the first three terms of the series, $a$, $b$, and $c$ respectively, you have to output the *n<sup>th</sup>* term of the series using recursion.

Recursive method for calculating *n<sup>th</sup>* term is given below.

$$S(n) = \begin{cases}a & n = 1,\\b & n = 2,\\c & n = 3,\\S(n-1) + S(n-2) + S(n-3) & otherwise\end{cases}$$

## Input Format

- The first line contains a single integer, $n$.

- The next line contains *3* space-separated integers, $a$, $b$, and $c$.

## Output Format

Print the *n<sup>th</sup>* term of the series, $S(n)$.

## Constraints

- $1 \le n \le 20$
- $1 \le a, b, c \le 100$

## Sample Input

5
1 2 3

## Sample Output

11

## Explanation

Consider the following steps:

-

-

-

-

-

From steps , , , and , we can say ; then using the values from step , , , and , we get . Thus, we print  as our answer.
