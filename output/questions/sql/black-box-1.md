# The Black Box

- **Domain:** sql
- **Difficulty:** Advanced
- **Max Score:** 150
- **Success Ratio:** 0.46564885496183206
- **Total Submissions:** 262
- **Solved Count:** 122
- **URL:** https://www.hackerrank.com/challenges/black-box-1

## Problem Statement

Let's define a new data structure - black box. A black box is a data structure that is capable of performing the following operations:

- add an integer to the black box
- delete an integer from the black box
- find the subset from the set of numbers present inside the black box which produce a maximal value after being [XOR](https://en.wikipedia.org/wiki/Exclusive_or)ed.

We will give you *N* queries. Each query is an addition or a deletion operation as mentioned above. After each query we ask you to find the maximal possible [XOR](https://en.wikipedia.org/wiki/Exclusive_or) that can be obtained by combining some of the numbers that are present in the black box.

**Input Format**  
The first line of input contains an integer *N*.  
Then there is a line with *N* integers, separated with single spaces. Some of the integers are positive while some are negative.  

Let's denote the i<sup>th</sup> such integer by *A<sub>i</sub>*. If it's positive, then it corresponds to the addition operation: addition of *A<sub>i</sub>* to the black box. Otherwise, it corresponds to the deletion operation: deletion of |*A<sub>i</sub>*| from the black box.

It is guaranteed that:

- we will never add a number that is already present in the black box.
- we will never delete a number that is currently not present in the black box.

**Output Format**

After each query, output the maximal XOR in a new line. If the black box has no numbers after the query, output `0`. 

**Constraints**

1 &le; *N* &le; 5 * 10<sup>5</sup>  
0 < |*A<sub>i</sub>*| &le; 2 * 10<sup>9</sup>  

**Sample Input**

<pre>6
1 2 3 4 -2 -3</pre>

**Sample Output**

<pre>1
3
3
7
7
5</pre>

**Explanation**

+ 1st Operation A = [1], maximum XOR is 1. 
+ 2nd Operation A = [1,2], maximum XOR is 1&oplus;2 = 3
+ 3rd Operation A = [1,2,3], maximum XOR is 1&oplus;2 or 3 = 3
+ 4th Operation A = [1,2,3,4], maximum XOR is 4&oplus;3 = 7
+ 5th Operation A = [1,3,4], maximum XOR is 4&oplus;3 = 7
+ 6th Operation A = [1,4], maximum XOR is 4&oplus;1 = 5

**TimeLimit**

The timelimits for this challenge is given [here](http://hr-testcases.s3.amazonaws.com/3133/tl.json), there might be chances of some submissions written in python TLEing post rerun on additional testcases, we will provide scores on a per submission basis if such a situation arises. 

## Input Format

The first line of input contains an integer N.

Then there is a line with N integers, separated with single spaces. Some of the integers are positive while some are negative.

Let's denote the ith such integer by Ai. If it's positive, then it corresponds to the addition operation: addition of Ai to the black box. Otherwise, it corresponds to the deletion operation: deletion of |Ai| from the black box.

It is guaranteed that:

- we will never add a number that is already present in the black box.

- we will never delete a number that is currently not present in the black box.

## Output Format

After each query, output the maximal XOR in a new line. If the black box has no numbers after the query, output 0.

## Constraints

1 ≤ N ≤ 5 * 105

0 < |Ai| ≤ 2 * 109

## Sample Input

1 2 3 4 -2 -3

## Sample Output

3
3
7
7
5

## Explanation

- 1st Operation A = [1], maximum XOR is 1.

- 2nd Operation A = [1,2], maximum XOR is 1⊕2 = 3

- 3rd Operation A = [1,2,3], maximum XOR is 1⊕2 or 3 = 3

- 4th Operation A = [1,2,3,4], maximum XOR is 4⊕3 = 7

- 5th Operation A = [1,3,4], maximum XOR is 4⊕3 = 7

- 6th Operation A = [1,4], maximum XOR is 4⊕1 = 5

TimeLimit

The timelimits for this challenge is given here, there might be chances of some submissions written in python TLEing post rerun on additional testcases, we will provide scores on a per submission basis if such a situation arises.
