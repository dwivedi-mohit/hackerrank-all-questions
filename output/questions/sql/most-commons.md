# Company Logo

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9121392450011633
- **Total Submissions:** 163338
- **Solved Count:** 148987
- **URL:** https://www.hackerrank.com/challenges/most-commons

## Problem Statement

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string $s$, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

- Print the three most common characters along with their occurrence count.
- Sort in descending order of occurrence count.  
- If the occurrence count is the same, sort the characters in alphabetical order.   

For example, according to the conditions described above, 

$\color{green}\texttt{G}\color{red}\texttt{OO}\color{green}\texttt{G}\color{black}\texttt{LE}$ would have it's logo with the letters $\color{green}\texttt{G},\color{red}\texttt{O},\color{black}\texttt{E}$. 




## Input Format

A single line of input containing the string $S$.  



## Output Format

Print the three most common characters along with their occurrence count each on a separate line.  
Sort output in descending order of occurrence count.  
If the occurrence count is the same, sort the characters in alphabetical order.  

## Constraints

+ $ 3 < len(S) \le 10^4 $   
+ $S$ has at least $3$ distinct characters   

## Sample Input

aabbbccde

## Sample Output

b 3
a 2
c 2

## Explanation

Here, b occurs  times. It is printed first.

Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.
