# Marc's Cakewalk

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.966164941988084
- **Total Submissions:** 95670
- **Solved Count:** 92433
- **URL:** https://www.hackerrank.com/challenges/marcs-cakewalk

## Problem Statement

Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories.  If Marc has eaten $j$ cupcakes so far, after eating a cupcake with $c$ calories he must walk *at least* $2^j \times c$  miles to maintain his weight.

**Example**    
$calorie = [5, 10, 7]$   

If he eats the cupcakes in the order shown, the miles he will need to walk are $(2^0\times 5) + (2^1\times 10) + (2^2\times 7) = 5 + 20 + 28 = 53$.  This is not the minimum, though, so we need to test other orders of consumption.  In this case, our minimum miles is calculated as $(2^0\times 10) + (2^1\times 7) + (2^2 \times 5) = 10 + 14 + 20 = 44$.

Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes *in any order*.  

**Function Description**  

Complete the *marcsCakewalk* function in the editor below.  

marcsCakewalk has the following parameter(s):  

- *int calorie[n]:* the calorie counts for each cupcake   

**Returns**   

- *long:* the minimum miles necessary

## Input Format

The first line contains an integer $n$, the number of cupcakes in $calorie$.  
The second line contains $n$ space-separated integers, $calorie[i]$.


## Constraints

- $1 \le n \le 40$
- $1 \le c[i] \le 1000$

## Sample Input

3
1 3 2

## Sample Output

11

## Explanation

Let's say the number of miles Marc must walk to maintain his weight is . He can minimize  by eating the  cupcakes in the following order:

- Eat the cupcake with  calories, so .

- Eat the cupcake with  calories, so .

- Eat the cupcake with  calories, so .

We then print the final value of , which is , as our answer.
