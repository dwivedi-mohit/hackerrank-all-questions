# Ollivander's Inventory

- **Domain:** databases
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9423269770742695
- **Total Submissions:** 259272
- **Solved Count:** 244319
- **URL:** https://www.hackerrank.com/challenges/harry-potter-and-wands

## Problem Statement

Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand. 

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each *non-evil* wand of high power and age. Write a query to print the _id_, _age_, _coins\_needed_, and _power_ of the wands that Ron's interested in, sorted in order of descending _power_. If more than one wand has same power, sort the result in order of descending _age_.

## Input Format

The following tables contain data on the wands in Ollivander's inventory:

- _Wands:_ The _id_ is the id of the wand, _code_ is the code of the wand, _coins\_needed_ is the total number of gold galleons needed to buy the wand, and _power_ denotes the quality of the wand (the higher the power, the better the wand is). <img src="https://s3.amazonaws.com/hr-challenge-images/19502/1458538092-b2a8163a74-ScreenShot2016-03-08at12.13.39AM.png"/>

- _Wands\_Property:_ The _code_ is the code of the wand, _age_ is the age of the wand, and _is\_evil_ denotes whether the wand is good for the dark arts. If the value of _is\_evil_ is _0_, it means that the wand is not evil. The mapping between *code* and *age* is one-one, meaning that if there are two pairs, $(code_1,\ age_1)$ and $(code_2,\ age_2)$, then $code_1 \neq code_2$ and $age_1 \neq age_2$.<img src="https://s3.amazonaws.com/hr-challenge-images/19502/1458538221-18c4092b7d-ScreenShot2016-03-08at12.13.53AM.png"/>

----

## Sample Input

Wands Table:
Wands_Property Table:

## Sample Output

9 45 1647 10
12 17 9897 10
1 20 3688 8
15 40 6018 7
19 20 7651 6
11 40 7587 5
10 20 504 5
18 40 3312 3
20 17 5689 3
5 45 6020 2
14 40 5408 1

## Explanation

The data for wands of age 45 (code 1):

- The minimum number of galleons needed for

- The minimum number of galleons needed for

The data for wands of age 40 (code 2):

- The minimum number of galleons needed for

- The minimum number of galleons needed for

- The minimum number of galleons needed for

- The minimum number of galleons needed for

The data for wands of age 20 (code 4):

- The minimum number of galleons needed for

- The minimum number of galleons needed for

- The minimum number of galleons needed for

The data for wands of age 17 (code 5):

- The minimum number of galleons needed for

- The minimum number of galleons needed for
