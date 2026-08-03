# Stock Prediction

---

| Field | Value |
|---|---|
| **Slug** | `stocks-prediction` |
| **Domain** | fp |
| **Difficulty** | Hard |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/stocks-prediction |

---

## Problem Statement

George is very concerned about the stock options his company has granted him, because the company's stock price has fluctuated unpredictably and has often failed to meet expectations.  With this in mind, George has decided to sell his options.  Before doing so, he would like to perform a series of calculations.

Stock price history is presented as an array of positive integers, $A = \{a_0, a_1, \ldots, a_{n-1}\}$, which represents the average price per day of that stock. For a given day $d\ (0 \le d < n)$ and margin $M$, George needs to find the longest subarray containing the day's entry as a minimum,  $a_d$, and all other entries not exceeding $a_d+M$.

That is, he has to find the longest subarray, $A[l, r] = \{a_l, a_{l+1}, \ldots, a_r\}$, such that 

- $0 \le l \le d \le r < n$
- $a_d = minimum\{A[l, r]\}$
- $ \forall i \in [l, r], a_d \le a_i \le a_d + M$

George asks you to help him solve this problem.

## Input Format

The first list contains an integer $n$ which represents the length of the array $A$. The second line contains $n$ space-separated integers, $a_0, a_1, \ldots, a_{n-1}$, which represent the element of array $A$. The next line contains the number of queries $Q$. Each of the subsequent $Q$ lines contain two integers $d$ and $M$ which represent the index of the element, which should be minimal and be included in subarray, and margin, respectively.

## Output Format

For each query output the length of the longest subarray with the required properties.

**Constraints**

$1 \le n \le 5\cdot 10^4$

$1 \le A[i] \le 10^9, 0 \le i < n$

$1 \le Q \le 10^5$

$0 \le d < n$

$0 \le M \le 10^9$

## Sample Tests

### Test 1

```
5
3 5 2 6 1
2
0 2
2 3
```

### Test 2

```
2
3
```
