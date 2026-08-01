# Sherlock and The Beast

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.833923582622784
- **Total Submissions:** 96287
- **Solved Count:** 80296
- **URL:** https://www.hackerrank.com/challenges/sherlock-and-the-beast

## Problem Statement

Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their supercomputer, *The Beast*. 

Shortly after resolving to investigate, Sherlock receives a note from Moriarty boasting about infecting *The Beast* with a virus.  He also gives him a clue:  an integer. Sherlock determines the key to removing the virus is to find the largest *Decent Number* having that number of digits.

A _Decent Number_ has the following properties:

1. Its digits can only be _3_'s and/or _5_'s.
2. The number of _3_'s it contains is divisible by _5_.
3. The number of _5_'s it contains is divisible by _3_.
4. It is the largest such number for its length. 

Moriarty's virus shows a clock counting down to *The Beast*'s destruction, and time is running out fast. Your task is to help Sherlock find the key before *The Beast* is destroyed!

For example, the numbers $55533333$ and $555555$ are both decent numbers because there are $3$ $5$'s and $5$ $3$'s in the first, and $6$ $5$'s in the second.  They are the largest values for those length numbers that have proper divisibility of digit occurrences.  

**Function Description**

Complete the *decentNumber* function in the editor below.     

decentNumber has the following parameter(s):  

- *int n:* the length of the decent number to create  

**Prints**  

Print the decent number for the given length, or $-1$ if a decent number of that length cannot be formed. No return value is expected.  


## Input Format

The first line is an integer, $t$, the number of test cases. 

The next $t$ lines each contain an integer $n$, the number of digits in the number to create.



## Constraints

$1 \le t \le 20$  
$1 \le n \le 100000$  

## Sample Input

STDIN   Function
-----   --------
4       t = 4
1       n = 1 (first test case)
3       n = 3 (second test case)
5
11

## Sample Output

-1
555
33333
55555533333

## Explanation

For , there is no Decent Number having  digit, so print .

For ,  is the only possible number. (Decent Number Property 3).

For ,  is the only possible number. (Decent Number Property 2).

For ,  is the Decent Number.  All other permutations of these digits are not decent (Decent Number Property 4).
