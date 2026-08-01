# Majority

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.03253796095444685
- **Total Submissions:** 461
- **Solved Count:** 15
- **URL:** https://www.hackerrank.com/challenges/oracle1

## Problem Statement

Neo has to save the world one last time. One of the battles
has cost Neo his eyes. He has to fight the battle with the 
Deus ex machina.  

In front of Neo is a set of **N** balls, each ball is color 
coded 0/1. Deus ex machina wants Neo to figure out which
ball's color is the majority ( appears more than > N/2 ). If his choice of 
ball is correct, Deus ex machina will reach a truce and let 
humans live and if Neo fails to identify the ball with the majority, 
the entire human race would be put back into matrix.

Neo being blind won't be able to see the balls let alone figure out
the ball with the majority. He seeks the Oracle's help. Neo picks any 
two balls from the set and asks Oracle if they are of the same color 
or not. If they are the same color, the Oracle answers **YES** and if 
they are not, Oracle answers **NO**. We will call <i>b</i><sub>0/1</sub> as ball b 
with color <i>0/1</i> respectively. Majority exists in this set, i.e.,  
  
∃ <i>b</i><sub>i</sub> : |<i>b</i><sub>i</sub>| > N/2, i ∈ {0,1}

**Input Format**

First line contains 5 single space separated characters/Integers.  
1<sup>st</sup> is N which is the cardinality of the balls set.  
2<sup>nd</sup> is 0 indicating that Majority exists.  
3<sup>rd</sup> is an integer indicating the number of times oracle might lie ( 0 in this version of the game)    
4<sup>th</sup> is 2 indicating each ball can only have any of the 2 colors.  
5<sup>th</sup> is an integer 1 indicating the oracle lies exactly 0 time( ignore this number)  
**2<sup>nd</sup>** line is an integer D, D lines follow. Each line shows all 
your previous questions to Oracle. Each question is of the format 

    A B YES/NO 

0≤A,B<N 

**Constraints**

N ∈ {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}  
2 colors  
A minimum of N/2 queries must be asked to Oracle before Neo makes a guess.  
Any guess of color before that would result in losing the game.

**Output Format**

Output 2 single spaced integers which serve as indices of the balls whose colors
Oracle has to compare. When Neo is sure of the ball with the majority,
output 1 integer which is the index of the ball whose color is the majority.

**Sample Input**

    10 0 0 2 1
    2
    0 1 YES
    3 4 NO

The 1<sup>st</sup> line  says that there are 10 balls and majority exists and each ball has any
of the two colors. 2<sup>nd</sup> says that two queries were asked to oracle. The 1st 
one was whether the balls indexed at 0 and 1 are of the same color or not and the Oracle's 
reply was a YES and the 2nd one was whether the balls indexed at 3 and 4 were of the same 
color or not and the Oracle's reply was a NO.

**Sample Output**

    1 2

Neo wants to know whether the balls indexed at 1 and 2 are of the same color or not.

    1

Neo answers that the ball indexed at 1 is of the majority.

**Task**

Complete the function <i>nextQuestion</i> which takes in all the 5 integers, along with a 2-D array <i>query</i> where query[i][j] = 1 if a query 

    i j 

is asked and the Oracle says YES. The same value is set to 0 if the oracle says NO.

Note:- query[i][j] = query[j][i]

and the values is set to -1 if no query is asked
for i and j.

**Scoring**

If M queries were asked to Oracle, on correct answer
if   
M < N/2, score = 0  
M >= N-1, score = 1  
N/2 <= M < N-1, score = (N - M -1)/12

A minimum score of 1 is given for every correct submission. 


## Input Format

First line contains 5 single space separated characters/Integers.

1st is N which is the cardinality of the balls set.

2nd is 0 indicating that Majority exists.

3rd is an integer indicating the number of times oracle might lie ( 0 in this version of the game)

4th is 2 indicating each ball can only have any of the 2 colors.

5th is an integer 1 indicating the oracle lies exactly 0 time( ignore this number)

2nd line is an integer D, D lines follow. Each line shows all
your previous questions to Oracle. Each question is of the format

A B YES/NO

0≤A,B

## Output Format

Output 2 single spaced integers which serve as indices of the balls whose colors
Oracle has to compare. When Neo is sure of the ball with the majority,
output 1 integer which is the index of the ball whose color is the majority.

## Constraints

N ∈ {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

2 colors

A minimum of N/2 queries must be asked to Oracle before Neo makes a guess.

Any guess of color before that would result in losing the game.

## Sample Input

10 0 0 2 1
2
0 1 YES
3 4 NO

The 1st line  says that there are 10 balls and majority exists and each ball has any
of the two colors. 2nd says that two queries were asked to oracle. The 1st
one was whether the balls indexed at 0 and 1 are of the same color or not and the Oracle's
reply was a YES and the 2nd one was whether the balls indexed at 3 and 4 were of the same
color or not and the Oracle's reply was a NO.

## Sample Output

1 2

Neo wants to know whether the balls indexed at 1 and 2 are of the same color or not.

1

Neo answers that the ball indexed at 1 is of the majority.

Task

Complete the function nextQuestion which takes in all the 5 integers, along with a 2-D array query where query[i][j] = 1 if a query

i j

is asked and the Oracle says YES. The same value is set to 0 if the oracle says NO.

Note:- query[i][j] = query[j][i]

and the values is set to -1 if no query is asked
for i and j.

Scoring

If M queries were asked to Oracle, on correct answer
if

M < N/2, score = 0

M >= N-1, score = 1

N/2 <= M < N-1, score = (N - M -1)/12

A minimum score of 1 is given for every correct submission.
