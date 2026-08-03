# Fair Cut

---

| Field | Value |
|---|---|
| **Slug** | `fair-cut` |
| **Domain** | algorithms |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/fair-cut |

---

## Preview

Choose some k from n integers in such way that the sum of the absolute difference among all pairs is minimal.

## Problem Statement

Li and Lu have $n$ integers, $a_1, a_2, \ldots, a_n$, that they want to divide fairly between the two of them. They decide that if Li gets integers with indices $I = \{i_1, i_2, \ldots, i_k\}$ (which implies that Lu gets integers with indices $J = \{1, \ldots, n\} \setminus I$), then the measure of unfairness of this division is: 
$$f(I) = \sum\limits_{i \in I} \sum\limits_{j \in J} |a_i - a_j|$$

Find the minimum measure of unfairness that can be obtained with some division of the set of integers where Li gets exactly $k$ integers. 

**Note** $A \setminus B$ means [Set complement](https://en.wikipedia.org/wiki/Complement_(set_theory))

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of integers Li and Lu have) and $k$ (the number of integers Li wants).		
The second line contains $n$ space-separated integers describing the respective values of $a_1, a_2, \ldots, a_n$.

## Output Format

Print a single integer denoting the minimum measure of unfairness of some division where Li gets $k$ integers.

**Sample Input 0**
 
    4 2
	4 3 1 2
 
__Sample Output 0__
 
     6
   

**Explanation 0**		
One possible solution for this input is $I = \{2,4\};\, J=\{1,3\}$. $|a_2 - a_1| + |a_2 - a_3| + |a_4 - a_1| + |a_4 - a_3| = 1 + 2 + 2 + 1 = 6$
  

**Sample Input 1** 

 
    4 1
    3 3 3 1
  

**Sample Output 1**
 
    2
  

**Explanation 1**		
The following division of numbers is optimal for this input: $I = \{1\};\, J = \{2,3,4\}$.

## Constraints

- $1 \le k < n \le 3000$
- $1 \le a_i \le 10^9$
- For $\text{15%}$ of the test cases, $n \le 20$.
- For $\text{45%}$ of the test cases, $n \le 40$.

## Sample Tests

### Test 1

```
4 2
4 3 1 2
```

### Test 2

```
6
```

### Test 3

```
4 1
3 3 3 1
```

### Test 4

```
2
```
