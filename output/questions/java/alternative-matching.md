# Alternative Matching

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9452312488242723
- **Total Submissions:** 37211
- **Solved Count:** 35173
- **URL:** https://www.hackerrank.com/challenges/alternative-matching

## Problem Statement

*Alternations*, denoted by the `|` character, match a single item out of several possible items separated by the vertical bar. When used inside a character class, it will match characters; when used inside a group, it will match entire expressions (i.e., everything to the left or everything to the right of the vertical bar). We must use parentheses to limit the use of alternations. 

![ach17.png](https://s3.amazonaws.com/hr-challenge-images/14623/1449645537-1ecd61e235-ach17.png)
$$\textit{In the image above, the RegEx pattern is matched with the test string.}$$

For example:

- `(Bob|Kevin|Stuart)` will match either `Bob` or `Kevin` or `Stuart`.  
- `([a-f]|[A-F])` will match any of the following characters: `a`, `b`, `c`, `d`, `e`, `f`, `A`, `B`, `C`, `D`, `E`, or `F`. 

----

__Task__ 

Given a test string, $s$, write a RegEx that matches $s$ under the following conditions:  

- $s$ must start with `Mr.`, `Mrs.`, `Ms.`, `Dr.` or `Er.`.  
- The rest of the string must contain only *one or more* English alphabetic letters (upper and lowercase).

**Note:** This is a RegEx-only challenge. You are not required to write code; you simply need to fill in the blank.
