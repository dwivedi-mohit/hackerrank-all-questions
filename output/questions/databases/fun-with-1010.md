# Fun with 1010

- **Domain:** databases
- **Difficulty:** Expert
- **Max Score:** 120
- **Success Ratio:** 0.9088235294117647
- **Total Submissions:** 340
- **Solved Count:** 309
- **URL:** https://www.hackerrank.com/challenges/fun-with-1010

## Problem Statement

When you look at photographs of watches and clocks, you'll find that they almost always show the time 10:10. There are lots of theories and even urban legends about this. For example, when showing 10:10, the hands look like a smile, and so you are more inclined to buy the watch or clock :D (a form of [subliminal advertising](http://en.wikipedia.org/wiki/Subliminal_stimuli#Consumption_and_television)).

Now, you are given $N$ and $M$. You are to find the number of sequences $A_1, A_2, \ldots, A_N$ such that:

- $A_1$ is a number of the form $1010^K$ for some $1 \le K \le M$,
- If $P = A_2 \cdot A_3 \cdots A_N$, then $A_1$ is divisible by $P$, and $P$ is divisible by $1010$, and
- $A_2, A_3, \ldots, A_N$ are squarefree.

Since the number can be very large, only give the number modulo $2000003$.

**Input Format**  
The first line of input contains a single integer $T$, which is the number of test cases. The following lines contain the test cases.

Each test case consists of one line containing two integers, $N$ and $M$.

**Constraints**  
$1 \le T \le 10^5$  
$2 \le N \le M \le 10^{12}$  

**Output Format**  
For each test case, output a single line containing the answer.

**Sample Input**  

    2
    2 3
    3 3

**Sample Output**  

    3
    62

**Explanation**  
For the first test case, the possible sequences are:  
$\{1010, 1010\}$,  
$\{1020100, 1010\}$,  
$\{1030301000, 1010\}$  



## Input Format

The first line of input contains a single integer , which is the number of test cases. The following lines contain the test cases.

Each test case consists of one line containing two integers,  and .

## Output Format

For each test case, output a single line containing the answer.

## Sample Input

2 3
3 3

## Sample Output

62

## Explanation

For the first test case, the possible sequences are:

,

,
