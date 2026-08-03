# Cut Them All

## Metadata

- **ID:** 658462
- **Type:** code
- **Difficulty:** 8.333333333333334
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Greedy Algorithms, Easy, Interviewer Guidelines
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates greedy algorithms, problem solving, and array manipulation concepts, ideal for junior-level roles. The problem requires determining if a rod can be cut into segments while satisfying a minimum length constraint for the final cut.

## Problem Statement

You are given an array lengths of size n, where each element represents the length of a required segment. The total length of the uncut rod is equal to the sum of all values in lengths.

You must perform exactly n - 1 cuts to obtain the required segments.

The machine used for cutting has a constraint:

	
- The final cut must be made on a rod whose length is greater than or equal to minLength

Determine whether it is possible to plan the sequence of cuts such that:

	
- All n - 1 cuts are completed
	
- The rod used for the final cut satisfies the minimum length requirement

Return "Possible" if it can be done, otherwise return "Impossible".

 

Example

n = 3

lengths = [4, 3, 2]

minLength = 7

 

The rod is initially sum(lengths) = 4 + 3 + 2 = 9 units long. First cut off the segment of length 4 + 3 = 7 leaving a rod 9 - 7 = 2.  Then check that the length 7 rod can be cut into segments of lengths 4 and 3. Since 7 is greater than or equal to minLength = 7, the final cut can be made. Return "Possible"

 

Example

n = 3

lengths = [4, 2, 3]

minLength = 7

 

The rod is initially sum(lengths) = 4 + 2 + 3 = 9 units long. In this case, the initial cut can be of length 4 or 4 + 2 = 6.  Regardless of the length of the first cut, the remaining piece will be shorter than minLength. Because n - 1 = 2 cuts cannot be made, the answer is "Impossible"

 

Function Description

Complete the function cutThemAll in the editor with the following parameter(s):

    int lengths[n]:  the lengths of the segments, in order

    int minLength: the minimum length the machine can accept

 

Returns

    string: "Possible" if all n-1 cuts can be made. Otherwise, return the string "Impossible"

 

Constraints

	
- 2 ≤ n ≤ 105

	
- 1 ≤ t ≤ 109
	
- 
1 ≤ lengths[i] ≤ 109 
	
- The sum of the elements of lengths equals the uncut rod length.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, the number of elements in lengths.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, lengths[i].

The next line contains an integer, minLength, the minimum length accepted by the machine.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN     Function 
-----     -------- 
4     →   lengths[] size n = 4
3     →   lengths[] =  [3, 5, 4, 3]
5
4
3
9     →   minLength= 9

```

Sample Output

Possible
```

Explanation

 

The uncut rod is 3 + 5 + 4 + 3 = 15 units long. Cut the rod into lengths of 3 + 5 + 4 = 12 and 3. Then cut the 12 unit piece into lengths 3 and 5 + 4 = 9. The remaining segment is 5 + 4 = 9 units and that is long enough to make the final cut.

Sample Case 1

Sample Input For Custom Testing

STDIN     Function 
-----     -------- 
3     →   lengths[] size n = 3
5     →   lengths[] =  [5, 6, 2]
6
2
12    →   minLength= 12

```

Sample Output

Impossible
```

Explanation

 

The uncut rod is 5 + 6 + 2 = 13 units long. After making either cut, the rod will be too short to make the second cut.

## Sample Input/Output

## Preview

You are given an array lengths of size n, where each element represents the le
