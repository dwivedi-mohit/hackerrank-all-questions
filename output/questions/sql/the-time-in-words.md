# The Time in Words

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 25
- **Success Ratio:** 0.9305450236966825
- **Total Submissions:** 126600
- **Solved Count:** 117807
- **URL:** https://www.hackerrank.com/challenges/the-time-in-words

## Problem Statement


Given the time in numerals we may convert it into words, as shown below:  

$$\begin{align*} 
\text{5:00} & \rightarrow  ~ \text{five o' clock}  \\\
\text{5:01} & \rightarrow  ~ \text{one minute past five}  \\\
\text{5:10} & \rightarrow ~ \text{ten minutes past five}  \\\
\text{5:15} & \rightarrow ~ \text{quarter past five}  \\\
\text{5:30} & \rightarrow ~ \text{half past five}  \\\
\text{5:40} & \rightarrow ~ \text{twenty minutes to six}  \\\
\text{5:45} & \rightarrow ~ \text{quarter to six}  \\\
\text{5:47} & \rightarrow ~ \text{thirteen minutes to six}  \\\
\text{5:28} & \rightarrow ~ \text{twenty eight minutes past five}
\end{align*}$$

At $minutes = 0$, use _o' clock_.  For $1 \leq minutes \leq 30$, use _past_, and for $30 \lt minutes$ use _to_.  Note the space between the apostrophe and _clock_ in _o' clock_.  Write a program which prints the time in words for the input given in the format described.  

**Function Description**  

Complete the *timeInWords* function in the editor below.  

timeInWords has the following parameter(s):  

- *int h:* the hour of the day  
- *int m:* the minutes after the hour  

**Returns**  

- *string:* a time string as described  

## Input Format

The first line contains $h$, the hours portion 
The second line contains $m$, the minutes portion  



## Constraints

+ $1 \le h \le 12$  
+ $0 \le m \lt 60$

## Sample Input

5
47

## Sample Output

thirteen minutes to six
