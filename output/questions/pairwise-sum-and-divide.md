# Pairwise Sum and Divide

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 20
- **Success Ratio:** 0.6848739495798319
- **Total Submissions:** 1666
- **Solved Count:** 1141
- **URL:** https://www.hackerrank.com/challenges/pairwise-sum-and-divide

## Problem Statement

You are given an array of numbers. Let us denote the array with $A[]$. Your task is very simple. You need to find the value returned by the function $\text{fun}(A)$.

    fun(A)
        sum = 0
        for i = 1 to A.length
            for j = i+1 to A.length
                sum = sum + Floor((A[i]+A[j])/(A[i]*A[j])) 
        return sum
        
In short, this function takes all distinct pairs of indexes from the array and adds the value $ \left \lfloor \frac{A[i]+A[j]}{A[i]\times A[j]}\right \rfloor$ to the sum. Your task is to find the sum.  

**Note:** $\left \lfloor \frac{A}{B} \right\rfloor$ is the integer division function.  

**Input Format**  
The first line contains $T$, the number of test cases to follow.  

Each test case contains two lines: the first line contains $N$, the size of the array, and the second line contains $N$ integers separated by spaces.  

**Output Format**  
The output should contain exactly $T$ lines where the $i^{\text{th}}$ line contains the answer for the $i^{\text{th}}$ test case.  

**Constraints**  
$1 \le T \le 15$  
$1 \le N \le 2 \times 10^5$  
$1 \le \text{Sum of $N$ over all test cases } \le 2 \times 10^5$  
$1 \le A[i] \le 10^9$  

**Sample Input**  

    2
    3
    4 2 3
    3
    1 4 1

**Sample Output**  

    0
    4
    
**Explanation**  
*First Test Case:* $\left \lfloor \frac{6}{8}\right \rfloor + \left \lfloor \frac{7}{12}\right \rfloor + \left \lfloor \frac{5}{6}\right \rfloor = 0$  
*Second Test Case:* $\left \lfloor \frac{5}{4}\right \rfloor + \left \lfloor \frac{2}{1}\right \rfloor + \left \lfloor \frac{5}{4}\right \rfloor = 4$  


## Input Format

The first line contains , the number of test cases to follow.

Each test case contains two lines: the first line contains , the size of the array, and the second line contains  integers separated by spaces.

## Output Format

The output should contain exactly  lines where the  line contains the answer for the  test case.

## Sample Input

3
4 2 3
3
1 4 1

## Sample Output

4

## Explanation

First Test Case:

Second Test Case:

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
