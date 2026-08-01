# Bangalore Bank

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.8914893617021277
- **Total Submissions:** 470
- **Solved Count:** 419
- **URL:** https://www.hackerrank.com/challenges/bangalore-bank

## Problem Statement

There is a famous old bank in Bangalore. It has just started the process of filling its database with bank account numbers of its clients. In order to put one account number to the database, an employee has to insert it from a piece of paper to a computer using a standard keyboard (without using number pad found on the right hand side of most keyboards). The weird thing is that every employee assigned to this task can type in using only 2 index fingers (one left hand index finger and one right hand index finger).  
<br>
Below is the sample representation of number keys present in the keyboard.  
<br>
![1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 0](http://hr-challenge-images.s3.amazonaws.com/3957/keyboard.jpg)  
<br>
He can perform any one of the following steps:

1. He can move any one of his fingers to adjacent keys.
2. He can press the key just below any of his fingers. But he can press only one key at a time.

Each of the above steps takes 1 second. So moving a finger from key 3 to key 5 takes 2s, moving a finger from key 7 to key 2 takes 5s, and moving a finger from key 0 to key 8 takes 2s (Key 0 is the *rightmost key*).  Similarly, pressing a single key takes 1 second.  

Write a program that computes the minimal time needed to add account number of an employee to the database. Before the process, an employee can place his finger wherever he wants. All digits should be inserted in the given order.

**Note**  

* It is not necessary that left finger will always lie on the left side of right finger. They can also lie on the same key, and in opposite direction also. 

**Input**  
In the first line, there is a number _n_ denoting the length of the bank account number.  
In the second line, there are _n_ digits separated by a single space denoting the bank account number.

**Output**  
In one and only line, print the minimum time (in seconds) required to rewrite the bank account number according to the above rules.  

**Constraints**  
1 &le; _n_ &le; 10<sup>4</sup>

**Input #00**

	2
	1 2

**Output #00**

	2

**Input #01**

	3
	1 0 3

**Output #01**

	5

**Explanations**  
<br>
*Test Case #00:*  An employee can put his left finger on *key 1* and his right finger on *key 2* before the process, so the whole process takes 2 seconds.  
<br>
*Test Case #01:*  An employee can put his left finger on *key 1* and his right finger on *key 0* before the process. From that position, it takes 2 seconds to press first two keys. After that, he can move his left finger from *key 1* to *key 3*, which takes 2 seconds and then press it which takes additional second. The whole process takes 5 seconds. Note that *key 0* is the rightmost key.

---
**Tested by** [Ray Williams Robinson Valiente](/shaka_shadows), [abhiranjan](/abhiranjan)


## Constraints

1 ≤ n ≤ 104

Input #00

2
1 2

Output #00

2

Input #01

3
1 0 3

Output #01

5

Explanations

Test Case #00:  An employee can put his left finger on key 1 and his right finger on key 2 before the process, so the whole process takes 2 seconds.

Test Case #01:  An employee can put his left finger on key 1 and his right finger on key 0 before the process. From that position, it takes 2 seconds to press first two keys. After that, he can move his left finger from key 1 to key 3, which takes 2 seconds and then press it which takes additional second. The whole process takes 5 seconds. Note that key 0 is the rightmost key.

Tested by Ray Williams Robinson Valiente, abhiranjan
