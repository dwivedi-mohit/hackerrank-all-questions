# Xaero And A Binary Gift

---

| Field | Value |
|---|---|
| **Slug** | `xaero-and-a-binary-gift` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 30 |
| **Contest** | 101hack29 |
| **URL** | https://www.hackerrank.com/challenges/xaero-and-a-binary-gift |

---

## Problem Statement

Today is Xaero's birthday. His mom decided to surprise him with a truly fantastic gift: his favourite binary string $A$. But, unfortunately, all the stocks of binary string $A$ have been sold out, and only a binary string $B$ ( $A \ne B$ ) is available in the market.

She purchased a binary string $B$ and tries to convert it to binary string $A$ by applying the given **SWAP** operation zero or more times.

**Explanation:**

* **SWAP**
	* Let the string $B$ of the form $B_1B_2 ..B_i....B_j..B_n$
    * Choose $2$ indices $i$ and $j$ such that $1 \le i,j \le |B|$, where $|B|$ denotes the length of string $B$.
    * Swap the binary bits present at index $i$ and $j$  i.e.  $B_i$ and $B_j$. 
	* Resultant String = $B_1B_2 ..B_j....B_i..B_n$.
  

Your task is to help Xaero's mom by telling her the minimum number of swap operations required to convert binary string $B$ to binary string $A$.

## Input Format

First line of input contains a binary string $A$. 

Second line of input contains a binary string $B$.

**Constraints**

$1 \le |A|, |B| \le 10^{3}$

$A_i, B_i \in$ $\{0, 1\}$

$A \ne B$

## Output Format

If it is possible to convert binary string $B$ to binary string $A$, output the minimum number of operations required for the conversion, otherwise, output $-1$.

## Sample Tests

### Test 1

```
1001
0110
```

### Test 2

```
2
```

### Test 3

```
010
11
```

### Test 4

```
-1
```

### Test 5

```
1110
1100
```

### Test 6

```
-1
```
