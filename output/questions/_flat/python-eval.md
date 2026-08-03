# Python Evaluation

---

| Field | Value |
|---|---|
| **Slug** | `python-eval` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/python-eval |

---

## Preview

Evaluate the expressions in Python using the expression eval().

## Problem Statement

The `eval()` expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.


For example:


```python
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
```
  

Here, `eval()` can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.


For example:

```python
>>> type(eval("len"))
<type 'builtin_function_or_method'>
```

Without eval()

```python
>>> type("len")
<type 'str'>
```
  

**Task**

You are given an expression in a line. Read that line as a string variable, such as *var*, and print the result using *eval(var)*.


**NOTE**: Python2 users, please import `from __future__ import print_function`.


**Constraint**

Input string is less than 100 characters.


**Sample Input**


	print(2 + 3)

**Sample Output**


	5
  

  

<!-- In Python2, input() function works equivalent to eval(raw_input()) do give it a try.  -->

## Sample Tests

### Test 1

```
>>>
eval
(
"9 + 5"
)
14
>>>
x
=
2
>>>
eval
(
"x + 3"
)
5
```

### Test 2

```
>>>
type
(
eval
(
"len"
))
<
type
'builtin_function_or_method'
>
```

### Test 3

```
>>>
type
(
"len"
)
<
type
'str'
>
```

### Test 4

```
print(2 + 3)
```

### Test 5

```
5
```
