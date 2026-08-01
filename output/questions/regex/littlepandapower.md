# Little Panda Power

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 30
- **Success Ratio:** 0.6197785606441872
- **Total Submissions:** 3974
- **Solved Count:** 2463
- **URL:** https://www.hackerrank.com/challenges/littlepandapower

## Problem Statement

**Little Panda** has a thing for powers and modulus and he likes challenges. His friend **Lucy**, however, is impractical and challenges **Panda** to find both positive and negative powers of a number modulo a particular number. We all know that $A^{-1}\bmod X$ refers to the modular inverse of $A$ modulo $X$ (see [Wikipedia](http://en.wikipedia.org/wiki/Modular_multiplicative_inverse)).  

Since **Lucy** is impractical, she says that $A^{-n}\bmod  X = (A^{-1}\bmod  X)^n\bmod X$ for $n \gt 0$.  

Now she wants **Panda** to compute $A^B\bmod X$.   

She also thinks that this problem can be very difficult if the constraints aren't given properly. **Little Panda** is very confused and leaves the problem to the worthy programmers of the world. Help him in finding the solution.

**Input Format**  
The first line contains $T$, the number of test cases.  
Then $T$ lines follow, each line containing $A$, $B$ and $X$.  

**Output Format**  
Output the value of $A^B\bmod  X$.  

**Constraints**  
$1 \le T \le 1000$  
$1 \le A \le 10^6$  
$-10^6 \le B \le 10^6$  
$1 \le X \le 10^6$  
$A$  and $X$ are coprime to each other (see [Wikipedia](http://en.wikipedia.org/wiki/Coprime_integers))  

**Sample Input**  

    3  
    1 2 3  
    3 4 2  
    4 -1 5

**Sample Output**  

    1  
    1  
    4  

**Explanation**  
*Case 1:* $1^2\bmod  3 = 1 \bmod  3 = 1$  
*Case 2:* $3^4\bmod  2 = 81 \bmod  2 = 1$  
*Case 3:* $4^{-1}\bmod  5 = 4$  

## Input Format

The first line contains , the number of test cases.

Then  lines follow, each line containing ,  and .

## Output Format

Output the value of .

## Constraints

and  are coprime to each other (see Wikipedia)

## Sample Input

1 2 3
3 4 2
4 -1 5

## Sample Output

1
4

## Explanation

Case 1:

Case 2:

Case 3:
