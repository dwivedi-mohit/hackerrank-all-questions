# Stock Prediction

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.6697819314641744
- **Total Submissions:** 642
- **Solved Count:** 430
- **URL:** https://www.hackerrank.com/challenges/stocks-prediction

## Problem Statement

George is very concerned about the stock options his company has granted him, because the company's stock price has fluctuated unpredictably and has often failed to meet expectations.  With this in mind, George has decided to sell his options.  Before doing so, he would like to perform a series of calculations.

Stock price history is presented as an array of positive integers, $A = \{a_0, a_1, \ldots, a_{n-1}\}$, which represents the average price per day of that stock. For a given day $d\ (0 \le d < n)$ and margin $M$, George needs to find the longest subarray containing the day's entry as a minimum,  $a_d$, and all other entries not exceeding $a_d+M$.

That is, he has to find the longest subarray, $A[l, r] = \{a_l, a_{l+1}, \ldots, a_r\}$, such that 

- $0 \le l \le d \le r < n$
- $a_d = minimum\{A[l, r]\}$
- $ \forall i \in [l, r], a_d \le a_i \le a_d + M$

George asks you to help him solve this problem.

## Input Format

The first list contains an integer $n$ which represents the length of the array $A$. The second line contains $n$ space-separated integers, $a_0, a_1, \ldots, a_{n-1}$, which represent the element of array $A$. The next line contains the number of queries $Q$. Each of the subsequent $Q$ lines contain two integers $d$ and $M$ which represent the index of the element, which should be minimal and be included in subarray, and margin, respectively.  

## Output Format

For each query output the length of the longest subarray with the required properties.

**Constraints**  
$1 \le n \le 5\cdot 10^4$  
$1 \le A[i] \le 10^9, 0 \le i < n$  
$1 \le Q \le 10^5$  
$0 \le d < n$  
$0 \le M \le 10^9$

## Sample Input

3 5 2 6 1
2
0 2
2 3

## Sample Output

3

## Explanation

Query #1: The first element, , should be included in the subarray. Since  is not less than  and does not cross the margin (), it can be included. The third element, , is less than the first element, so it cannot be included. To that end, the answer here is 2, as the longest subarray will be .

Query #2: Here  and . The next element, , is excluded because it is greater than the margin, .  All of the previous elements will be included, as they are within the allowed range . To that end, the longest subarray will be  and have a length of 3.

Tested by  Bo You
