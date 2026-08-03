# Validating Credit Card Numbers

---

| Field | Value |
|---|---|
| **Slug** | `validating-credit-card-number` |
| **Domain** | python |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/validating-credit-card-number |

---

## Preview

Verify whether credit card numbers are valid or not.

## Problem Statement

You and Fredrick are good friends. Yesterday, Fredrick received $N$ credit cards from __ABCD Bank__. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from __ABCD Bank__ has the following characteristics:

<br>
► It must start with a $4$, $5$ or $6$. 

► It must contain exactly $16$ digits.

► It must only consist of digits ($0$-$9$).

► It may have digits in groups of $4$, separated by _one_ hyphen __"$ $-$ $"__.

► It must __`NOT`__ use any other separator like '$ \ $ ' , '_', etc. <br>
► It must __`NOT`__ have $4$ or more consecutive repeated digits.  


**Examples**:


<sub>__Valid Credit Card Numbers__</sub>


	4253625879615786
    4424424424442444
    5122-2368-7954-3214
	
<sub>__Invalid Credit Card Numbers__</sub>


	42536258796157867		#17 digits in card number → Invalid 
    4424444424442444		#Consecutive digits are repeating 4 or more times → Invalid
    5122-2368-7954 - 3214	#Separators other than '-' are used → Invalid
    44244x4424442444		#Contains non digit characters → Invalid
    0525362587961578		#Doesn't start with 4, 5 or 6 → Invalid

## Input Format

The first line of input contains an integer $N$.

The next $N$ lines contain credit card numbers.


__Constraints__


$ 0 < N < 100$

## Output Format

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

## Sample Tests

### Test 1

```
4253625879615786
4424424424442444
5122-2368-7954-3214
```

### Test 2

```
42536258796157867 #17 digits in card number → Invalid 
4424444424442444 #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214 #Separators other than '-' are used → Invalid
44244x4424442444 #Contains non digit characters → Invalid
0525362587961578 #Doesn't start with 4, 5 or 6 → Invalid
```

### Test 3

```
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
```

### Test 4

```
Valid
Valid
Invalid
Valid
Invalid
Invalid
```
