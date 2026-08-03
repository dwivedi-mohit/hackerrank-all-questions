# Day 1: Interquartile Range

---

| Field | Value |
|---|---|
| **Slug** | `s10-interquartile-range` |
| **Domain** | tutorials |
| **Difficulty** | Easy |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/s10-interquartile-range |

---

## Preview

Calculate the interquartile range.

## Problem Statement

**Objective** <br>
In this challenge, we practice calculating the *interquartile range*. We recommend you complete the [Quartiles](/challenges/s10-quartiles) challenge before attempting this problem.

**Task** <br>
The interquartile range of an array is the difference between its first ($Q_1$) and third ($Q_3$) quartiles (i.e., $Q_3 - Q_1$).

Given an array, $values$, of $n$ integers and an array, $freqs$, representing the respective frequencies of $values$'s elements, construct a data set, $S$, where each $values[i]$ occurs at frequency $freqs[i]$. Then calculate and print $S$'s interquartile range, rounded to a scale of $1$ decimal place (i.e., $12.3$ format).

**Tip:** Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to *not* include the median in your upper and lower data sets.

**Example** 

$values = [1, 2, 3]$

$freqs = [3, 2, 1]$ 


Apply the frequencies to the values to get the expanded array $S = [1, 1, 1, 2, 2, 3]$.  Here $left = [1, 1, 1], right = [2, 2, 3]$.  The median of the left half, $Q_1 = 1.0$, the middle element.  For the right half, $Q_3 = 2.0$. Print the difference to one decimal place: $Q_3 - Q_1 = 2.0 - 1.0 = 1$, so print $1.0$.  


**Function Description**


Complete the *interQuartile* function in the editor below. 


*interQuartile* has the following parameters: 

- *int values[n]:* an array of integers

- *int freqs[n]:* $values[i]$ occurs $freqs[i]$ times in the array to analyze 


**Prints**


- *float:* the interquartile range to 1 place after the decimal

## Input Format

The first line contains an integer, $n$, the number of elements in arrays $values$ and $freqs$. 		
The second line contains $n$ space-separated integers describing the elements of array $values$. 	
The third line contains $n$ space-separated integers describing the elements of array $freqs$.

## Output Format

Print the *interquartile range* for the expanded data set on a new line. Round the answer to a scale of $1$ decimal place (i.e., $12.3$ format).

## Constraints

- $5 \le n \le 50$

- $0 \lt values[i]  \le 100$ 

- $0 \lt \sum_{i = 0}^{n - 1}freqs[i]  \le 10^{3}$ 

- The number of elements in $S$ is equal to $\sum freqs$.

## Sample Tests

### Test 1

```
STDIN Function
----- --------
6 arrays size n = 6
6 12 8 10 20 16 values = [6, 12, 8, 10, 20, 16]
5 4 3 2 1 5 freqs = [5, 4, 3, 2, 1, 5]
```

### Test 2

```
9.0
```
