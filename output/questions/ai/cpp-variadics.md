# C++ Variadics

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.9555979614158386
- **Total Submissions:** 42971
- **Solved Count:** 41063
- **URL:** https://www.hackerrank.com/challenges/cpp-variadics

## Problem Statement

A template parameter pack is a template parameter that accepts zero or more template arguments (non-types, types, or templates). To read more about parameter pack, [click here](http://en.cppreference.com/w/cpp/language/parameter_pack).

Create a template function named <em>reversed_binary_value</em>. It must take an arbitrary number of *bool* values as template parameters. These booleans represent binary digits in reverse order. Your function must return an integer corresponding to the binary value of the digits represented by the booleans. For example:  <em>reversed_binary_value<0,0,1>()</em> should return $4$.

## Input Format

The first line contains an integer, $t$, the number of test cases.
Each of the $t$ subsequent lines contains a test case. A test case is described as $2$ space-separated integers, $x$ and $y$, respectively.

* $x$ is the value to compare against.
* $y$ represents the range to compare: $64 \times y$ to $64\times y+63$.

## Output Format

Each line of output contains $64$ binary characters (i.e., $0$'s and $1$'s). Each character represents one value in the range. The *first* character corresponds to the *first* value in the range. The *last* character corresponds to the *last* value in the range. The character is $1$ if the value in the range matches $X$; otherwise, the character is $0$.

## Constraints

- $0 \le x \le 65535$  
- $0 \le y \le 1023$
- The number of template parameters passed to <em>reversed_binary_value</em> will be $\le 16$.

## Sample Input

65 1
10 0

## Sample Output

0000000000100000000000000000000000000000000000000000000000000000

## Explanation

The second character on the first line is a , because the second value in the range  is  and  is .

The eleventh character on the second line is a , because the eleventh value in the range  is  and  is .

All other characters are zero, because the corresponding values in the range do not match .
