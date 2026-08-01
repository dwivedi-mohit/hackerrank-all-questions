# Assignment Problem

- **Domain:** fp
- **Difficulty:** Expert
- **Max Score:** 50
- **Success Ratio:** 0.647834274952919
- **Total Submissions:** 531
- **Solved Count:** 344
- **URL:** https://www.hackerrank.com/challenges/assignment

## Problem Statement

Calvin has a math assignment at school where he has to evaluate a lot of expressions. Calvin decides to not to waste much of his time. There are $M$ expressions overall. By looking at Susie’s answers, Calvin has figured that the answers to all questions form a non decreasing sequence. 

He decides that all his answers are going to be between $1$ and $N$ (inclusive). He fills his answer sheet with a random non-decreasing sequence of length $M$ where each element is between $1$ and $N$. 

Here is the part where the real problem starts for Calvin. He does not want to choose a large value of $N$, because, he will have a lot of options to choose from. Also, if he chooses a very small value of $N$, a lot of answers would become equal and the teacher will become suspicious.  

If $x = \max_{1≤i≤N}(f(i))$, f(i) being the frequency or number of times $i$ occurs in the sequence of $M$ values he picked. Calvin wants to find out [expected value](http://en.wikipedia.org/wiki/Expected_value) of $x$. Help him solve the problem.  

For example, if $M = 3$ & $N = 3$, the possible sequences are:  

    1 1 1 (x = 3)  
    1 1 2 (x = 2)  
    1 1 3 (x = 2)  
    1 2 2 (x = 2)  
    1 2 3 (x = 1)  
    1 3 3 (x = 2)  
    2 2 2 (x = 3)  
    2 2 3 (x = 2)  
    2 3 3 (x = 2)  
    3 3 3 (x = 3)  

expected value of $x = 2.2$

**Input Format**  
The first line contains an integer $T$ which refers to the number of test cases. $T$ lines follow, each containing $2$ numbers, $M$ and $N$ for the corresponding test cases.  

**Constraints**  
$1 \le T \le 15$  
$1 \le M \le 250$  
$1 \le N \le 10^9$  

**Output Format**  
Output $T$ lines, each containing answer to the corresponding test case. Error of upto $10^{-3}$ is allowed.  

**Sample Input**  

    4
    1 5
    3 3
    2 9
    9 6

**Sample Output**  

    1.0000000000
    2.2000000000
    1.2000000000
    4.3146853147
    
**Explanation**  
For second testcase we have  

$$\begin{align*}
\text{Seq} && \text{Freq} \\\
111 && 3 \\\
112 && 2 \\\
113 && 2 \\\
122 && 2 \\\
123 && 1 \\\
133 && 2 \\\
222 && 3 \\\
223 && 2 \\\
233 && 2 \\\
333 && 3 \\\
\end{align*}$$  

$$\begin{align*}
E(x) &= \sum P_x \times x \\\
&= P_1 + 2P_2 + 3P_3 \\\
&= \frac{1}{10} + \frac{2 \times 6}{10} + \frac{3 \times 3}{10} \\\
&= \frac{22}{10}
\end{align*}$$


## Input Format

The first line contains an integer  which refers to the number of test cases.  lines follow, each containing  numbers,  and  for the corresponding test cases.

## Output Format

Output  lines, each containing answer to the corresponding test case. Error of upto  is allowed.

## Sample Input

1 5
3 3
2 9
9 6

## Sample Output

1.0000000000
2.2000000000
1.2000000000
4.3146853147

## Explanation

For second testcase we have
