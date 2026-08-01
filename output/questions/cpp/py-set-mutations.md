# Set Mutations

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9827492122727033
- **Total Submissions:** 170427
- **Solved Count:** 167487
- **URL:** https://www.hackerrank.com/challenges/py-set-mutations

## Problem Statement

We have seen the applications of *union, intersection, difference* and *symmetric difference* operations, but these operations do not make any changes or mutations to the set.  

**We can use the following operations to create mutations to a set:**

__.update()__ or __`|=`__ <br>
Update the set by adding elements from an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
```

__.intersection_update()__ or __`&=`__<br>
Update the set by keeping only the elements found in it and an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
```

__.difference_update()__ or __`-=`__<br>
Update the set by removing elements found in an iterable/another set.<br>
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
```

__.symmetric_difference_update()__ or __`^=`__<br>
Update the set by only keeping the elements found in either set, but not in both.
```python
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
```

---

__TASK__<br>
You are given a set $A$ and $N$ number of other sets. These $N$ number of sets have to perform some specific mutation operations on set $A$.

Your task is to execute those operations and print the sum of elements from set $A$.


## Input Format

The first line contains the number of elements in set $A$.<br>
The second line contains the space separated list of elements in set $A$.<bR>
The third line contains integer $N$, the number of other sets.<br>
The next $2*N$ lines are divided into $N$ parts containing two lines each.<br>
The first line of each part contains the space separated entries of the _operation name_ and the _length of the other set_.<br>
The second line of each part contains space separated list of elements in the other set.<bR>

$0 <$ *len(set(__A__))* $< 1000$ <br>
$0 <$ *len(otherSets)* $< 100$ <br>
$0 < N < 100$

## Output Format

Output the sum of elements in set $A$.

## Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

## Explanation

After the first operation, (intersection_update operation), we get:

set

After the second operation, (update operation), we get:

set

After the third operation, (symmetric_difference_update operation), we get:

set

After the fourth operation, ( difference_update operation), we get:

set

The sum of elements in set  after these operations is .
