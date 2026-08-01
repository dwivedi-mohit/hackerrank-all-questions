# Police Operation

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.7095571095571096
- **Total Submissions:** 2145
- **Solved Count:** 1522
- **URL:** https://www.hackerrank.com/challenges/police-operation

## Problem Statement

Roy is helping the police department of his city in crime fighting. Today, they informed him about a new planned operation.

Think of the city as a $2D$ plane. The road along the $X$-axis is very crime prone, because $n$ criminals live there. No two criminals live at the same position.

To catch these criminals, the police department has to recruit some police officers and give each of them USD $h$ as wages. A police officer can start his operation from any point $a$, drive his car to point $b$ in a straight line, and catch all the criminals who live on this way. The cost of fuel used by the officer's car is equal to the square of the euclidean distance between points $a$ and $b$ (Euclidean distance between points $(x_1,y_1)$ and $(x_2,y_2)$ equals to $\sqrt{ (x_1-x_2)^2 + (y_1-y_2)^2 }$ ).

The police department asks Roy to plan this operation. So Roy has to tell them the number of officers to recruit and the routes these officers should take in order to catch all the criminals. Roy has to provide this information while minimizing the total expenses of this operation.

Find out the minimum amount of money required to complete the operation.


## Input Format

The first line contains two integers $n$ $(0 \le n \le 2 \times 10^{6})$, number of criminals, and $h$ $( 0 \le h \le 10^{9} )$, the cost of recruiting a police officer. The next line contains $n$ space separated integers. The $i^{th}$ integer indicates the position of the $i^{th}$ criminal on $X$-axis (in other words, if the $i^{th}$ integer is $x$, then location of the $i^{th}$ criminal is $(x,0)$). The value of the positions are between $1$ and $10^9$ and are given in increasing order in the input.


## Output Format

Print the minimum amount of money required to complete the operation.


## Sample Input

5 10
1 4 5 6 9

## Explanation

For the sample test case, police department recruits  officers who get paid . The first officer starts at point  and catches the criminal there. So he does not use any fuel. The second officer catches criminals at points ,  and . He burns fuel worth USD . The third officer catches the criminal at point . He also does not burn any fuel. The total money spent by the department is, .

Timelimits

Timelimits for this challenge are given here
