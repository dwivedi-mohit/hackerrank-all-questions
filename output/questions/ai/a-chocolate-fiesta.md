# A Chocolate Fiesta

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 40
- **Success Ratio:** 0.666933066933067
- **Total Submissions:** 5005
- **Solved Count:** 3338
- **URL:** https://www.hackerrank.com/challenges/a-chocolate-fiesta

## Problem Statement

Welcome to the exciting class of Professor Manasa. In each lecture she used to play some game while teaching a new concept. Today's topic is Set Theory. For today's game, she had given a set _A = {a<sub>1</sub>, a<sub>2</sub>, ...a<sub>N</sub>}_ of _N_ integers to her students and asked them to play the game as follows.  

At each step of the game she calls a random student and asks him/her to select a non-empty subset from set _A_ such that this subset had not been selected earlier and the sum of subset should be even. This game ends when all possible subsets had been selected. Manasa needs your help in counting the total number of times students can be called assuming each student gives the right answer. **While it is given that if two numbers are same in the given set, they have different colors. It means that if a1 = a2, then choosing a1 and choosing a2 will be considered as different sets**. 

**Note**  

1. Two subsets are different if there exists an element _(a<sub>k</sub>)_ that is present in one subset but not in other. Let's say set _A = {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>} = {2, 2, 3}_, then all possible subsets are _{}, {a<sub>1</sub>}, {a<sub>2</sub>}, {a<sub>3</sub>}, {a<sub>1</sub>, a<sub>2</sub>}, {a<sub>1</sub>, a<sub>3</sub>}, {a<sub>2</sub>, a<sub>3</sub>}, {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>}_ which is equivalent to _{}, {2}, {2}, {3}, {2, 2}, {2, 3}, {2, 3}, {2, 2, 3}_.  

2. Students can be called multiple times.  

 

**Input Format**  
The first line contains an integer _N_ i.e. size of set _A_.  
Next line will contain _N_ integers, each representing an element of _A_.  

**Output Format**  
Print number of time students are called. As this number can be very large you have to print the answer _modulo (10<sup>9</sup> + 7)_. 

**Constraints**  
1 &le; _N_ &le; 10<sup>5</sup>  
0 &le; _a<sub>i</sub>_ &le; 10<sup>4</sup> , where _i &isin; [1 .. N]_

**Sample Input 00**  

	4
	2 4 6 1
    
**Sample Output 00**  

	7
    
**Sample Input 01**  

	3
    1 2 2
    
**Sample Output 01**  

	3
    
**Explanation**  
There are 7 different ways in which a non-empty subset, with even sum, can be selected, i.e., _{2}, {4}, {6}, {2, 4}, {2, 6}, {4, 6}, {2, 4, 6}_.<br>

For second sample test case, there are 3 different ways in which a non-empty subset, with even sum, can be selected, i.e., _{a<sub>2</sub>}, {a<sub>3</sub>}, {a<sub>2</sub>, a<sub>3</sub>}_ which is equivalent to _{2}, {2}, {2,2}_.



## Input Format

The first line contains an integer N i.e. size of set A.

Next line will contain N integers, each representing an element of A.

## Output Format

Print number of time students are called. As this number can be very large you have to print the answer modulo (109 + 7).

## Constraints

1 ≤ N ≤ 105

0 ≤ ai ≤ 104 , where i ∈ [1 .. N]

## Sample Input

4
2 4 6 1

## Sample Output

7

## Explanation

There are 7 different ways in which a non-empty subset, with even sum, can be selected, i.e., {2}, {4}, {6}, {2, 4}, {2, 6}, {4, 6}, {2, 4, 6}.

For second sample test case, there are 3 different ways in which a non-empty subset, with even sum, can be selected, i.e., {a2}, {a3}, {a2, a3} which is equivalent to {2}, {2}, {2,2}.
