# Easy School

---

| Field | Value |
|---|---|
| **Slug** | `easy-school` |
| **Contest** | hourrank-1 |
| **Difficulty** | Medium |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/easy-school |

---

## Problem Statement

Kamil finished his final exams, but he's not happy with his grades. He wants to change his grade for $n$ subjects. Each teacher will change his grade for a price: The $i$<sup>th</sup> teacher will do this for $C_i$ coins. The teachers have a deal: The $i$<sup>th</sup> teacher will correct Kamil's grade for free if Kamil bribes at least $b_i$ other teachers.

Kamil wants to know the minimum amount of coins he needs to bribe his teachers to change his grades.

**Input Format**<br>

The first line of input contains one integer number $n$: the number of different subjects.

The next $n$ lines contain two integers $C_i$ and $b_i$: the coins needed to bribe $i$-th teacher and the minimum number of teachers which Kamil must bribe so that $i$<sup>th</sup> teacher changes his grade for free, respectively.

**Constraints**<br>
For full score $1\leq n \leq 3·10^5$<br>
In 20% of testcases $1\leq n \leq 1000$<br>
$1 \leq C_i \leq 3·10^5$<br>
$0 \leq b_i < n $
 
 **Output Format**<br>
 
In a single line, print one integer number: the minimum amount of coins required to change the grade for all subjects.

**Sample Input 1:**<br>

    2
    3 0
    2 1

**Sample Output 1:**<br>

    2
    
**Sample Input 2:**<br> 

    4
    1 1
    3 1
    4 1
    9 3
    
**Sample Output 2:**<br>

    8
