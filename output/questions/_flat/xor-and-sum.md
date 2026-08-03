# Xor and Sum

---

| Field | Value |
|---|---|
| **Slug** | `xor-and-sum` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/xor-and-sum |

---

## Preview

You are given two positive integers a and b in binary 
representation. You should find the given sum modulo 10^9+7.

## Problem Statement

You are given two positive integers $a$ and $b$ in binary representation. You should find the following sum modulo $10^{9} + 7$:

$$\sum\limits_{i=0}^{314159} (a~xor~(b~shl~i))$$

where operation $xor$ means exclusive OR operation, operation $shl$ means binary shift to the left.

Please note, that we consider ideal model of binary integers. That is there is infinite number of bits in each number, and there are no disappearings (or cyclic shifts) of bits.

## Input Format

The first line contains number $a$ $(1 \le a < 2^{10^5})$ in binary representation. The second line contains number $b$ $(1 \le b < 2^{10^5})$ in the same format. All the numbers do not contain leading zeros.

## Output Format

Output a single integer $-$ the required sum modulo $10^{9} + 7$.

## Sample Tests

### Test 1

```
10
1010
```

### Test 2

```
489429555
```
