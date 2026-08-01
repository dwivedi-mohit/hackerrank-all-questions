# Crossword Puzzle

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.8466854979265581
- **Total Submissions:** 16639
- **Solved Count:** 14088
- **URL:** https://www.hackerrank.com/challenges/crossword-puzzle

## Problem Statement

A $10 \times 10$ Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid.  Cells are marked either `+` or `-`.  Cells marked with a `-` are to be filled with the word list.  

The following shows an example crossword from the input $crossword$ grid and the list of words to fit, $words = [POLAND,LHASA,SPAIN,INDIA]$:

```
Input 	   		Output

++++++++++ 		++++++++++
+------+++ 		+POLAND+++
+++-++++++ 		+++H++++++
+++-++++++ 		+++A++++++
+++-----++ 		+++SPAIN++
+++-++-+++ 		+++A++N+++
++++++-+++ 		++++++D+++
++++++-+++ 		++++++I+++
++++++-+++ 		++++++A+++
++++++++++ 		++++++++++
POLAND;LHASA;SPAIN;INDIA
```

**Function Description**

Complete the *crosswordPuzzle* function in the editor below.  It should return an array of strings, each representing a row of the finished puzzle.

crosswordPuzzle has the following parameter(s):  
  
- *crossword*: an array of $10$ strings of length $10$ representing the empty grid  
- *words:* a string consisting of semicolon delimited strings to fit into $crossword$  



## Input Format

Each of the first $10$ lines represents $crossword[i]$, each of which has $10$ characters, $crossword[i][j]$.
  
The last line contains a string consisting of semicolon delimited $words[i]$ to fit.  

## Output Format

Position the words appropriately in the $10 \times 10$ grid, then return your array of strings for printing.  

## Constraints

$1 \le | words | \le 10$  
$crossword[i][j] \in \{+,-\}$  
$words[i][j] \in ascii[A-Z]$  


## Sample Input

+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA

## Sample Output

+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++
