# Byteland Itinerary

---

| Field | Value |
|---|---|
| **Slug** | `byteland-itinerary` |
| **Domain** | mathematics |
| **Difficulty** | Advanced |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/byteland-itinerary |

---

## Preview

Help to find the expected length of maximum continuous trip made by car!

## Problem Statement

###A Byteland Vacation
You're planning a vacation to Byteland. It has $m$ cities, and you can travel between cities either by *plane* or by *car*. There are exactly $k$ highways in Byteland, and highway $i$ connects cities $a_i$ and $b_i$. If you want to travel from some city $u$ to some city $v$ and there is no highway between them, you can travel the distance from $u$ to $v$ by plane. 

One curious feature of Byteland is that *the number of highways connecting some city to others is equal for each city in Byteland*. More formally, let $deg_u$ be the number of cities such that there is a highway directly connecting city $u$ to some city, $v$. $deg_u = deg_v$ for all $1 \le u, v \le m$.

You want to finalize the itinerary for your Byteland vacation. You decide to visit a sequence of $n$ cities, $A$, such that $1 \le a_i \le m$. During your trip, you'll visit each city in the sequence $A = \{a_1, a_2, \ldots, a_n\}$; first traveling to city $a_1$, then traveling from $a_1$ to $a_2$, then traveling from $a_2$ to $a_3$, $\ldots$, finally traveling from $a_{n-1}$ to $a_n$. Be aware that you *may end up visiting certain cities more than once*.

###Exciting Roads
There are two ways to travel from $a_i$ to $a_{i + 1}$: by plane or by car. However, your preference is to travel by car because you dislike going through airport security and waiting in endless lines.

We call a continuous subsequence, $(l, r)$, of $A$ *exciting* if you can travel all the cities from $a_l$ to $a_r$ by car. More formally, $(l, r)$ is exciting if for each $l \le i \le r - 1$ there is a highway between $a_i$ and $a_{i + 1}$ (note that $a_i$ must not be equal to $a_{i + 1}$).

We call $r - l + 1$ the *length* of continuous subsequence $(l, r)$. You want to maximize the length of maximum exciting subsequence of $A$.

###Task
You decide to take a random itinerary, $A$ (recall that $|A| = n$, and each $a_i$ is a random city from $1$ to $m$) and follow it. You want to know the expected maximum length of a continuous exciting subsequence in your itinerary.

## Input Format

The first line contains three space-seperated non-negative integers describing the respective values of $n$ (the number of cities in your itinerary), $m$ (the number of cities in Byteland), and $k$ (the number of highways in Byteland).
Each line $i$ of the $k$ subsequent lines contain two space-separated positive integers describing the respective cities, $a_i$ and $b_i$, connected by highway $i$ in Byteland.

## Output Format

Let the answer be an irreducible fraction, $\frac{p}{q}$. Print the result of $(p \cdot q^{-1})\ mod\ (10^9 + 7)$.

**Sample Input 0**

    3 2 0

**Sample Output 0**

    1

**Explanation 0**		
There are no roads, meaning that all the exciting subsequences have length $1$. The expected length is also $1$.

**Sample Input 1**

    3 3 3
    1 2
    2 3
    3 1

**Sample Output 1**

	333333338 
  

**Explanation 1**		
There are exactly $27$ different plans and there are highways connecting all the cities. There are $3$ sequences with maximum length of exciting subsequence $1$, $12$ sequences with maximum length of exciting subseqence $2$ and $12$ sequences with maximum length of exciting subsequence $3$.

The expected value of maximum length: $E = (1 \cdot 3 + 2 \cdot 12 + 3 \cdot 12) / 3^3 = 63 / 27 = 7 / 3$.

That means, we need to print $7 \cdot 3^{(-1)}$ modulo $(10^9+7) = 333333338$. $3^{(-1)}$ means [Modulo inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) here.

## Constraints

- $1 \le n, m \le 10^5$
- $0 \le k \le 10^6$
- $1 \le a_i, b_i \le m$, $a_i \ne b_i$
- There are no loops and no multiple edges in Byteland road graph.
- All roads are undirected. 
- Test cases with $n, m \le 10$ are $10\%$ of the total score.
- Test cases with $n, m \le 100$ are $25\%$ of the total score
- Test cases with $n, m \le 1000$ are $50\%$ of the total score

## Sample Tests

### Test 1

```
3 2 0
```

### Test 2

```
1
```

### Test 3

```
3 3 3
1 2
2 3
3 1
```

### Test 4

```
333333338
```
