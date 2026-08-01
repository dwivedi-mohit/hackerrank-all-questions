# Red John is Back

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 65
- **Success Ratio:** 0.8194686634526618
- **Total Submissions:** 19498
- **Solved Count:** 15978
- **URL:** https://www.hackerrank.com/challenges/red-john-is-back

## Problem Statement

Red John has committed another murder. This time, he doesn't leave a red smiley behind. Instead he leaves a puzzle for Patrick Jane to solve. He also texts Teresa Lisbon that if Patrick is successful, he will turn himself in. The puzzle begins as follows.  

There is a wall of size *4xn* in the victim's house. The victim has an infinite supply of bricks of size *4x1* and *1x4* in her house. There is a hidden safe which can only be opened by a particular configuration of bricks. First we must calculate the total number of ways in which the bricks can be arranged so that the entire wall is covered.  The following diagram shows how bricks might be arranged to cover walls where $1 \le n \le 4$:


![image](https://s3.amazonaws.com/hr-assets/0/1523548158-285d2d86ee-bricks.png)

There is one more step to the puzzle.  Call the number of possible arrangements $M$.   Patrick must calculate the number of prime numbers $P$ in the inclusive range $0 - M$.  

As an example, assume $n=3$.  From the diagram above, we determine that there is only one configuration that will cover the wall properly.  $1$ is not a prime number, so $P=0$.

A more complex example is $n=5$.  The bricks can be oriented in $3$ total configurations that cover the wall.  The two primes $2$ and $3$ are less than or equal to $3$, so $P=2$.


![image](https://s3.amazonaws.com/hr-assets/0/1523550290-dc87615c2f-bricks2.png)

**Function Description**  

Complete the *redJohn* function in the editor below.  It should return the number of primes determined, as an integer.  

redJohn has the following parameter(s):  

- *n*: an integer that denotes the length of the wall  

## Input Format

The first line contains the integer $t$, the number of test cases.  
Each of the next $t$ lines contains an integer $n$, the length of the $4\times n$ wall.

## Output Format

Print the integer $P$ on a separate line for each test case.


## Constraints

- $1 \le t \le 20$
- $1 \le n \le 40$

## Sample Input

1
7

## Sample Output

3

## Explanation

For , the brick can be laid in 1 format only: vertically.

The number of primes  is .

For , one of the ways in which we can lay the bricks is

There are  ways of arranging the bricks for  and there are  primes .
