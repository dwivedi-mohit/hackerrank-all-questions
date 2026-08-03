# Xoring Ninja

---

| Field | Value |
|---|---|
| **Slug** | `xoring-ninja` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 55 |
| **URL** | https://www.hackerrank.com/challenges/xoring-ninja |

---

## Preview

Given a list of integers, sum the XORs of all the list's  non-empty subsets and mod your answer by 10^9 + 7.

## Problem Statement

An [XOR](https://en.wikipedia.org/wiki/Exclusive_or) operation on a list is defined here as the *xor* ($\oplus$) of all its elements (e.g.: $XOR(\{A, B, C\}) = A \oplus B \oplus C$). 

The $XorSum$ of set $arr$ is defined here as the sum of the $XOR$s of all non-empty subsets of $arr$ known as $arr'$. The set $arr'$ can be expressed as:

$\begin{eqnarray} XorSum(arr) = \sum_{i = 1}^{2^n-1} XOR(arr'_i) = XOR(arr'_1) + XOR(arr'_2) + \dots + XOR(arr'_{2^n-2}) + XOR(arr'_{2^n-1}) \end{eqnarray}$	 

**For example:** Given set $arr = \{n_1, n_2, n_3\}$

- The set of possible non-empty subsets is: $arr' = \{\{n_1\}, \{n_2\}, \{n_3\}, \{n_1, n_2\}, \{n_1, n_3\}, \{n_2, n_3\}, \{n_1, n_2, n_3\}\}$ 	

- The $XorSum$ of these non-empty subsets is then calculated as follows: 	
$XorSum(arr)$ = $ n_1 + n_2 + n_3 + (n_1 \oplus n_2) + (n_1 \oplus n_3) + (n_2 \oplus n_3) + (n_1 \oplus n_2 \oplus n_3)$

Given a list of $n$ space-separated integers, determine and print $XorSum\ \%\ (10^9+7)$.  


For example, $arr = \{3,4\}$.  There are three possible subsets, $arr' = \{\{3\},\{4\},\{3,4\}\}$.  The XOR of $arr'[1] = 3$, of $arr'[2] = 4$ and of $arr[3] = 3 \oplus 4 = 7$.  The XorSum is the sum of these: $3 + 4 + 7 = 14$ and $14\ \%\ (10^9+7) = 14$.


**Note:** The cardinality of [powerset](https://en.wikipedia.org/wiki/Power_set)$(n)$ is $2^n$, so the set of non-empty subsets of set $arr$ of size $n$ contains $2^n-1$ subsets.

**Function Description**


Complete the *xoringNinja* function in the editor below.  It should return an integer that represents the XorSum of the input array, modulo $(10^9+7)$.


xoringNinja has the following parameter(s):


- *arr*: an integer array

## Input Format

The first line contains an integer $T$, the number of test cases.		

Each test case consists of two lines:

-  The first line contains an integer $n$, the size of the set $arr$. 

-  The second line contains $n$ space-separated integers $arr[i]$.

## Output Format

For each test case, print its $XorSum\ \%\ (10^9+7)$ on a new line.  The $i^{th}$ line should contain the output for the $i^{th}$ test case.

## Constraints

$1 \le T \le 5$		
$1 \le n \le 10^5$		 
$0 \le arr[i] \le 10^9,\ 1 \le i \le n$

## Sample Tests

### Test 1

```
1
3
1 2 3
```

### Test 2

```
12
```

### Test 3

```
2
4
1 2 4 8
5
1 2 3 5 100
```

### Test 4

```
120
1648
```
