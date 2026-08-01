# Sansa and XOR

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.9297287777386404
- **Total Submissions:** 5678
- **Solved Count:** 5279
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-sansa-and-xor

## Problem Statement

Sansa has an array. She wants to find the value obtained by [XOR](http://en.wikipedia.org/wiki/XOR#Bitwise_operation)-ing the contiguous subarrays, followed by [XOR](http://en.wikipedia.org/wiki/XOR#Bitwise_operation)-ing the values thus obtained. Determine this value.  

**Example**   
$arr=[3,4,5]$   
```
Subarray	Operation	Result
3		None		3
4		None		4
5		None		5
3,4		3 XOR 4		7
4,5		4 XOR 5		1
3,4,5		3 XOR 4 XOR 5	2
```

Now we take the resultant values and XOR them together:

$3\oplus 4\oplus 5\oplus 7\oplus 1\oplus 2=6$.  Return $6$.   

**Function Description**  

Complete the *sansaXor* function in the editor below.  

sansaXor has the following parameter(s):  

- *int arr[n]:*  an array of integers  

**Returns**   

- *int:* the result of calculations  

## Input Format

The first line contains an integer $t$, the number of the test cases.   

Each of the next $t$ pairs of lines is as follows:  
- The first line of each test case contains an integer $n$, the number of elements in $arr$.  
- The second line of each test case contains $n$ space-separated integers $arr[i]$.    


## Constraints

$1 \le t \le 5$  
$2 \le n \le 10^5$  
$1 \le arr[i] \le 10^8 $  


## Sample Input

3
1 2 3
4
4 5 7 5

## Sample Output

0

## Explanation

Test case #00:

Test case #01:
