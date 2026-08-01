# Day 1: Standard Deviation

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9886299807662848
- **Total Submissions:** 58751
- **Solved Count:** 58083
- **URL:** https://www.hackerrank.com/challenges/s10-standard-deviation

## Problem Statement

**Objective**	
In this challenge, we practice calculating *standard deviation*. Check out the *Tutorial* tab for learning materials and an instructional video! 

**Task**	
Given an array, $arr$, of $n$ integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of $1$ decimal place (i.e., $12.3$ format). An error margin of $\pm 0.1$ will be tolerated for the standard deviation.

**Example**   
$arr = [2, 5, 2, 7, 4]$  

The sum of the array values is $20$ and there are $5$ elements.  The mean is $4.0$.  
Subtract the mean from each element, square each result, and take their sum.  

$(2 - 4)^2 = 4$   
$(5 - 4)^2 = 1$   
$(2 - 4)^2 = 4$  
$(7 - 4)^2 = 9$   
$(4 - 4)^2 = 0$   

Their sum is 18.  Take the square root of $\frac{18}{5}$ to get $1.7$, the standard deviation.  

**Function Description**   

Complete the *stdDev* function in the editor below.  

*stdDev* has the following parameters:   
- *int arr[n]:* an array of integers   

**Prints**   
- *float:* the standard deviation to 1 place after the decimal   

## Input Format

The first line contains an integer, $n$, denoting the size of arr. 		
The second line contains $n$ space-separated integers that describe $arr$.

## Output Format

Print the *standard deviation* on a new line, rounded to a scale of $1$ decimal place (i.e., $12.3$ format).

## Constraints

- $5 \le n \le 100$  
- $0 \lt arr[i]  \le 10^{5}$   

## Sample Input

STDIN           Function
-----           --------
5               arr[] size n = 5
10 40 30 50 20  arr =[10, 40, 30, 50, 20]

## Sample Output

14.1

## Explanation

First, find the mean:

Next, calculate the squared distance from the mean, , for each :

-

-

-

-

-

Now compute , so:
