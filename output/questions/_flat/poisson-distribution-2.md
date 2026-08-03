# Poisson Distribution #2

---

| Field | Value |
|---|---|
| **Slug** | `poisson-distribution-2` |
| **Domain** | ai |
| **Difficulty** | Medium |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/poisson-distribution-2 |

---

## Preview

Basic problems on the Poisson Distribution.

## Problem Statement

The manager of a industrial plant is planning to buy a machine of either type *A* or type *B*. For each day’s operation the number of repairs *X*, that the machine *A* needs is a poisson random variable with mean **0.88**. The daily cost of operating *A* is 
<pre>
C<sub>A</sub> = 160 + 40 ∗ X<sup>2</sup>
</pre>
For machine *B*, let *Y* be the poisson random variable indicating the number of daily repairs, which has mean **1.55**, and the daily cost of operating *B* is 
<pre>
C<sub>B</sub> = 128 + 40 ∗ Y<sup>2</sup> 
</pre>
Assume that the repairs take negligible time and each night the machine are cleaned so that they operate like new machine at the start of each day. What is the expected daily cost of each machine ?

**Submission Modes and Output Format**

You may submit either an R or Python program to accomplish the above task, or solve the problem on pen-and-paper. Your output should be two floating point/decimal numbers(as answers to 1st and 2nd questions respectively), correct to 3 places of decimal.

1. In the text box below, enter two floating point/decimal numbers(as answers to 1st and 2nd questions respectively), correct to 3 places of decimal.

2. Alternatively, you may submit an R program, which uses the above parameters (hard-coded) and computes the answer.

Your answer should resemble something like:
<pre>
9.123
8.345
</pre>
(This is **NOT** the answer, just a demonstration of what the answering format should resemble).

## Sample Tests

### Test 1

```
C
A
 = 160 + 40 ∗ X
2
```

### Test 2

```
C
B
 = 128 + 40 ∗ Y
2
```

### Test 3

```
9.123
8.345
```
