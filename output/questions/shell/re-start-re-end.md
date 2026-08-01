# Re.start() & Re.end()

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9416373803682337
- **Total Submissions:** 90486
- **Solved Count:** 85205
- **URL:** https://www.hackerrank.com/challenges/re-start-re-end

## Problem Statement

###<sub>[start() & end()](https://docs.python.org/2/library/re.html#re.MatchObject.start)</sub>

These expressions return the indices of the *start* and *end* of the substring matched by the group.

<sub>__Code__</sub>  

    >>> import re
    >>> m = re.search(r'\d+','1234')
    >>> m.end()
    4
    >>> m.start()
    0
    
---
__Task__  
You are given a string $S$.  
Your task is to find the indices of the *start* and *end* of string $k$ in $S$.

## Input Format

The first line contains the string $S$.  
The second line contains the string $k$.

__Constraints__  

$ 0 < len(S) < 100$  
$ 0 < len(k) < len(S)$

## Output Format

Print the tuple in this format: (_start_ __index_, _end_ __index_).   
If no match is found, print `(-1, -1)`.

## Sample Input

aaadaa
aa

## Sample Output

(0, 1)
(1, 2)
(4, 5)
