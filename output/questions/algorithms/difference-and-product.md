# Difference and Product

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.3844049247606019
- **Total Submissions:** 2924
- **Solved Count:** 1124
- **URL:** https://www.hackerrank.com/challenges/difference-and-product

## Problem Statement

Tim likes Math. He likes it so much that he always brings his tablets with him and reads math e-books everywhere, even during parties.

Tim found an interesting exercise in one of the e-books he is reading. But you want him to join the party, so you decide to answer the question for him.

The problem is: Given $D$ and $P$, how many ordered pairs of integers are there whose [absolute difference](http://en.wikipedia.org/wiki/Absolute_difference) is $D$ and whose product is $P$? In other words, how many pairs of integers $(A,B)$ are there such that:

$$|A-B| = D$$
$$A\times B = P$$


## Input Format

The first line of input contains $T$, the number of test cases. The next $T$ lines describe the test cases.

Each test case consists of a single line containing two integers $D$ and $P$ separated by a single space.

## Output Format

For each test case, output a single line containing a single integer which is the answer for that test case.

**Constraints**  

$1 \le T \le 20000$  
$|D| \le 10^9$  
$|P| \le 10^9$  

## Sample Input

1 2
0 4
-1 1

## Sample Output

2
0

## Explanation

Case 1: There are four pairs of integers with absolute difference  and product , namely , , , .

Case 2: There are two pairs of integers with absolute difference  and product , namely , .

Case 3: There are no pairs of integers with absolute difference , because the absolute value is never negative.
