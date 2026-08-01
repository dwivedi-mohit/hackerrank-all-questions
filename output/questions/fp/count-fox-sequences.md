# Count Fox Sequences

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 80
- **Success Ratio:** 0.7677725118483413
- **Total Submissions:** 211
- **Solved Count:** 162
- **URL:** https://www.hackerrank.com/challenges/count-fox-sequences

## Problem Statement



A non-decreasing sequence is a called a **Fox** sequence, iff the most frequent element in the sequence is unique. 

e.g. The sequence `1, 1, 2, 3, 4`  is a **Fox** sequence, because it follows the above definition. The most frequent element is 1. It occurs twice in the series, and is unique.

But the sequence `1, 1, 2, 2` is _not_ a **Fox** sequence, because there are two most frequent elements - 1 and 2. It violates the uniqueness property.

**Note**: Sequence `2, 1, 1` is not a **Fox** sequence, because it is not a non-decreasing sequence.

You need to find the number of all possible **Fox** sequences of length _n_ with elements having value between _lo_ and _hi_ inclusive.  

As the number can grow very large, return the number modulo (_10<sup>9</sup> + 7_).

**Input Format**  
The first line will contain _T_, i.e., the number of test cases.  
For each test case, there will be a single line containing three space separated integers _n, lo, hi_.

**Output Format**  
For each test case, display a single value corresponding to the number of all possible **Fox** sequences.

**Constraints**  

1  &le; T &le; 5  
1  &le; lo, hi &le; 10<sup>9</sup>  
lo &le; hi  
0  &le; \|hi - lo\| < 10<sup>5</sup>  
1  &le; n &le; 10<sup>5</sup>  

**Sample Input**

	5
	2 1 1
	2 1 3
	3 1 2
	4 4 5
	10 2 4

**Sample Output**

	1
	3
	4
	4
	60

**Explanation**  
For the first test case, `1 1` is the only possible **Fox** sequence.  
For the second test case, `1 1`, `2 2`, and `3 3` are three possible **Fox** sequences.  
For the third test case, `1 1 1`, `2 2 2`, `1 1 2`, and `1 2 2` are four possible **Fox**  
sequences.  
Rest of the test cases are up to you to figure out. 


## Input Format

The first line will contain T, i.e., the number of test cases.

For each test case, there will be a single line containing three space separated integers n, lo, hi.

## Output Format

For each test case, display a single value corresponding to the number of all possible Fox sequences.

## Constraints

1  ≤ T ≤ 5

1  ≤ lo, hi ≤ 109

lo ≤ hi

0  ≤ \|hi - lo\| < 105

1  ≤ n ≤ 105

## Sample Input

2 1 1
2 1 3
3 1 2
4 4 5
10 2 4

## Sample Output

3
4
4
60

## Explanation

For the first test case, 1 1 is the only possible Fox sequence.

For the second test case, 1 1, 2 2, and 3 3 are three possible Fox sequences.

For the third test case, 1 1 1, 2 2 2, 1 1 2, and 1 2 2 are four possible Fox

sequences.

Rest of the test cases are up to you to figure out.
