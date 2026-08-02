# Mandragora Forest

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.7747786194388137
- **Total Submissions:** 9373
- **Solved Count:** 7262
- **URL:** https://www.hackerrank.com/challenges/mandragora

## Problem Statement

The evil forest is guarded by vicious mandragoras. Garnet and her [pet](http://finalfantasy.wikia.com/wiki/Quina) must make a journey through.  She starts with $1$ health point ($s$) and $0$ experience points.    

As she encouters each mandragora, her choices are:

1. Garnet's pet *eats* mandragora $i$. This increments $s$ by $1$ and defeats mandragora $i$.  
2. Garnet's pet *battles* mandragora $i$. This increases $p$ by $s \times H[i]$ experience points and defeats mandragora $i$. 

Once she defeats a mandragora, it is out of play.  Given a list of mandragoras with various health levels, determine the maximum number of experience points she can collect on her journey.  

For example, as always, she starts out with $s = 1$ health point and $p=0$ experience points.  Mandragoras have the following health values: $H=[3, 2, 5]$.  For each of the beings, she has two choices, $e$at or $b$attle.  We have the following permutations of choices and outcomes:
			
    Action  s	p
    _______ _   __
    e, e, e 4	0
    e, e, b	3	15
    e, b, b	2	14
    b, b, b	1	10
    b, b, e	2	10
    b, e, e	3	9
    b, e, b	2	16
    e, b, e	3	6
    
Working through a couple of rows, first, her pet can eat all three and she does not gain any experience points.  In the second row, her pet eats the first two to have $1+2=3$ health points, then battles the beast with $5$ heatlth points to gain $3 * 5 =15$ experience points.  We see that the best option is to eat the beast with $2$ points and battle the others to achieve $2 \times (3+5)=16$ experience points.

**Function Description**  

Complete the *mandragora* function in the editor below.  It must return an integer that denotes the maximum number of experience points that Garnet can earn.

mandragora has the following parameter(s):  

- *H*: an array of integers that represents the health values of mandragoras  

## Input Format

The first line contains an integer, $t$, denoting the number of test cases. Each test case is described over two lines:

1. The first line contains a single integer $n$, the number of mandragoras in the forest. 
2. The second line contains $n$ space-separated integers describing the respective health points for the mandragoras $H[H[1], H[2]...H[n]]$.  	

## Output Format

For each test case, print a single line with an integer denoting the maximum number of experience points that Garnet can earn.

## Constraints

* $1 \le t \le 10^5$   
* $1 \le n \le 10^5$   
* $1 \le H[i] \le 10^7$, where $1 \le i \le n$   
* The sum of all $n$s in a single test case is $\le 10^6$  

## Sample Input

3
3 2 2

## Explanation

There are  mandragoras having the following health points: . Initially,  and . The following is an optimal sequence of actions for achieving the maximum number of experience points possible:

- Eat the second mandragora ().  is increased from  to , and  is still .

- Battle the first mandragora ().  remains the same, but  increases by  experience points.

- Battle the third mandragora ().  remains the same, but  increases by  experience points.

Garnet earns  experience points.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
