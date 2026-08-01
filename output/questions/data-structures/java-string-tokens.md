# Java String Tokens

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.8427182696039802
- **Total Submissions:** 340084
- **Solved Count:** 286595
- **URL:** https://www.hackerrank.com/challenges/java-string-tokens

## Problem Statement

Given a string, $s$, matching the regular expression `[A-Za-z !,?._'@]+`, split the string into *tokens*. We define a token to be one or more consecutive English alphabetic letters. Then, print the number of tokens, followed by each token on a new line.

**Note:** You may find the [String.split](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#split-java.lang.String-) method helpful in completing this challenge.

## Input Format

A single string, $s$.

## Output Format

On the first line, print an integer, $n$, denoting the number of tokens in string $s$ (they *do not* need to be unique). Next, print each of the $n$ tokens on a new line in the same order as they appear in input string $s$.

## Constraints

- $1 \le \text{ length of } s \le 4 \cdot 10^5$
- $s$ is composed of *any* of the following: English alphabetic letters, blank spaces, exclamation points (`!`), commas (`,`), question marks (`?`), periods (`.`), underscores (`_`), apostrophes (`'`), and at symbols (`@`).

## Sample Input

He is a very very good boy, isn't he?

## Sample Output

He
is
a
very
very
good
boy
isn
t
he

## Explanation

We consider a token to be a contiguous segment of alphabetic characters. There are a total of  such tokens in string , and each token is printed in the same order in which it appears in string .
