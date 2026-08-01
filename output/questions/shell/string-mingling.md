# String Mingling

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9404883011190234
- **Total Submissions:** 7864
- **Solved Count:** 7396
- **URL:** https://www.hackerrank.com/challenges/string-mingling

## Problem Statement

Pawel and Shaka recently became friends. They believe their friendship will last forever if they merge their favorite strings.

The lengths of their favorite strings are the same, $n$. Mingling two strings, $P = p_1p_2 \ldots p_n$ and $Q = q_1q_2 \ldots q_n$, both of length $n$, will result in the creation of a new string $R$ of length $2 \times n$. It will have the following structure:

$$R= p_1q_1p_2q_2 \ldots p_nq_n$$

You are given two strings $P$ (Pawel's favorite) and $Q$ (Shaka's favorite), determine the mingled string $R$.

**Input Format** 

The first line of input contains the string $P$. <br>
The second line contains $Q$.  


**Output Format** 

Print the mingled string, $R$.   



**Constraints**  

$1 \le n \le 10^5$ <br>
The string only consists of lowercase English characters ($a-z$). <br>
*length(P) = length(Q)* $= n$

**Sample Input #00**

	abcde
	pqrst

**Sample Output #00**  

	apbqcrdset

**Sample Input #01**

	hacker
	ranker

**Sample Output #01**  

	hraacnkkeerr

**Explanation** 

*Sample Case #00:*  

$P = a\ \ \ b\ \ \ c\ \ \ d\ \ \ e$   
$Q = p\ \ \ q\ \ \ r\ \ \ s\ \ \ t$  
$R = ap\ bq\ cr\ ds\ et$  
<br>

*Sample Case #01:* 

$P = h\ \ \ a\ \ \ c\ \ \ k\ \ \ e\ \ \ r$  
$Q =	r\ \ \ a\ \ \ n\ \ \ k\ \ \ e\ \ \ r$  
$R = hr\ aa\ cn\ kk\ ee\ rr$

<br>

---
**Tested by** [Wanbo](/wanbo)


## Input Format

The first line of input contains the string .

The second line contains .

## Output Format

Print the mingled string, .

## Constraints

The string only consists of lowercase English characters ().

length(P) = length(Q)

Sample Input #00

abcde
pqrst

Sample Output #00

apbqcrdset

Sample Input #01

hacker
ranker

Sample Output #01

hraacnkkeerr

## Explanation

Sample Case #00:

Sample Case #01:

Tested by Wanbo
