# Iterables and Iterators

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.9680136564616332
- **Total Submissions:** 142936
- **Solved Count:** 138364
- **URL:** https://www.hackerrank.com/challenges/iterables-and-iterators

## Problem Statement

The _itertools_ module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an _iterator algebra_ making it possible to construct specialized tools succinctly and efficiently in pure _Python_. 

To read more about the functions in this module, check out their [documentation here](https://docs.python.org/2/library/itertools.html). 

You are given a list of $N$ lowercase English letters. For a given integer $K$, you can select any $K$ indices (assume $1$-based indexing) with a uniform probability from the list.  

Find the _probability_ that _at least_ one of the $K$ indices selected will contain the letter: '$a$'.  


**Input Format**

The input consists of three lines. The first line contains the integer $N$, denoting the length of the list. The next line consists of $N$ space-separated lowercase English letters, denoting the elements of the list. 

The third and the last line of input contains the integer $K$, denoting the number of
indices to be selected. 


**Output Format**

Output a single line consisting of the _probability_ that _at least_ one of the $K$ indices selected contains the letter:'$a$'. 

**Note**: The answer must be correct up to 3 decimal places. 


**Constraints**

$1 \le N \le 10$

$1 \le K \le N$

*All the letters in the list are lowercase English letters.*


**Sample Input**

    4 
    a a c d
    2
    



**Sample Output**

	0.8333


**Explanation**

All possible unordered tuples of length $2$ comprising of indices from $1$ to $4$ are:

$(1,2) , (1,3) , (1,4) , (2,3) , (2,4) , (3,4) $ 

Out of these $6$ combinations, $5$ of them contain either index $1$ or index $2$ which are the indices that contain the letter '$a$'. 

Hence, the answer is $\frac{5}{6}$.

<!-- Note: Considering ordered tuples(permutations) would not change the answer as -->

<!-- both the numerator and the denominator in the probability would be doubled. -->

## Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of
indices to be selected.

## Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

## Constraints

All the letters in the list are lowercase English letters.

## Sample Input

a a c d
2

## Sample Output

0.8333

## Explanation

All possible unordered tuples of length  comprising of indices from  to  are:

Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.

Hence, the answer is .
