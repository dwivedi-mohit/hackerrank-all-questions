# Superman Celebrates Diwali 

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.8246318607764391
- **Total Submissions:** 2988
- **Solved Count:** 2464
- **URL:** https://www.hackerrank.com/challenges/superman-celebrates-diwali

## Problem Statement

Superman has been invited to India to celebrate Diwali. Unfortunately, on his arrival he learns that he has been invited mainly to help rescue people from a fire accident that has happened in a posh residential locale of New Delhi, where rescue is proving to be especially difficult. As he reaches the place of the fire, before him there are $N$ buildings, each of the same height $H$, which are on fire. Since it is Diwali, some floors of the buildings are empty as the occupants have gone elsewhere for celebrations. In his hurry to start the rescue Superman reaches the top of the building, but realizes that his jumping power is depleted and restricted due to change in his geographical setting.
He soon understands the restrictions of his jumping power, and they are as follows: 

+ He can use the jumping power any number of times until he reaches the bottom floor, which means he can use the jumping power only until before he reaches the bottom (Ground floor), which means, once he reaches the bottom floor, he cannot move to the top floor again and try to save people. (In one single drop from the top to bottom)

+ While switching buildings, he loses height $I$ while jumping.

The second restriction is explained below with an example.

Assume $I = 2$. Now Superman is in the 2<sup>nd</sup> building 5<sup>th</sup> floor ($B = 2$, $F = 5$). If he wants to switch to the fifth building ($B = 5$), he will lose height ($I = 2$), which means he will be at floor _3_ at building _5_ ($B = 5$, $F = 3$). He can jump freely from the current floor to the floor below on the same building . That is, suppose if he is at $(B = 5, F = 4)$, he can go to $(B = 5, F = 3)$ without any restrictions. He cannot skip a floor while jumping in the same building. He can go to the floor below the current floor of the same building or use his jumping power, switch building, and lose height $I$.

Given the information about the occupied floors in each of the $N$ buildings, help Superman to determine the maximum number of people he can save in one single drop from the top to the bottom floor with the given restrictions.

## Input Format

Input starts with three values:  the number of buildings $N$, the height of the buildings $H$, and the height Superman will lose when he switches buildings $I$.

These are followed by $N$ lines. Each $i^{th}$ line starts with a non negative integer $u$ indicating how many people are in the $i$<sup>th</sup> building. Each of the following $u$ integers indicates that a person is at height $u_i$ in the $i^{th}$ buiding. Each of the following $u$ integers are given and repetitions are allowed which means there can be more than one person in a floor.

$i$ indicates building number and $j$ indicates floor number. Building number will not be given; since $N$ lines follow the first line, you can assume that the $i^{th}$ line indicates the $i^{th}$ building's specifications.

**Constraints**  
$1 \le H,N \le 1900$  
$1 \le I \le 450$  
$0 \le u \le 1900$ (for each $i$, which means the maximum number of people in a particular building will not exceed $1900$)    
$1 \le u_{ij} \le H$

## Output Format

Output the maximum number of people Superman can save.

## Constraints

(for each , which means the maximum number of people in a particular building will not exceed )

## Sample Input

4 15 2
5 1 1 1 4 10
8 9 5 7 7 3 9 8 8
5 9 5 6 4 3
0

## Explanation

Input starts with , ,  .

 lines follow. Each line describes building .

Each line begins with , which denotes the number of persons in a particular building, followed by floor number, where each person resides. Floor number can repeat as any number of people can reside on a particular floor.

I've attached a figure here to explain the sample test case.

You can verify the first building's specifications with the figure.

 (Total number of persons in the first building), followed by 1 1 1 4 10(Floor numbers).

 floor = 3 persons.

 floor = 1 person.

 floor = 1 person.

Similarly, the specifications for the other three buildings follow.

The connected line shows the path which Superman can use to save the maximum number of people. In this case, that number is .

You can also note in the figure that when he switches from Building 2 to Building 3, he loses height  (). Similarly, when he switches from Building 3 to Building 1 ,the same height loss happens as mentioned in the problem statement.
