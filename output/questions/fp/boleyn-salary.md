# Boleyn Salary

---

| Field | Value |
|---|---|
| **Slug** | `boleyn-salary` |
| **Domain** | fp |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/boleyn-salary |

---

## Preview

K'th lowest salary.

## Problem Statement

Boleyn Su runs a company called Acme. There are _N_ employees in the company, and each one of them is represented by a unique employee id whose range lies in _[1, N]_. Being the head of company, Boleyn's employee id is _1_.

<br>
Each employee, except Boleyn, has exactly one direct superior. This means that the hierarchial structure of the company is like a tree, where

1. Boleyn, employee id 1, represents the root node.
2. Each pair of employee is directly or indirectly connected to one another.
3. There is no cycle.

Let's represent the salary by the array _s = {s[1], s[2], s[3]..., s[N]}_, where _s[i]_ is the salary of the _i<sup>th</sup>_ employee. Salary structure in the company is non-uniform. Even a subordinate may get a higher salary than her superior. Some of the employees in Acme are curious about who gets the _k<sup>th</sup>_ lowest salary *among her subordinates*. Help them in solving their query.

**Note**


1. _1<sup>st</sup>_ lowest salary is equivalent to lowest salary, _2<sup>nd</sup>_ lowest means lowest salary which is greater that _1<sup>st</sup>_ lowest salary, and so on.
2. Salary of each employee is different.
3. It is not necessary that the people who are placed higher on hierarchy will have a greater salary than their subordinates.

**Input Format**

The first line contains two space separated integers, _N Q_, where _N_ is the number of employees in Acme, and _Q_ is the number of queries.

Then follows _N-1_ lines. Each of these lines contain two space separated integers, _u p_, where _p_ is the superior of _u_. _u_ and _p_ are employees id.

In the next line there are _N_ space separated integers, _s[1] s[2] ... s[n]_, where _s[i]_, _i &isin; [1..N]_, is the salary of _i<sup>th</sup>_ employee.

Then, _Q_ queries follow. Each query contains two space separated integers, _v k_. See output format for it's definition.

**Output format**

For the first query, print the id of employee who has the _k<sup>th</sup>_ lowest salary among the subordinates of _v_.

For the subsequent queries, we need to find the _k<sup>th</sup>_ lowest salary of the subordinates of _v+d_, where _d_ is the answer of previous query.

**Constraints**

1 &le; _N_ &le; 3*10<sup>4</sup>

1 &le; _Q_ &le; 3*10<sup>4</sup>

1 &le; _s[i]_ &le; 10<sup>9</sup>, _i_ &isin; _[1..N]_

_s[i]_ &ne; s[j], 1 &le; i < j &le; _N_

1 &le; _u, p_ &le; _N_, _u_ &ne; _p_

_-N_ &le; _d_ &le; _N_

For _1<sup>st</sup>_ query, 1 &le; _v_ &le; _N_

For later queries, 1 &le; _v+d_ &le; _N_

For each query, 1 &le; _K_ &le; Number_of_subordinates


**Sample Input**

    8 7
    2 1
    3 2
    4 2
    7 4
    8 4
    5 1
    6 5
    70 40 60 80 10 20 30 50
    2 1
    -6 5
    -4 1
    -5 3
    2 1
    -5 4
    2 2

**Sample Output**

    7
    8
    7
    3
    6
    2
    8

**Explanation**

Tree structure will be

             1(70)
            / \
           /   \
        2(40)  5(10)
         / \      \
        /   \      \
     3(60)  4(80)  6(20)
             / \
            /   \
         7(30)  8(50)


*Query #1* `Node = 2`, `k = 1`: Subordinates, in increasing order of salary, are _(7, 30), (8, 50), (3, 60), (4, 80)_. So employee _7_ has the _1<sup>st</sup>_ lowest salary among the subordinates of _2_.

*Query #2* `Node = -6+7 = 1`, `k = 5`: Subordinates are _(5, 10), (6, 20), (7, 30), (2, 40), (8, 50), (3, 60), (4, 80)_ . _8<sup>th</sup>_ employee has the _5<sup>th</sup>_ lowest salary among the subordinate of _1_.

*Query #3* `Node = -4+8 = 4`, `k = 1`: Subordinates are _(7, 30), (8, 50)_ . Similarly 7 is the answer of this query.

*Query #4* `Node = -5+7 = 2`, `k = 3`: Subordinates are _(7, 30), (8, 50), (3, 60), (4, 80)_. Similarly 3 is the answer for this query.

*Query #5* `Node = 2+3 = 5`, `k = 1`: Subordinates are _(6, 20)_. _6<sup>th</sup>_ employee has the most, and only, lowest salary. 

*Query #6* `Node = -5+6 = 1`, `k = 4`: Subordinates are _(5, 10), (6, 20), (7, 30), (2, 40), (8, 50), (3, 60), (4, 80)_.  2 is answer of this query.

*Query #7* `Node = 2+2 = 4`, `k = 2`: Subordinates are _(7, 30), (8, 50)_. Employee _8_ has the second lowest salaries among the subordinates of 4.


---
**Tested by:** [scturtle](/scturtle)

## Sample Tests

### Test 1

```
8 7
2 1
3 2
4 2
7 4
8 4
5 1
6 5
70 40 60 80 10 20 30 50
2 1
-6 5
-4 1
-5 3
2 1
-5 4
2 2
```

### Test 2

```
7
8
7
3
6
2
8
```

### Test 3

```
1(70)
 / \
 / \
 2(40) 5(10)
 / \ \
 / \ \
 3(60) 4(80) 6(20)
 / \
 / \
 7(30) 8(50)
```
