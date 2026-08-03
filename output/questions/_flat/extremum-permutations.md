# Extremum Permutations

---

| Field | Value |
|---|---|
| **Slug** | `extremum-permutations` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/extremum-permutations |

---

## Preview

Count no. of permutations of set of N elements so that K contiguous elements are smaller than their adjacent and L contiguous elements are greater than their adjacents

## Problem Statement

Let's consider a permutation _P = {p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>}_ of the set of _N = {1, 2, 3, ..., N}_ elements .


_P_ is called a magic set if it satisfies both of the following constraints:


* Given a set of _K_ integers, the elements in positions _a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>K</sub>_ are less than their adjacent elements, i.e., _p<sub>a<sub>i</sub>-1</sub> > p<sub>a<sub>i</sub></sub> < p<sub>a<sub>i</sub>+1</sub>_
* Given a set of _L_ integers, elements in positions _b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>L</sub>_ are  greater than their adjacent elements, i.e., _p<sub>b<sub>i</sub>-1</sub> < p<sub>b<sub>i</sub></sub> > p<sub>b<sub>i</sub>+1</sub>_


How many such magic sets are there?

**Input Format**

The first line of input contains three integers _N_, _K_, _L_ separated by a single space.

The second line contains _K_ integers, _a<sub>1</sub>, a<sub>2</sub>, ... a<sub>K</sub>_ each separated by single space. 

the third line contains _L_ integers, _b<sub>1</sub>, b<sub>2</sub>, ... b<sub>L</sub>_ each separated by single space. 

**Output Format**

Output the answer modulo 1000000007 (10<sup>9</sup>+7).

**Constraints**  

3 <= _N_ <= 5000

1 <= K, L <= 5000

2 <= a<sub>i</sub>, b<sub>j</sub> <= N-1, where i &isin; [1, K] AND j &isin; [1, L]

 



**Sample Input #00**


    4 1 1
    2
    3

**Sample Output #00**


    5

**Explanation #00**

Here, N = 4 a<sub>1</sub> = 2 and b<sub>1</sub> = 3. The 5 permutations of {1,2,3,4} that satisfy the condition are 

+ 2 1 4 3
+ 3 2 4 1
+ 4 2 3 1
+ 3 1 4 2
+ 4 1 3 2
  

**Sample Input #01**
	
    10 2 2
    2 4
    3 9
  

**Sample Output #01**

	161280

## Sample Tests

### Test 1

```
4 1 1
2
3
```

### Test 2

```
5
```

### Test 3

```
10 2 2
2 4
3 9
```

### Test 4

```
161280
```
