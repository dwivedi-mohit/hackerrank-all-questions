# A Weird Function

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.5653846153846154
- **Total Submissions:** 520
- **Solved Count:** 294
- **URL:** https://www.hackerrank.com/challenges/a-weird-function

## Problem Statement

Ma5termind is going through the Euler's book of knowledge when he finds the following function: 

	def function(L,R):
    	sum=0
    	for i in range(L,R+1):				#[L,R]
            for j in range(1,i+1):			#[1,i]
            	cnt=0
            	if (j)*(j+1) == 2*i :
                	for k in range(1,i+1):	#[1,i]
                    	if __gcd(k,i)==1:	#__gcd Greatest Common Divisor 
                        	cnt+=1
                sum=sum+cnt
        return sum
        
The function seems weird as well as interesting. Don't you think ?? 

Fascinated by the function, Ma5termind codes it and successfully compiles it in the first go itself. After all, he is a good coder. Ma5termind checks the output computed by the function for all the values of $L$ and $R$ in the range $[1,100]$ and finds that the results are correct.

But as we all know, Ma5termind loves large numbers - very large numbers. When he inputs $L=1$ & $R=10^{12}$, the code does not produce any output #TimeLimitExceeded. He still wants to know the answer for such large ranges. Can you help him by writing a code that can also produce an answer for such large ranges?   

**Input Format**  
First line of input contains a single integer $T$ denoting the number of test cases. First and the only line of each test case contains two space separated integers $L$ and $R$ denoting inputs to the above function.  

**Output Format**  
Output consists of $T$ lines each containing result computed by the function when corresponding range is inputted to the function.

**Constraints**  
$1 \le T \le 10^5$  
$1 \le L \le R \le 10^{12}$

**Sample Input**  

    2
    1 10
    2 5

**Sample Output**  

    9
    2

**Explanation**  
Pass Parameters to the function and check the result.

## Input Format

First line of input contains a single integer  denoting the number of test cases. First and the only line of each test case contains two space separated integers  and  denoting inputs to the above function.

## Output Format

Output consists of  lines each containing result computed by the function when corresponding range is inputted to the function.

## Sample Input

1 10
2 5

## Sample Output

2

## Explanation

Pass Parameters to the function and check the result.
