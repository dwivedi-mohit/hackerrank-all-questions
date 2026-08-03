# Xaero And The Enigma Hacking 

---

| Field | Value |
|---|---|
| **Slug** | `xaero-and-breaking-enigma` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack29 |
| **URL** | https://www.hackerrank.com/challenges/xaero-and-breaking-enigma |

---

## Problem Statement

Xaero and Allen are two computer scientists who are working in the National Physics laboratory of Britain. World War $3$ has been declared and, being a native of the rival country, Xaero hates his coworker Allen. Additionally, the name and fame of Allen's work adds a jealous note to the hatred. Therefore, he tries to betray him by stealing his famous work on the **Turing Machine**.

Xaero tries to take away a string $S$ consisting of **'?'** and lowercase letters made by Allen Turing. Xaero, being clever, knows that Allen would have encrypted the string. So, in order to decrypt the string $S$, Xaero needs to replace each **'?'** character with some lower case alphabet letter and then perform $Q$ reversal operations in the given order. Each operation consists of two integers $L$ and $R$ denoting the substring of string $S$, and the operation is to reverse the substring from $L$ to $R$.
Allen, being more clever and cunning than Xaero, discovers the betrayal of his close friend Xaero. So, he made the string $S$ in such a way that, if Xaero unknowingly replaces the **'?'** characters in the string $S$ such that the formed string $S$ is the $K^{th}$ lexographical smallest string which will remain same even after performing all the $Q$ operations, then the string $S$ will be destroyed automatically, and Xaero won't be able to decrypt it.

Xaero wants to decrypt the string $S$ at any cost and therefore he wants you to tell him the $K^{th}$ lexographical smallest string which will remain same even after performing all the $Q$ operations to ensure safety. Please help this bad man to decrypt the given string $S$.

## Input Format

First line of input contains $3$ space separated integers $N$, $M$ and $K$ denoting the length of string $S$, number of reversal operations required to be performed and the value of $K$ respectively. Next line of input contains a string consisting of **'?'** and lower case alphabets ( **'a'** to **'z'** ). Next $M$ lines of input contains $2$ space separated integers $L$ and $R$ denoting a substring of string $S$, where a string in $i^{th}$ line denotes the substring which is required to be reversed in $i^{th}$ reversal operation.

**Constraints**

$1 \le N,M \le 10^{5}.$

$1 \le L \le R \le N.$

$1 \le K \le 10^{15}.$

## Output Format

For each test case, print the $K^{th}$ lexographical smallest string following the above criteria if it exists. Print **"Bad Luck Allen"** otherwise.

## Sample Tests

### Test 1

```
3 1 1
a?b
1 2
```

### Test 2

```
aab
```

### Test 3

```
3 1 2
a?b
1 2
```

### Test 4

```
Bad Luck Allen
```

### Test 5

```
3 1 4
?a?
1 3
```

### Test 6

```
dad
```

### Test 7

```
5 5 10513609
?????
1 1
2 2
3 3
4 4
5 5
```

### Test 8

```
xaero
```
