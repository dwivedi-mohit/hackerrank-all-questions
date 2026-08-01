# Klotski

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 150
- **Success Ratio:** 0.8405797101449275
- **Total Submissions:** 414
- **Solved Count:** 348
- **URL:** https://www.hackerrank.com/challenges/klotski

## Problem Statement

<sup>The *time limit* for this challenge is 4 times the [standard time limit](https://www.hackerrank.com/environment).</sup>

Klotski is a classical puzzle.  In this puzzle, you are given a rectangle box of a fixed size with some blocks inside of it. One of these blocks is special, we will call it the "*target*" block. To solve this puzzle, you will need to slide blocks within this box to move the *target* block to a specified place.

To slide a block, you must follow certain rules:

* Blocks can only be moved in four directions: _up, down, left and right_.
* Overlapping blocks are not allowed.
* Blocks can never be moved outside of the box.

Your task is to find one optimal solution for the Klotski puzzle. A solution consists of a sequence of moves that takes the puzzle from its initial state, to a solved state.
<br>
For a solution to be considered optimal, there should not be another sequence of moves whose length is less than the current solution.  

Note that the definition of "*one move*" might be different from what you might expect. In the puzzle, you might choose one block and move it anywhere, as long as the above rules are followed. As long as you don't change the block you are currently moving, the whole sequence of movements counts as only one move, regardless of how far that block has moved.  Examples will be given in following sections.  

**Input format**  
Two integers, $m$ and $n$, are given in the first line, where $m$ is the number of rows and $n$ is the number of columns.   
In the following $m$ lines, each line contains $n$ strings separated by spaces.  
Each character in the string describes one cell of the Klotski puzzle.  
A string consists only of '.'s (e.g. ".", "..."), which stands for empty cells, while other strings encode blocks.  
The next line contains one string, which indicates the target block.  
The last line contains a coordinate that specifies the place where the target block should be moved to. This coordinate is the top-left corner where the target block should be placed.  

For example, you might be given a puzzle like this:

    3 4
    A A C .
    A B C .
    B B . .
    B
    0 1

This Klotski puzzle consists of 3 blocks:

	# Block "A", top-left corner is (0,0)

    A A . .
	A . . .
	. . . .
    
    # Block "B", top-left corner is (1,0)

	. . . .
	. B . .
	B B . .
    
    # Block "C", top-left corner is (0,2)

	. . C .
	. . C .
	. . . .
    
Note that *the top-left corner* means the topmost and leftmost coordinate
of a block, which might be outside of the block. See block $B$ for an example.  
<br>
To solve this puzzle, block $B$ should be placed in the following place:

	. . B .
    . B B .
    . . . .
    
**Output format**  
The first line is an integer $k$, indicating the number of moves in an optimal solution.  
In the following $k$ lines, you should output a sequence of moves indicating one possible optimal solution. Each line describes a move in the following format:

	<block name> <from> <to>
    
which means to move the block $<block\ name>$ whose top-left corner is $<from>$ to a place where its top-left corner is $<to>$.
    
For example, with the example input above:

    3 4
    A A C .
    A B C .
    B B . .
    B
    0 1

One of the possible outputs is:

	2
	C (0,2) (1,3)
	B (1,0) (0,1)


This means one optimal solution consists of 2 moves.   
First we move block $C$ from $(0, 2)$ to $(1, 3)$:

    A A . .
    A B . C
    B B . C
    
And then we move block $B$ from $(1, 0)$ to $(0, 1)$:

	A A B .
    A B B C
    . . . C

**Constraints**  

- $1 \le m,n \le 6$
- Block size won't exceed $3\times 3$.
- All inputs are guaranteed to be solvable within 201 steps, i.e. $0 \le k \le 200$.

**Notes**  

- In the case where there are multiple solutions to the puzzle, you only need to print one of them.
- Test cases will not be overly difficult, being a little wise about states and your program should have enough time to work out this challenge.
- If you want to do a search, taking block shapes into account will save you some space.

**Sample Input**  

	3 4
	A A C .
	A B C .
	B B . .
	B
	0 1

**Sample Output**  

	2
	C (0,2) (1,3)
	B (1,0) (0,1)


---

**Tested by** [Patrick Spettel](https://www.hackerrank.com/patsp) 
<br>



## Constraints

-

- Block size won't exceed .

- All inputs are guaranteed to be solvable within 201 steps, i.e. .

Notes

- In the case where there are multiple solutions to the puzzle, you only need to print one of them.

- Test cases will not be overly difficult, being a little wise about states and your program should have enough time to work out this challenge.

- If you want to do a search, taking block shapes into account will save you some space.

## Sample Input

3 4
A A C .
A B C .
B B . .
B
0 1

## Sample Output

C (0,2) (1,3)
B (1,0) (0,1)

Tested by Patrick Spettel
