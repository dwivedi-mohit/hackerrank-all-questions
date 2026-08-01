# C++ Class Template Specialization

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 35
- **Success Ratio:** 0.9721374865735768
- **Total Submissions:** 46550
- **Solved Count:** 45253
- **URL:** https://www.hackerrank.com/challenges/cpp-class-template-specialization

## Problem Statement

You are given a *main* function which reads the enumeration values for two different types as input, then prints out the corresponding  [enumeration](http://en.cppreference.com/w/cpp/language/enum) names. Write a class template that can provide the names of the enumeration values for both types. If the enumeration value is not valid, then print `unknown`.

## Input Format

The first line contains $t$, the number of test cases.		
Each of the $t$ subsequent lines contains two space-separated integers. The first integer is a color value, $c$, and the second integer is a fruit value, $f$.

## Output Format

The locked stub code in your editor prints $t$ lines containing the *color* name and the *fruit* name corresponding to the input enumeration index.

## Constraints

- $1 \le t \le 100$  
- $-2 \times 10^9 \le c \le 2 \times 10^9$  
- $-2 \times 10^9 \le f \le 2 \times 10^9$  

## Sample Input

1 0
3 3

## Sample Output

green apple
unknown unknown

## Explanation

Since , there are two lines of output.

- The two input index values,  and , correspond to green in the color enumeration and apple in the fruit enumeration. Thus, we print green apple.

- The two input values,  and , are outside of the range of our enums. Thus, we print unknown unknown.
