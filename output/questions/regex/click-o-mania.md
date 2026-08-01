# Click-o-Mania

- **Domain:** regex
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.02164009111617312
- **Total Submissions:** 1756
- **Solved Count:** 38
- **URL:** https://www.hackerrank.com/challenges/click-o-mania

## Problem Statement

Clickomania is a 1-player game consisting of a rectangular grid of square blocks, each colored in one of _k_ colors. Adjacent blocks horizontally and vertically of the same color are considered to be a part of the same group. A move selects a group containing at least two blocks and removes those blocks, followed by two "falling" rules; 

1. Any blocks remaining above the holes created, fall down through the same column.  
2. Any empty columns are removed by sliding the succeeding columns left.  

**Sample illustration**

![ClickoMania](https://s3.amazonaws.com/hr-assets/0/1526564633-b155b9a7b1-Clickomania.png)


In this game, you have to code a bot such that it eliminates as many possible blocks from the grid. The top left of the grid is indexed (0,0) and the bottom right of the grid is indexed 
(rows-1,columns-1). 

**Input Format**  
The first line of the input is 3 space separated integers, *x y k* where **x and y are the row index and the column index** of the grid respectively, and k is the number of colors the grid has.

An empty cell in the grid will be denoted by '-'.


**Output Format**   
Output 2 space separated integers that represent the co-ordinates of the block you choose to remove from the grid. You can output any one of the nodes of the group which you choose to remove. 


**Constraints**  
1 ≤ k ≤ 7  
Each color can be any of 'V','I','B','G','Y','O','R' (VIBGYOR)  

**Sample Input**    
  
    20 10 2
    BBRBRBRBBB
    RBRBRBBRRR
    RRRBBRBRRR
    RBRBRRRBBB
    RBRBRRRRBB
    RBBRBRRRRR
    BBRBRRBRBR
    BRBRBBRBBB
    RBBRRRRRRB
    BBRBRRBBRB
    BBBRBRRRBB
    BRBRRBRRBB
    BRRBBBBBRB
    RRBBRRBRRR
    RRRBRRRBBB
    RRRRRBBBRR
    BRRRBRRRBB
    BBBBRBRRRB
    BRBBBBBRBB
    RRRRRBBRRR


**Sample Output**  
    0 1

**Explanation**  
In this output, the player chooses to remove all the adjacent blocks of the group (*0,0*), (*0,1*) and (*1,1*) which forms one group. 

**Challenge**  
Complete the function _nextMove_ which takes integers __x__, __y__ - the row and column size of the grid, __color__ - the number of colors the grid has, and __grid__ - a 2D array of characters which is the board.

**Scoring**  
Your score depends on the number of blocks left (*count*), the size of the board and the number of colors (*k*).   
Score = (1 - count/20) x 5 x k

if count ≥ 20, a nominal score of 0.01 would be given. 

The maximum scores for the testcases of this challenge are 10, 15, 25, and 30. Hence you can get a total score of 80.                           

## Input Format

The first line of the input is 3 space separated integers, x y k where x and y are the row index and the column index of the grid respectively, and k is the number of colors the grid has.

An empty cell in the grid will be denoted by '-'.

## Output Format

Output 2 space separated integers that represent the co-ordinates of the block you choose to remove from the grid. You can output any one of the nodes of the group which you choose to remove.

## Constraints

1 ≤ k ≤ 7

Each color can be any of 'V','I','B','G','Y','O','R' (VIBGYOR)

## Sample Input

20 10 2
BBRBRBRBBB
RBRBRBBRRR
RRRBBRBRRR
RBRBRRRBBB
RBRBRRRRBB
RBBRBRRRRR
BBRBRRBRBR
BRBRBBRBBB
RBBRRRRRRB
BBRBRRBBRB
BBBRBRRRBB
BRBRRBRRBB
BRRBBBBBRB
RRBBRRBRRR
RRRBRRRBBB
RRRRRBBBRR
BRRRBRRRBB
BBBBRBRRRB
BRBBBBBRBB
RRRRRBBRRR

## Sample Output

0 1

## Explanation

In this output, the player chooses to remove all the adjacent blocks of the group (0,0), (0,1) and (1,1) which forms one group.

Challenge

Complete the function nextMove which takes integers x, y - the row and column size of the grid, color - the number of colors the grid has, and grid - a 2D array of characters which is the board.

Scoring

Your score depends on the number of blocks left (count), the size of the board and the number of colors (k).

Score = (1 - count/20) x 5 x k

if count ≥ 20, a nominal score of 0.01 would be given.

The maximum scores for the testcases of this challenge are 10, 15, 25, and 30. Hence you can get a total score of 80.
