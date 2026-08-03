# The Trigonometric Ratios

---

| Field | Value |
|---|---|
| **Slug** | `trignometric-ratios` |
| **Domain** |  |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/trignometric-ratios |

---

## Preview

Compute the Sine and Cosine in as few characters as possible

## Problem Statement

The [Sine](https://en.wikipedia.org/wiki/Sine), [Cosine](https://en.wikipedia.org/wiki/Cosine) of x can be computed as follows.

sin(x) = x - x<sup>3</sup>/3! + x<sup>5</sup>/5! - x<sup>7</sup>/7! + x<sup>9</sup>/9! ....

cos(x) = 1 - x<sup>2</sup>/2! + x<sup>4</sup>/4! - x<sup>6</sup>/6! + x<sup>8</sup>/8! ....

Your task is to compute the Sine and Cosine for given values of x (where x is in radians) using the above series upto 5 terms.

**Input Format**

First line will contain N, the number of test cases.
Next N line will contain the input values of x

1<= N <= 50

0 < x < 10

Each value of x can contain upto 2 places of 
decimal in radians.


**Output Format**

2N Lines, corresponding to the N input values of x. For each input, you will output 2 lines.

1<sup>st</sup> line will be the Sine and the 2<sup>nd</sup> line will be the Cosine of x. 
An error margin of +/- 0.001 will be tolerated while evaluating the answers. Please round off your answer to 3 decimal places.

**Sample Input**

    5
    2.83
    3.24
    0.99
    2.74
    5.04

**Sample Output**

    0.309
    -0.943
    -0.089
    -0.963
    0.836
    0.549
    0.392
    -0.914
    0.195
    2.746
  

**Scoring** 

If the program output matches the expected output (permitting a deviation of +/- 0.001 for each output)

This is a codegolf problem. 

Score = maxScore\* (400 - S)/400 

S = min(Number of characters in source code,399)

## Sample Tests

### Test 1

```
5
2.83
3.24
0.99
2.74
5.04
```

### Test 2

```
0.309
-0.943
-0.089
-0.963
0.836
0.549
0.392
-0.914
0.195
2.746
```
