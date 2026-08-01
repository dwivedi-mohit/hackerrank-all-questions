# Java Strings Introduction

- **Domain:** java
- **Difficulty:** Easy
- **Max Score:** 5
- **Success Ratio:** 0.9423373815932388
- **Total Submissions:** 568063
- **Solved Count:** 535307
- **URL:** https://www.hackerrank.com/challenges/java-strings-introduction

## Problem Statement

> "A string is traditionally a sequence of characters, either as a literal constant or as some kind of variable." &mdash; [Wikipedia: String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))
    
This exercise is to test your understanding of Java Strings. A sample *String* declaration:

    String myString = "Hello World!"

The elements of a *String* are called *characters*. The number of *characters* in a *String* is called the *length*, and it can be retrieved with the *String.length()* method.

Given two strings of lowercase English letters, $A$ and $B$, perform the following operations:

1. Sum the lengths of $A$ and $B$.
2. Determine if $A$ is lexicographically larger than $B$ (i.e.: does $B$ come before $A$ in the dictionary?).
3. Capitalize the first letter in $A$ and $B$ and print them on a single line, separated by a space.

## Input Format

The first line contains a string $A$.
The second line contains another string $B$.
The strings are comprised of only lowercase English letters.


## Output Format

There are three lines of output:    
For the first line, sum the lengths of $A$ and $B$.        
For the second line, write `Yes` if $A$ is lexicographically greater than $B$ otherwise print `No` instead.    
For the third line, capitalize the first letter in both $A$ and $B$ and print them on a single line, separated by a space.

## Sample Input

hello
java

## Sample Output

9
No
Hello Java

## Explanation

String  is "hello" and  is "java".

 has a length of , and  has a length of ; the sum of their lengths is .

When sorted alphabetically/lexicographically, "hello" precedes "java"; therefore,  is not greater than  and the answer is No.

When you capitalize the first letter of both  and  and then print them separated by a space, you get "Hello Java".
