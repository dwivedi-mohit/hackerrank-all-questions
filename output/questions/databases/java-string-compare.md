# Java Substring Comparisons

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9238699229540612
- **Total Submissions:** 405083
- **Solved Count:** 374244
- **URL:** https://www.hackerrank.com/challenges/java-string-compare

## Problem Statement

We define the following terms:

- [Lexicographical Order](https://en.wikipedia.org/wiki/Lexicographical_order), also known as *alphabetic* or *dictionary* order, orders characters as follows:		
	$$\texttt{A} \lt \texttt{B} \lt \ldots \lt \texttt{Y} \lt \texttt{Z} \lt \texttt{a} \lt \texttt{b} \lt \ldots \lt \texttt{y} \lt \texttt{z}$$ 
    
    For example, `ball < cat`, `dog < dorm`, `Happy < happy`, `Zoo < ball`.
- A [substring](https://en.wikipedia.org/wiki/Substring) of a string is a contiguous block of characters in the string. For example, the substrings of `abc` are `a`, `b`, `c`, `ab`, `bc`, and `abc`.

Given a string, $s$, and an integer, $k$, complete the function so that it finds the lexicographically *smallest* and *largest* substrings of length $k$.   

**Function Description**   

Complete the *getSmallestAndLargest* function in the editor below.   

*getSmallestAndLargest* has the following parameters:   

- *string s:* a string  
- *int k:* the length of the substrings to find   

**Returns**  

- *string:* the string '<smallest> + "\n" + <largest>' where <smallest> and <largest> are the two substrings   

## Input Format

The first line contains a string denoting $s$.		
The second line contains an integer denoting $k$.

## Output Format

  

## Constraints

- $1 \le |s| \le 1000$
- $s$ consists of English alphabetic letters only (i.e., `[a-zA-Z]`).

## Sample Input

welcometojava
3

## Sample Output

ava
wel

## Explanation

String  has the following lexicographically-ordered substrings of length :

We then return the first (lexicographically smallest) substring and the last (lexicographically largest) substring as two newline-separated values (i.e., ava\nwel).

The stub code in the editor then prints ava as our first line of output and wel as our second line of output.
