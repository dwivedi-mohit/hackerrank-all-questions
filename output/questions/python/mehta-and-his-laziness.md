# Mehta and his Laziness

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 30
- **Success Ratio:** 0.6713166911404796
- **Total Submissions:** 4086
- **Solved Count:** 2743
- **URL:** https://www.hackerrank.com/challenges/mehta-and-his-laziness

## Problem Statement

Mehta is a very lazy boy. He always sleeps in Maths class. One day his teacher catches him sleeping and tells him that she would mark him absent for the whole semester. While she pretends to be strict, she is actually very kind-hearted. So she wants to give Mehta a chance to prove himself. She gives him a problem. If Mehta can answer it correctly, she will forgive him. Can you help Mehta find the answer to this problem?  

The problem: The teacher gives Mehta a number $N$ and asks him to find out the probability that any proper divisor of $N$ would be an even perfect square.  

**Note: Even perfect square means the number should be even and a perfect square.**  

**Input Format**  
The first line of input contains an integer $T$, the number of test cases.   
$T$ lines follow, each line containing $N$, the number that the teacher provides.  

**Output Format**  
For each test case, print in a newline the output in $p/q$ format where $p$ and $q$ are positive coprime integers.  
if $p$ is 0, you should simply output `0`.  

**Constraints**  
$1 \le T \le 4 \times 10^4$  
$2 \le N \le 10^6$  

**Sample Input**

    4
    2
    8
    36
    900

**Sample Output**

    0
    1/3
    1/8
    3/26
    
**Explaination**  
For the first case $N = 2$, the set of proper divisors is $\{1\}$. Since $1$ is not an even perfect square, the probability is $0$.    
For the second case $N = 8$, the set of proper divisors is $\{1,2,4\}$ and only $4$ is an even perfect square among them, so probability = $1/3$.  
For the third case $N = 36$, the set of proper divisors is $\{1,2,3,4,6,9,12,18\}$, and only $4$ is an even perfect square, so probability = $1/8$.  
For the fourth case $N = 900$, there will be total of $26$ proper divisors and $3$ of them $\{4,36,100\}$ are even perfect squares.   

## Input Format

The first line of input contains an integer , the number of test cases.

 lines follow, each line containing , the number that the teacher provides.

## Output Format

For each test case, print in a newline the output in  format where  and  are positive coprime integers.

if  is 0, you should simply output 0.

## Sample Input

2
8
36
900

## Sample Output

1/3
1/8
3/26

Explaination

For the first case , the set of proper divisors is . Since  is not an even perfect square, the probability is .

For the second case , the set of proper divisors is  and only  is an even perfect square among them, so probability = .

For the third case , the set of proper divisors is , and only  is an even perfect square, so probability = .

For the fourth case , there will be total of  proper divisors and  of them  are even perfect squares.
