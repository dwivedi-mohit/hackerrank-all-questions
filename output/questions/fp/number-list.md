# Number List

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6549935149156939
- **Total Submissions:** 1542
- **Solved Count:** 1010
- **URL:** https://www.hackerrank.com/challenges/number-list

## Problem Statement

Sam is playing with an array, $A$, of $N$ positive integers. Sam writes a list, $S$, containing all $A$'s *[contiguous](https://en.wikipedia.org/wiki/Contiguity#Computer_science) subarrays*, and then replaces each subarray with its respective *maximum element*.

For example, consider the following $A$ where $N=3$:	
$A = \{1,2,3\}$		
Subarrays of $A$: $S_{initial} = \{ \{1\}, \{2\}, \{3\}, \{1,2\}, \{2,3\}, \{1,2,3\} \}$		
Updated (Maximum) Subarrays: $S_{maximums} = \{ \{1\}, \{2\}, \{3\}, \{2\}, \{3\}, \{3\} \}$

Help Sam determine how many numbers in $S_{maximums}$ are *greater than* $K$.


## Input Format

The first line contains a single integer, $T$ (the number of test cases). Each test case is described over two lines:	
The first line of each test case contains two space-separated integers, $N$ (the number of elements in array $A$) and $K$, respectively.		
The second line of each test case contains $N$ space-separated integers describing the elements in $A$.  

**Constraints**  
$1 \le T \le 10^{5}$  
$1 \le N \le 2 \times 10^{5}$  
$1 \le A_i \le 10^{9}$  
$0 \le K \le 10^{9}$  
$The \ sum \ of \ N \ over \ all \ test \ cases \ does \ not \ exceed \ 10^{6}$.  


## Output Format

For each test case, print the number of $maximums \gt K$ in $S_{maximums}$ on a new line.

## Constraints

.

## Sample Input

3 2
1 2 3
3 1
1 2 3

## Sample Output

5

## Explanation

Both test cases use the same  as described in the Problem Statement, so  for both test cases.

Test Case 0:

 has  elements , so we print .

Test Case 1:

 has  elements , so we print .
