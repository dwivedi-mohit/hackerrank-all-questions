# Area Under Curves and Volume of Revolving a Curve

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9034360994159989
- **Total Submissions:** 7363
- **Solved Count:** 6652
- **URL:** https://www.hackerrank.com/challenges/area-under-curves-and-volume-of-revolving-a-curv

## Problem Statement

**Definite Integrals via Numerical Methods**  

This relates to definite integration via numerical methods. 

Consider the algebraic expression given by:  

$(a$<sub>$1$</sub>$)x$<sup>$b$<sub>$1$</sub></sup> $+$ $(a$<sub>$2$</sub>$)x$<sup>$b$<sub>$2$</sub></sup> $+$ $(a$<sub>$3$</sub>$)x$<sup>$b$<sub>$3$</sub></sup> $......(a$<sub>$n$</sub>$)x$<sup>$b$<sub>$n$</sub></sup>  


For the purpose of numerical computation, the area under the curve $y = f(x)$ between the limits $a$ and $b$ can be computed by the [Limit Definition of a Definite Integral](https://www.math.ucdavis.edu/~kouba/CalcTwoDIRECTORY/defintdirectory/).  

Here is some background about [**areas and volume computation**](http://tutorial.math.lamar.edu/Classes/CalcI/Area_Volume_Formulas.aspx).

Using equal subintervals of length $= 0.001$, you need to:   

1. Evaluate the area bounded by a given polynomial function of the kind described above, between the given limits of $L$ and $R$.  

2. Evaluate the volume of the solid obtained by revolving this polynomial curve around the $x$-axis.  


A relative error margin of $0.01$ will be tolerated.

**Input Format** 

The first line contains $N$ integers separated by spaces, which are the values of $a$<sub>$1$</sub>$, a$<sub>$2$</sub>$...a$<sub>$N$</sub>.  <br>
The second line contains $N$ integers separated by spaces, which are the values of $b$<sub>$1$</sub>$, b$<sub>$2$</sub>$...b$<sub>$N$</sub>.  <br>
The third line contains two space separated integers, $L$ and $R$, the lower and upper range limits in which the integration needs to be performed, respectively.  

**Constraints** 

$-1000 <= a <= 1000$   
$-20 <= b <= 20$   
$1 <= L < R <= 20$   

**Output Format**
      
The first line should contain the area between the curve and the $x$-axis, bound between the specified limits. <br>
The second line should contain the volume of the solid obtained by rotating the curve around the $x$-axis, between the specified limits.  



**Sample Input**  


    1 2 3 4 5
    6 7 8 9 10
    1 4  

**Explanation**

The algebraic expression represented by:

$(1)x$<sup>$6$</sup>$ + (2)x$<sup>$7$</sup>$ + (3)x$<sup>$8$</sup>$ + (4)x$<sup>$9$</sup>$ + (5)x$<sup>$10$</sup>

We need to find the area of the curve enclosed under this curve, between the limits $x=1$ and $4$. We also need to find the volume of the solid formed by revolving this curve around the $x$-axis between the limits $x = 1$ and $4$.

**Sample Output**

    2435300.3
    26172951168940.8

**Scoring**  

All test cases are weighted equally.
You need to clear all the tests in a test case.


## Input Format

The first line contains  integers separated by spaces, which are the values of .

The second line contains  integers separated by spaces, which are the values of .

The third line contains two space separated integers,  and , the lower and upper range limits in which the integration needs to be performed, respectively.

## Output Format

The first line should contain the area between the curve and the -axis, bound between the specified limits.

The second line should contain the volume of the solid obtained by rotating the curve around the -axis, between the specified limits.

## Sample Input

1 2 3 4 5
6 7 8 9 10
1 4

## Sample Output

2435300.3
26172951168940.8

Scoring

All test cases are weighted equally.
You need to clear all the tests in a test case.

## Explanation

The algebraic expression represented by:

We need to find the area of the curve enclosed under this curve, between the limits  and . We also need to find the volume of the solid formed by revolving this curve around the -axis between the limits  and .
