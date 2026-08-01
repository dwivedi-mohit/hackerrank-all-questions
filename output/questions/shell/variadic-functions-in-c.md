# Variadic functions in C

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.9677609748724186
- **Total Submissions:** 138931
- **Solved Count:** 134452
- **URL:** https://www.hackerrank.com/challenges/variadic-functions-in-c

## Problem Statement

Variadic functions are functions which take a variable number of arguments.  In C programming, a variadic function will contribute to the flexibility of the program that you are developing.

The declaration of a variadic function starts with the declaration of at least one named variable, and uses an ellipsis as the last parameter, 
e.g. 

```
int printf(const char* format, ...);
```
In this problem, you will implement three variadic functions named $sum()$, $min()$ and  $max()$ to calculate sums, minima, maxima of a variable number of arguments.  The first argument passed to the variadic function is the count of the number of arguments, which is followed by the arguments themselves.  
  


## Input Format

- The first line of the input consists of an integer $number\_of\_test\_cases$.  
- Each test case tests the logic of your code by sending a test implementation of 3, 5 and 10 elements respectively.  
- You can test your code against sample/custom input.  
- The error log prints the parameters which are passed to the test implementation.  It also prints the sum, minimum element and maximum element corresponding to your code.   

## Output Format

"Correct Answer" is printed corresponding to each correct execution of a test implementation."Wrong Answer" is printed otherwise.   

## Constraints

$1 \enspace \le \enspace number\_of\_test\_cases \enspace \le 50 $  
$1 \le element \le 1000000$ . 

## Sample Input

1

## Sample Output

Correct Answer
Correct Answer
Correct Answer
