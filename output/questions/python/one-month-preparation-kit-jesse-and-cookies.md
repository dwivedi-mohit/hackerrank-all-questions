# Jesse and Cookies

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.8221244500314268
- **Total Submissions:** 6364
- **Solved Count:** 5232
- **URL:** https://www.hackerrank.com/challenges/one-month-preparation-kit-jesse-and-cookies

## Problem Statement

Jesse loves cookies and wants the sweetness of some cookies to be greater than value $k$. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

*sweetness* $=  (1 \times$ *Least sweet cookie* $ +$  $2\times$ *2nd least sweet cookie*).

This occurs until all the cookies have a sweetness  $ \ge k $.  

Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return $-1$.

**Example**   
$k = 9$   
$A = [2, 7, 3, 6, 4, 6]$   

The smallest values are $2, 3$.  
Remove them then return $2 + 2 \times 3 = 8$ to the array.  Now $A = [8, 7, 6, 4, 6]$.  
Remove $4, 6$ and return $4 + 6 \times 2 = 16$ to the array.  Now $A = [16, 8, 7, 6]$.  
Remove $6, 7$, return $6 + 2 \times 7 = 20$ and $A = [20, 16, 8, 7]$.  
Finally, remove $8, 7$ and return $7 + 2 \times 8 =23$ to $A$.  Now $A = [23, 20, 16]$.  
All values are $\ge k =9$ so the process stops after $4$ iterations.  Return $4$.   

**Function Description**   
Complete the _cookies_ function in the editor below.  

_cookies_ has the following parameters:  

-	*int k:* the threshold value  
- 	*int A[n]:* an array of sweetness values  

**Returns**  

-	*int:* the number of iterations required or $-1$  

## Input Format

The first line has two space-separated integers, $n$ and $k$, the size of $A[]$ and  the minimum required sweetness respectively.   

The next line contains $n$ space-separated integers, $A[i]$.  

**Constraints**

$1 \le n \le 10^6$  
$0 \le k \le 10^9 $  
$0 \le A[i] \le 10^6$  


## Output Format

  

## Constraints

  

## Sample Input

STDIN               Function
-----               --------
6 7                 A[] size n = 6, k = 7
1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]

## Explanation

Combine the first two cookies to create a cookie with sweetness  =

After this operation, the cookies are .

Then, combine the cookies with sweetness  and sweetness , to create a cookie with resulting sweetness  =

Now, the cookies are .

All the cookies have a sweetness .

Thus,  operations are required to increase the sweetness.
