# Text Alignment

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9596521821095296
- **Total Submissions:** 424360
- **Solved Count:** 407238
- **URL:** https://www.hackerrank.com/challenges/text-alignment

## Problem Statement

In Python, a string of text can be aligned *left, right* and *center*.

__.ljust(width)__

This method returns a left aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  

---    
__.center(width)__

This method returns a centered string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----

---
__.rjust(width)__

This method returns a right aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank
    
---
__Task__

You are given a partial code that is used for generating the _HackerRank Logo_ of variable _thickness_.  
Your task is to replace the blank (`______`) with *rjust, ljust* or *center*.




## Input Format

 A single line containing the _thickness_ value for the logo.
 
 __Constraints__  

The *thickness* must be an *odd* number.  
$ 0 < thickness < 50$

## Output Format

Output the desired logo.

## Constraints

The thickness must be an odd number.

## Sample Output

H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
                    HHHHHHHHH
                     HHHHHHH
                      HHHHH
                       HHH
                        H
