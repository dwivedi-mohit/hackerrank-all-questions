# Build a String

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.5089900856998824
- **Total Submissions:** 11902
- **Solved Count:** 6058
- **URL:** https://www.hackerrank.com/challenges/build-a-string

## Problem Statement

Greg wants to build a string, $S$ of length $N$. Starting with an empty string, he can perform $2$ operations:<br>
	
1. Add a character to the end of $S$ for $A$ dollars.<br>
2. Copy any substring of $S$, and then add it to the end of $S$ for $B$ dollars.<br>

Calculate minimum amount of money Greg needs to build $S$.<br>

## Input Format

The first line contains number of testcases $T$.		

The $2 \times T$ subsequent lines each describe a test case over $2$ lines:		
The first contains $3$ space-separated integers, $N$, $A$ , and $B$, respectively.	
The second contains $S$ (the string Greg wishes to build).

**Constraints**

* $1 \le T \le 3$
* $1 \le N \le 3 \times 10^4$
* $1 \le A,B \le 10000$
* $S$ is composed of lowercase letters only.

## Output Format

On a single line for each test case, print the minimum cost (as an integer) to build $S$.

## Constraints

-

-

-

-  is composed of lowercase letters only.

## Sample Input

9 4 5
aabaacaba
9 8 9
bacbacacb

## Sample Output

42

## Explanation

Test Case 0:

 "";  ""

Append "";  ""; cost is

Append "";  ""; cost is

Append "";  ""; cost is

Copy and append "";  ""; cost is

Append "";  ""; cost is

Copy and append "";  ""; cost is

Summing each cost, we get , so our output for Test Case 1 is .

Test Case 1:

 "";  ""

Append "";  ""; cost is

Append "";  ""; cost is

Append "";  ""; cost is

Copy and append "";  ""; cost is

Copy and append "";  ""; cost is

Summing each cost, we get , so our output for Test Case 2 is .
