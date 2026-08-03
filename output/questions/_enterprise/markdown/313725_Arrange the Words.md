# Arrange the Words

## Metadata

- **ID:** 313725
- **Type:** code
- **Difficulty:** 9.722222222222221
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Strings, Algorithms, Data Structures, Problem Solving
- **Skills:** Problem Solving (Basic)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates string manipulation, algorithms, and data structures concepts, ideal for junior-level roles. The problem requires rearranging words in a sentence by length while maintaining their original order for words of the same length.

## Problem Statement

Rearrange the words in a sentence by length.

You are given a sentence that:

	
- Contains words separated by single spaces
	
- Starts with an uppercase letter
	
- Ends with a period (.)
	
- Contains only letters and spaces (besides the final period)

 

Your task is to rearrange the words in the sentence as follows:

	
- Order words by increasing length
	
- If multiple words have the same length, keep their original order (stable sort)

 

After rearranging, rebuild the sentence so that:

	
- The first letter is uppercase
	
- All other letters are lowercase
	
- Words are separated by single spaces
	
- The sentence ends with a period (.)

 

Example

Suppose sentence = 'The lines are printed in reverse order.'

Output: "In the are lines order printed reverse."

Explanation:

Sort the words by length. Keep the original order for the words with the same length.

	
- Length 2: {in}
	
- Length 3: {the, are} 
	
- Length 5: {lines, order}
	
- Length 7: {printed, reverse}

 

Reassemble the sequence of words, make the first letter uppercase, the intermediate letters lowercase, and the last character a period.

 

Constraints

	
- 
1 ≤ length of sentence < 105

## Sample Input/Output

## Preview

Rearrange the words in a sentence by length.
