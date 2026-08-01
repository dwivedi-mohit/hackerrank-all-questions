# Integers Come In All Sizes

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.993917152811086
- **Total Submissions:** 268953
- **Solved Count:** 267317
- **URL:** https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes

## Problem Statement

Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: $2^{31}-1$ (c++ int) or $2^{63} - 1$ (C++ long long int).    

As we know, the result of $a^b$ grows really fast with increasing $b$.  

Let's do some calculations on very large integers.  

**Task**  
Read four numbers, $a$, $b$, $c$, and $d$, and print the result of $a^b + c^d$.  

**Input Format**  
Integers $a$, $b$, $c$, and $d$ are given on four separate lines, respectively.

**Constraints**  
$1 \le a \le 1000$  
$1 \le b \le 1000$  
$1 \le c \le 1000$  
$1 \le d \le 1000$  

**Output Format**  
Print the result of $a^b + c^d$ on one line.  

**Sample Input**  

    9
    29
    7
    27
    
**Sample Output**  

    4710194409608608369201743232  
    
**Note**: This result is bigger than $2^{63} - 1$. Hence, it won't fit in the long long int of C++ or a 64-bit integer.  

## Input Format

Integers , , , and  are given on four separate lines, respectively.

## Output Format

Print the result of  on one line.

## Sample Input

29
7
27

## Sample Output

Note: This result is bigger than . Hence, it won't fit in the long long int of C++ or a 64-bit integer.
