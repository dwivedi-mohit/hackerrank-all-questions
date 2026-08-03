# Coding Friends

---

| Field | Value |
|---|---|
| **Slug** | `coding-friends` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/coding-friends |

---

## Preview

Can Kelly solve enough code challenges to catch up with Sam?

## Problem Statement

Can Kelly solve enough code challenges to catch up with Sam?
  


Sam and Kelly are programming buddies. Kelly resolves to practice more as Sam is ahead initially. They each solve a number of problems daily. Find the minimum number of days for Kelly to have solved more problems than Sam. If Kelly cannot surpass return -1.

 

**Example**

_samDaily = 3_

_kellyDaily = 5_

_difference = 5_

 

Initially, Sam has solved _difference_ problems more than Kelly. Each day, they solve _samDaily_ and _kellyDaily_ problems each.

Day 1: _samSolved = difference + samDaily =_ 5 + 3 = 8

_            kellySolved_ = _kellyDaily = _5

Day 2: _samSolved_ = 8 + 3 = 11

_            kellySolved_ = 5 + 5 = 10

Day 3: _samSolved_ = 11 + 3 = 14

_            kellySolved_ = 10 + 5 = 15

 

Sam is 5 problems ahead of Kelly and they solve 3 and 5 problems a day. Sam will be ahead by only 3 after the first day, 1 after the second, and Kelly will pass Sam on day 3.

 

  


**Function Description **

Complete the function _minNum_ in the editor below.

 

minNum has the following parameter(s):

    _samDaily:_  Number of problems Sam solves in a day

    _kellyDaily:_  Number of problems Kelly solves in a day

    _difference__:_  Number of problems Sam is ahead to begin

**Return**

    _int: _the minimum number of days needed by Kelly to exceed Sam, or -1 if it is impossible

 

Constraints

- _1 ≤ __samDaily__, __kellyDaily__ ≤ 100_
- _0 ≤ __difference__ ≤ 100_

  Input Format For Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer _samDaily_.

The second line contains an integer _kellyDaily_.

The third line contains an integer _ahead._

 

  Sample Case 0

**Sample Input 0**

STDIN     Function -----     -------- 3    →    samDaily = 3 5    →    kellyDaily = 5 1    →    difference = 1

 

**Sample Output 0**

1

 

**Explanation 0**

Sam is _1_ problem ahead of Kelly to begin. After _1_ day passes, Kelly will have solved _5_ problems while Sam will have only solved 1 + _3 = 4_ problems.

Sample Case 1

**Sample Input 1**

STDIN     Function -----     -------- 4    →    samDaily = 4 5    →    kellyDaily = 5 1    →    difference = 1

 

Sample Output 1 

2

 

Explanation 1

Sam is 1 problem ahead of Kelly to begin. After _1_ day passes, Kelly will have solved _5_ problems while Sam will have also solved _1 + 4 = 5_ problems. On the second day, Kelly will surpass Sam, _5 + 5 > 1 + 4 + 4_.
