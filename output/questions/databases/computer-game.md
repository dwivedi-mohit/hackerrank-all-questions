# Computer Game

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.5176832393644285
- **Total Submissions:** 3902
- **Solved Count:** 2020
- **URL:** https://www.hackerrank.com/challenges/computer-game

## Problem Statement

Sophia is playing a game on the computer. There are two random arrays A & B, each having the same number of elements. The game begins with Sophia removing a pair (A<sub>i</sub>, B<sub>j</sub>) from the array if they are not [co-prime](http://en.wikipedia.org/wiki/Coprime_integers). She keeps a count on the number of times this operation is done. 

Sophia wants to find out the maximal number of times(S) she can do this on the arrays. Could you help Sophia find the value?


## Input Format

The first line contains an integer <i>n</i>. 2 lines follow, each line containing <i>n</i> numbers separated by a single space. The format is shown below. 

    n
    A[0] A[1] ... A[n - 1]
    B[0] B[1] ... B[n - 1]


## Output Format

Output S which is the maximum number of times the above operation can be made.


## Constraints

0 < n <= 10<sup>5</sup>  
2 <= A[i], B[i] <= 10<sup>9</sup>  
Each element in both arrays are generated randomly between 2 and 10<sup>9</sup>


## Sample Input

2 5 6 7
4 9 10 12

## Explanation

You can remove:

(2, 4)
(5, 10)
(6, 9)

hence 3.
