# Magical Girl, Devu, and Spirits

---

| Field | Value |
|---|---|
| **Slug** | `devu-magical-girl-and-spirits` |
| **Domain** | misc |
| **Difficulty** | Easy |
| **Score** | 25 |
| **Contest** | 101hack23 |
| **URL** | https://www.hackerrank.com/challenges/devu-magical-girl-and-spirits |

---

## Preview

Help magical girl in reaching her home safely by suggesting her how to use magic power provided by her master Devu.

## Problem Statement

During a fair, magical girl gets separated from her parents. Night has fallen and it is dark already. The spirits have started appearing, and she has been trapped on a bridge. She needs to cross the bridge to return home safely. 

Initially, she is at the start of the bridge (i.e. at index $0$) with $0$ initial _strength_. On the bridge, there are a total of $n$ spirits (which appear in the order $1$ to $n$), both good and bad ones. Each spirit has a parameter strength $S_i$. When she comes in contact with good spirit, it increases her strength by $|S_i|$ ($S_i \geq 0$) while bad ones decrease by $|S_i|$ ($S_i < 0$).

Being skeptical about her safety, her master, Devu, had already granted her a very special power called "reverse the effect", which can be used **at most** once. By using this power on a spirit, it can change a bad spirit to a good spirit and vice versa. Formally a spirit having initial strength $S_i$, will have $- S_i$ strength after the application of special power on it. Note that she can use this special power on the spirit before the spirit show their effects of strengths. If, at any position, her strength becomes negative, she dies instantly. 

As she is quite intelligent, she will use the power provided by her master smartly. If she is able to reach home safely, print "She did it!" (without quotes). Otherwise print the maximum position up to which she could reach (i.e. the position at which she died due to the effect of spirits). 

Please find it fast! My heart is praying for her safety!

**Note**


*reverse the effect* special power is applied on the **spirit**

## Input Format

-	The first line of the input contains a single integer, $T$, denoting the number of test cases.
-	For each test case, there are two lines. 
	-	The first line will contain a single integer, $n$, denoting the number of spirits.
    -	The second line will contain $n$ space-separated integers denoting the strengths of the spirits (i.e. the $i^{th}$ integer will denote $S_i$).

## Output Format

For each test case, print a single line denoting the answer to the problem.

**Constraints**

-	$ 1\leq T \leq 10^5$
-	$ 1\leq n \leq 10^5$
-	$ -10^3 \leq S_i \leq 10^3$
-	Sum of $n$ over all the test cases will be less than or equal to $10^6$.

## Sample Tests

### Test 1

```
3
2
-1 -2
3
1 -2 3
4
1 2 3 -7
```

### Test 2

```
2
She did it!
She did it!
```
