# GCD Sequence

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.8535031847133758
- **Total Submissions:** 314
- **Solved Count:** 268
- **URL:** https://www.hackerrank.com/challenges/gcd-sequence

## Problem Statement

How many non decreasing sequences are there of length $K$, with the condition that numbers in sequence can take values only from $1,2,3, \cdots N$ and gcd of all numbers in the sequence must be $1$.

**Input Format**  
The first line contains an integer $T$ i.e. the number of test cases.<br>
$T$ lines follow, each line containing two integers $N$ and $K$ separated by a single space.  

**Output Format**  
For each testcase, print in a newline the answer $\mod(10^9+7)$. 

**Constraints**  

$ 1 \le T \le 5$  
$ 1 \le N \le  10^5$  
$ 1 \le K \le 10^5$  


**Sample Input**

	4
    2 4 
    3 4
    5 2
    1 10


**Sample Output**

	4
    13
    10
    1


**Explanation**

For the first testcase, the sequences are 
    
    (1,1,1,1), (1,1,1,2), (1,1,2,2), (1,2,2,2) = 4

For the second testcase, the sequences are 

    (1,1,1,1), (1,1,1,2), (1,1,1,3), (1,1,2,2), (1,1,2,3), (1,1,3,3)
    (1,3,3,3), (1,2,2,2), (1,2,2,3), (1,2,3,3), (2,2,2,3), (2,2,3,3), (2,3,3,3)
    
which are 13 in number.  
    
For the third testcase, the sequences are  

    (1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3, 4), (3, 5), (4, 5) = 10
    
for the fourth testcase, the only sequence is 

    (1,1,1,1,1,1,1,1,1,1)



## Input Format

The first line contains an integer  i.e. the number of test cases.

 lines follow, each line containing two integers  and  separated by a single space.

## Output Format

For each testcase, print in a newline the answer .

## Sample Input

2 4
3 4
5 2
1 10

## Sample Output

13
10
1

## Explanation

For the first testcase, the sequences are

(1,1,1,1), (1,1,1,2), (1,1,2,2), (1,2,2,2) = 4

For the second testcase, the sequences are

(1,1,1,1), (1,1,1,2), (1,1,1,3), (1,1,2,2), (1,1,2,3), (1,1,3,3)
(1,3,3,3), (1,2,2,2), (1,2,2,3), (1,2,3,3), (2,2,2,3), (2,2,3,3), (2,3,3,3)

which are 13 in number.

For the third testcase, the sequences are

(1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3, 4), (3, 5), (4, 5) = 10

for the fourth testcase, the only sequence is

(1,1,1,1,1,1,1,1,1,1)
