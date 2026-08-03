# Sergey and Homework

---

| Field | Value |
|---|---|
| **Slug** | `sergey-and-homework` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 80 |
| **Contest** | 101hack30 |
| **URL** | https://www.hackerrank.com/challenges/sergey-and-homework |

---

## Preview

Calculate the amount of homework Sergey will have to do.

## Problem Statement

Sergey studies $N$ subjects at Berland State University (BSU).

For each subject (say, the $i$<sup>th</sup>), Sergey assigns an integer $B_i$, denoting the importance of this subject. Also, for each subject, he has a book containing $A_i$ mathematical problems that are unsolved by Sergey.

Now, he wants to organize his studies for the next K days. During each one of those days, he will pick a subject with the maximal value of the product of the number of unsolved problems and the importance.  If there are similar subjects, pick the one with the minimal number and solve 1 problem from the book on this subject. If there are  no unsolved problems in the book for this subject, Sergey will do nothing on that day.

Formally, let $A_i$ denote the number of unsolved problems on the $i$<sup>th</sup> subject. Each day, Sergey will pick a subject with the maximum value of $A_i \times B_i$. If there are similar subjects, he will pick the one that has the minimal number. Then, he will solve one problem in this subject (so, the number of unsolved problems in this subject, namely $A_i$, will decrease by one).

To estimate how efficient his plan is, Sergey asks you to calculate the number of remaining problems in each of the subjects after he spends $K$ days as described above. 

Formally, you need to find the values of $A_i$ after $K$ days.

## Input Format

The first line of input contains 2 space-separated integers: $N$ and $K$, denoting the number of subjects and the number of days, respectively.

The following line contains $N$ space-separated integers $A_1, A_2, ..., A_N$ denoting the number of problems in the corresponding subjects.

The next line contains $N$ space-separated integers $B_1, B_2, ..., B_N$ denoting the importance of the corresponding subjects.

**Constraints**

- $1 \leq N \leq 10^5$
- $1 \leq K \leq 10^9$
- $1 \leq A_i, B_i \leq 10^9$

- In addition, $1 \leq N \leq 1000, 1 \leq K \leq 5 \times 10^4$ holds for test cases worth 25% of the problem's score.
- And, $1 \leq K \leq 10^6$ holds for test cases worth 50% of the problem's score,

## Output Format

Output $N$ space-separated integers. The $i$<sup>th</sup> of these numbers should be equal to the number of problems on the $i$<sup>th</sup> subject that will remain unsolved by Sergey after $K$ days.

## Sample Tests

### Test 1

```
5 7
7 4 1 2 5
9 4 3 2 1
```

### Test 2

```
1 3 1 2 5
```
