# Halloween party

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.934996045753525
- **Total Submissions:** 51843
- **Solved Count:** 48473
- **URL:** https://www.hackerrank.com/challenges/halloween-party

## Problem Statement

Alex is attending a Halloween party with his girlfriend, Silvia. At the party, Silvia spots the corner of an infinite chocolate bar (two dimensional, infinitely long in width and length).  

If the chocolate can be served only as 1 x 1 sized pieces and Alex can cut the chocolate bar exactly $K$ times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?

**Input Format**  
The first line contains an integer $T$, the number of test cases. $T$ lines follow.<br>
Each line contains an integer $K$.  

**Output Format**<br>
$T$ lines; each line should contain an integer that denotes the maximum number of pieces that can be obtained for each test case.<br>

**Constraints**<br>
$1 \le T \le 10$<br>
$2 \le K \le 10^7$<br>

**Note**: Chocolate must be served in _1 x 1_ sized pieces. Alex can't relocate any of the pieces, nor can he place any piece on top of another.

**Sample Input #00**  

    4
    5
    6
    7
    8
    
**Sample Output #00**  

    6
    9
    12
    16
    
**Explanation**<br>
The explanation below is for the first two test cases. The rest of them follow a similar logic.<br>

For the first test-case where $K = 5$, you need $3$ horizontal and $2$ vertical cuts.<br> 
![halloweenboard](https://hr-challenge-images.s3.amazonaws.com/halloween-party.jpg)
For the second test case, where $K = 6$, you need $3$ horizontal and $3$ vertical cuts.

## Input Format

The first line contains an integer , the number of test cases.  lines follow.

Each line contains an integer .

## Output Format

lines; each line should contain an integer that denotes the maximum number of pieces that can be obtained for each test case.

## Constraints

Note: Chocolate must be served in 1 x 1 sized pieces. Alex can't relocate any of the pieces, nor can he place any piece on top of another.

Sample Input #00

4
5
6
7
8

Sample Output #00

6
9
12
16

## Explanation

The explanation below is for the first two test cases. The rest of them follow a similar logic.

For the first test-case where , you need  horizontal and  vertical cuts.

For the second test case, where , you need  horizontal and  vertical cuts.
