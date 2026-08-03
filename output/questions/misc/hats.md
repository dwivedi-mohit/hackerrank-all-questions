# Hat merchant

---

| Field | Value |
|---|---|
| **Slug** | `hats` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 100 |
| **Contest** | indeed-prime-codesprint |
| **URL** | https://www.hackerrank.com/challenges/hats |

---

## Preview

Find the maximum profit that you can earn from selling hats. Only a limited number of hats can be carried in the suitcase.

## Problem Statement

You realize your greatest ambition is to become a hat merchant, and decide to kick off your new career by selling at a hat convention. 

Your product line has $N$ types of hats, and for each type you can have up to $S_i$ sellable units. Because you must travel by plane, your inventory is limited to the number of hats you can fit in a single suitcase whose size is restricted to $K$ units of space by the airline. 

Each hat type in your product line is unusually shaped; hats of the same type can be stacked on top of one another, but hats of different types are *not* stackable. The first hat of each type packed takes $A_i$ units of space; each subsequent hat *of the same type* can be stacked on top of it using $B_i$ units of space. Some hat types are so thin that $A_i$ or $B_i$ can be treated as $0$.

Each type of hat sold can earn you $X_i$ dollars. Assuming you sell all the hats in your suitcase, what is the maximum amount of money you can earn at the convention?

## Input Format

The first line contains two space-separated integers, $N$ and $K$, respectively.

The $N$ subsequent lines each contain 4 integers; every line $i+1$ contains $X_i$, $S_i$, $A_i$, and $B_i$.

**Constraints**

$1 \le N \le 2 \times 10^3$

$1 \le K \le 5 \times 10^3$

$1 \le X_i, S_i \le 10^7$

$0 \le B_i \le A_i \le K$

## Output Format

Print a single integer describing the maximum amount of money you'll earn at the convention.

**The time limits for this problem are:**

	Python2, Python3 - 20sec
    C, C++ - 1sec
    Java, Java8 and C# - 2sec

## Sample Tests

### Test 1

```
Python2, Python3 - 20sec
C, C++ - 1sec
Java, Java8 and C# - 2sec
```

### Test 2

```
3 120
1000 3 20 10
1500 5 70 70
9000 1 20 1
```

### Test 3

```
12500
```
