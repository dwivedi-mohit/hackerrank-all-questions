# Reaching Points 

---

| Field | Value |
|---|---|
| **Slug** | `reaching-points` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/reaching-points |

---

## Preview

Determine if Jen's bot can reach its destination.

## Problem Statement

Determine if Jen's bot can reach its destination.

There is a bot located at a pair of integer coordinates, _(x, y)_. It must be moved to a location with another set of coordinates. Though the bot can move any number of times, it can only make the following _two types_ of moves:

 

1. From location _(x, y)_ to location _(x + y, y)_.
2. From location _(x, y)_ to location _(x, x + y)_.

 

For example, if the bot starts at _(1, 1)_, it might make the following sequence of moves: _(1, 1) → (1, 2) → (3, 2) → (5, 2)_. Note that movement will always be either up or to the right.

 

![](https://hrcdn.net/s3_pub/istreet-assets/KHpX6EsS1uRUx_ETF6HZlw/reaching_points_example.svg)

 

Given starting and target ending coordinates, determine whether the bot can reach the ending coordinates given the rules of movement.

 

  


**Function Description **

Complete the function _canReach_ in the editor below. The function must return the string _Yes_ if the bot can reach its goal, otherwise return _No_.

 

canReach has the following parameter(s):

    _x1:_  integer value, starting x coordinate

    _y1:_  integer value, starting y coordinate

    _x2:_  integer value, target x coordinate

    _y2:_  integer value, target y coordinate

 

**Constraints**

- _1 ≤ x1, y1, x2, y2 ≤ 1000_

 

  Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer _x1_, the bot's starting x coordinate.

The second line contains an integer _y1_, the bot's starting y coordinate.

The third line contains an integer _x2_, the bot's target x coordinate.

The fourth line contains an integer _y2_, the bot's target y coordinate.

 

Sample Case 0

**Sample Input 0**

1 4 5 9

 

**Sample Output 0**

Yes

 

**Explanation 0**

 

![](https://hrcdn.net/s3_pub/istreet-assets/SgZQC-GXLNGG9gcFetJsfg/reaching_points_sample_0.svg)

_start = (1, 4), end = (5, 9)_

The bot starts at _(1, 4)_ and makes a move of type _1_, meaning that it moves to _(1 + 4, 1) = (5, 4)_.

Then it makes a move of type _2_ from _(5, 4)_ to _(5, 5 + 4) = (5, 9)_.

 

Sample Case 1

**Sample Input 1**

1 2 2 1

 

**Sample Output 1**

No

 

**Explanation 1**

 

![](https://hrcdn.net/s3_pub/istreet-assets/sdbeGFYfkv1LE4QwaWh6Zw/reaching_points_sample_1.svg)

_start = (1, 2), end = (2, 1)_

Our two types of movement both require an increase in _x_ or _y_, but the input value for _y_ decreases from the _start_ location to the _end_ location. It is impossible to reach _(2, 1)_ from _(1, 2)_. The only valid moves from the starting point are shown in green.
