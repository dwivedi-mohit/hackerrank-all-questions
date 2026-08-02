# Choose and Calculate

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.5468509984639017
- **Total Submissions:** 1302
- **Solved Count:** 712
- **URL:** https://www.hackerrank.com/challenges/choose-and-calculate

## Problem Statement

Animesh and Mohit are playing a game. They have $N$ balls in front of them. All the balls are numbered, not necessarily in any order. Animesh picks a set of $K$ balls from the lot each time, checks this set, puts it back into the lot, and repeats this process until all possible selections have been made. At each draw, Mohit picks two balls from these $K$ balls -- the one with the maximum number and the one with the minimum number, and notes their difference on a paper. At the end of the game, Animesh has to tell the $Sum$ of all the numbers on Mohit's paper. As value of this number can be very huge, you have to tell the value _mod_ $10^9+7$.  

**Input Format**  
The first line contains two integers $N$ and $K$.  
The next line will contain a list having $N$ numbers.  

**Output Format**  
Print the value of $Sum$  _mod_ $(10^9+7)$.  

**Constraints**  
$1 \le N \le 10^5$  
$1 \le K \le N$  
$0 \le \text{ numbers_on_ball } \le 10^9$  

**Sample Input**  

	4 2
	10 20 30 40

    
**Sample Output**  

	100

**Explanation**

There are 6 possible selections.  
1. 10 20  
2. 20 30  
3. 30 40  
4. 10 30  
5. 20 40  
6. 10 40  
Summation = 10+10+10+20+20+30 = 100

## Input Format

The first line contains two integers  and .

The next line will contain a list having  numbers.

## Output Format

Print the value of   mod .

## Sample Input

4 2
10 20 30 40

## Explanation

There are 6 possible selections.

1. 10 20

2. 20 30

3. 30 40

4. 10 30

5. 20 40

6. 10 40

Summation = 10+10+10+20+20+30 = 100

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
