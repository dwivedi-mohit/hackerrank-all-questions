# Saying Hi

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9703445554971067
- **Total Submissions:** 15208
- **Solved Count:** 14757
- **URL:** https://www.hackerrank.com/challenges/saying-hi

## Problem Statement

Given a sentence, $s$, write a RegEx to match the following criteria:	

1. The first character must be the letter $\textit{H}$ or $\textit{h}$.
2. The second character must be the letter $\textit{I}$ or $\textit{i}$.
3. The third character must be a single space (i.e.: $\textit{\\s}$). 
4. The fourth character *must not* be the letter $\textit{D}$ or $\textit{d}$.

Given $n$ lines of sentences as input, print each sentence matching your RegEx on a new line.

## Input Format

The first line contains an integer, $n$, denoting the number of lines of sentences.		
Each of the $n$ subsequent lines contains some sentence $s$ you must match.

## Output Format

Find each sentence, $s$, satisfying the RegEx criteria mentioned above, and print it on a new line.

## Constraints

- $1 \le n \le 10 $
- Each sentence, $s$, contains $1$ to $10$ words.
- Each word/token in a sentence is comprised only of upper and lowercase English letters.


## Sample Input

Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha

## Sample Output

Hi Alex how are you doing

## Explanation

The first sentence satisfies the RegEx criteria set forth in the Problem Statement (starts with the case-insensitive word , followed by a space, followed by a letter that is not ), so we print the sentence on a new line.

The second sentence fails our RegEx criteria, as the second word/token starts with a  (so we print nothing).

The third sentence fails our RegEx criteria, as it doesn't start with an  (so we print nothing).

The fourth sentence fails our RegEx criteria, as the third character in the sentence is not a space (so we print nothing).

The fifth sentence fails as our RegEx criteria, as the sentence does not start with the word  (so we print nothing).
