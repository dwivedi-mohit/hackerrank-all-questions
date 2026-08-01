# The Trigram

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.5166139240506329
- **Total Submissions:** 3792
- **Solved Count:** 1959
- **URL:** https://www.hackerrank.com/challenges/the-trigram

## Problem Statement

Given a large chunk of text, identify the most frequently occurring trigram in it. If there are multiple trigrams with the same frequency, then print the one which occurred first.

Assume that trigrams are groups of three consecutive words in the same sentence which are separated by nothing but a single space and are case insensitive. The size of the input will be less than 10 kilobytes.  

	Input: I love games. I love to code.
	Here "games I love" is not a trigram because all the three words in trigram should be from the 
    same sentence.

## Input Format

A large chunk of text.

## Output Format

The most popular trigram - three words, with nothing but a space in between them. The output should be in lowercase. (If a trigram ends with dot then you should remove the dot.)

## Constraints

The input contains lowercase or uppercase alphabets, whitespaces and dots.

## Sample Input

I came from the moon. He went to the other room. She went to the drawing room.

## Sample Output

went to the

## Explanation

Here, "went to the" is the only trigram that has occurred maximum number of times.
