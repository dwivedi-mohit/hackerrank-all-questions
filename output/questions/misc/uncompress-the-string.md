# Uncompress the String

---

| Field | Value |
|---|---|
| **Slug** | `uncompress-the-string` |
| **Domain** | misc |
| **Difficulty** | Medium |
| **Score** | 80 |
| **Contest** | 101hack27 |
| **URL** | https://www.hackerrank.com/challenges/uncompress-the-string |

---

## Problem Statement

You are given a compressed string $S$. The string has lowercase letters and digits from $1$ to $9$.

We can uncompress the given string as follows: whenever we get a digit "$n$" in the string, the portion of the uncompressed string before the number will repeat "$n$" times.


For example: **ab2cd3** will give **ababcdababcdababcd** as the final string. 

**ab12cd** will give **ababcd** as final string. 


Now you will be asked to find the number of characters which are equal to $X$ in the uncompressed string from $A$ to $B$(both inclusive).

## Input Format

The first line contains the string $S$.  

The second line contains a single integer $Q$, which indicates the number of queries to follow.   

Next follows $Q$ line, each line consisting of a lowercase character $X$ followed by $2$ space-separated integers, $A$ and $B$.


**Note:** Uncompressed string is 1 indexed.

## Output Format

Output the result of each query in a separate line.


**Constraints**

$1 \le |S| \le 10^5$  

$1 \le Q \le 10^5$  

$1 \le A,B \le min(10^{18}$, **Length of the uncompressed String)** 

$S$ **starts with a lowercase letter**.

## Sample Tests

### Test 1

```
ab2cd3
2
a 1 10
d 5 8
```

### Test 2

```
4
1
```
