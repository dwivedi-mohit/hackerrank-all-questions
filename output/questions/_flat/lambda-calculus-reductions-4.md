# Lambda Calculus - Reductions #4

---

| Field | Value |
|---|---|
| **Slug** | `lambda-calculus-reductions-4` |
| **Domain** | fp |
| **Difficulty** | Medium |
| **Score** | 5 |
| **URL** | https://www.hackerrank.com/challenges/lambda-calculus-reductions-4 |

---

## Preview

Reduce the given lambda calculus expression, if possible.

## Problem Statement

Reduce the following expression, using the beta-rule, to no more than **one term**. If the expression cannot be reduced, enter "CAN'T REDUCE".

	(λg.((λf.((λx.(f (x x)))(λx.(f (x x))))) g)) 
  

   

Your answer should look like:

	u
  

(This is not the actual answer, just a demonstration of how you should present it.)

## Sample Tests

### Test 1

```
(λg.((λf.((λx.(f (x x)))(λx.(f (x x))))) g))
```

### Test 2

```
u
```
