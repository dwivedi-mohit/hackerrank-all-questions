# Database Normalization #5

---

| Field | Value |
|---|---|
| **Slug** | `database-normalization-5` |
| **Domain** | databases |
| **Difficulty** | Medium |
| **Score** | 5 |
| **URL** | https://www.hackerrank.com/challenges/database-normalization-5 |

---

## Preview

Determine the normal form, given relations and determinants.

## Problem Statement

Consider the following relation and determinants.

R(**a**, **b**,c,d)


                       a,c -> b,d
                       a,d -> b
			Also, a,b is a primary key for the above relation.
          

The above relation is in **x** NF form where x may take the following values {1,2,3,3.5} corresponding to {1NF, 2NF, 3NF and BCNF} respectively.           

What is the maximum possible value of **x** such that the above relation satisfies the **x**NF form?

Your answer should only be restricted to one of these numbers:1/2/3/3.5
Do not leave any leading or trailing spaces.

## Sample Tests

### Test 1

```
a,c -> b,d
 a,d -> b
 Also, a,b is a primary key for the above relation.
```
