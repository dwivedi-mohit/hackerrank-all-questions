# Jim and the Challenge

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 90
- **Success Ratio:** 0.575
- **Total Submissions:** 240
- **Solved Count:** 138
- **URL:** https://www.hackerrank.com/challenges/jim-and-the-challenge

## Problem Statement

Hey buddy,

How are you? Last night I saw you programming on Hackerrank in my burger restauraunt. So I wonder if you can help me out on a problem I've been struggling with for like 10 hours.

It is called "The Challenge" and for some reasons the online judge always gives me TLE (Time Limit Exceeded). My code and the important part of the problem are attached with this email. I omitted the problem statement because it was three A4 sheets long and included a very boring story. 

I want you to send me an AC (Accepted) code so that I can learn from you and figure out why my implementation is so slow.

Your favourite burger cook,

Jim


PS: Tuesday is "Happy Burgers Day" so there is a -$\pi$% discount on all burgers!

###the_challenge.psc###
	### author: jim
    ### problem: the challenge
    ### status: TLE
    ### a..b : iterate from a to b ( both inclusive )
    define n, d as integers
    define H as an integer array
    define X as a two-dimensional integer array

    function m(i, j)
       for k = 1..d
          dist = dist + abs(X[i][k] - X[j][k])

    function main()
      read n and d from input
      for i = 1..n
         read H[i]
        for j = 1..d
          read X[i][j]	
      sum = 0
      for i = 1..n
          for j = i+1..n
           sum = sum + H[i] * H[j] * m(i, j)
      print sum mod 1000000009

###the_challenge.pdf###

**Input Format**

On the first line, you will be given $n$ and $d$, then $n$ lines follow, describing the $n$ points. Each point is described as $(H_i, X_{i1}, X_{i2}, ..., X_{id})$. So the first integer of each line is $H_i$, then $d$ integers follow which will describe the $X$ values of point $i$. 


**Output Format**

Print the answer to the challenge modulo $10^9 + 9$ on a single line.

**Constraints**

* $1 \leq d \leq 4$
* $1 \leq n \leq 3\cdot10^5$
* $1 \leq H_i \leq 10^6$
* $|X_{ij}| \leq 10^6$

**Sample Input**

    3 3
    5 1 2 3
    7 2 3 4
    8 4 5 6
    
**Sample Output**

	801
    
**Explanation**

Compare point 1 and point 2: Our first term of the sum is $5 \cdot 7 \cdot (|1 - 2| + |2 - 3| + |3 - 4|) = 105$.

Compare point 1 and point 3: The second term is $5 \cdot 8 \cdot (|1 - 4| + |2 - 5| + |3 - 6|) = 360$

Compare point 2 and point 3: The final term will be $7 \cdot 8 \cdot (|2 - 4| + |3 - 5| +  |4 - 6|) = 336$

So the answer is $105 + 360 + 336 = 801$.

## Input Format

On the first line, you will be given  and , then  lines follow, describing the  points. Each point is described as . So the first integer of each line is , then  integers follow which will describe the  values of point .

## Output Format

Print the answer to the challenge modulo  on a single line.

## Constraints

-

-

-

-

## Sample Input

3 3
5 1 2 3
7 2 3 4
8 4 5 6

## Explanation

Compare point 1 and point 2: Our first term of the sum is .

Compare point 1 and point 3: The second term is

Compare point 2 and point 3: The final term will be

So the answer is .
