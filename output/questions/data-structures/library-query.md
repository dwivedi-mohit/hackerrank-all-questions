# Library Query

---

| Field | Value |
|---|---|
| **Slug** | `library-query` |
| **Domain** | data-structures |
| **Difficulty** | Advanced |
| **Score** | 80 |
| **URL** | https://www.hackerrank.com/challenges/library-query |

---

## Preview

Given N shelves, modify the number of books in a shelf and print the number of books in the Kth ranked shelf.

## Problem Statement

A giant library has just been inaugurated this week. It can be modeled as a sequence of N consecutive shelves with each shelf having some number of books. Now, being the geek that you are, you thought of the following two queries which can be performed on these shelves.

* Change the number of books in one of the shelves.

* Obtain the number of books on the shelf having the k<sup>th</sup> rank within 
the range of shelves. 

A shelf is said to have the k<sup>th</sup> rank if its position is k when the shelves are sorted based on the number of the books they contain, in ascending order.

Can you write a program to simulate the above queries?


**Input Format**

The first line contains a single integer T, denoting the number of test cases.

The first line of each test case contains an integer N denoting the number of shelves in the library.

The next line contains N space separated integers where the i<sup>th</sup> integer represents the number of books on the i<sup>th</sup> shelf where 1<=i<=N.

The next line contains an integer Q denoting the number of queries to be performed. Q lines follow with each line representing a query.

Queries can be of two types:

* 1 x k - Update the number of books in the x<sup>th</sup> shelf to k (1 <= x <= N).
* 0 x y k - Find the number of books on the shelf between the shelves x and y 
(both inclusive) with the k<sup>th</sup> rank (1 <= x <= y <= N, 1 <= k <= y-x+1).


**Output Format**

For every test case, output the results of the queries in a new line.


**Constraints**

1 <= T <= 5

1 <= N <= 10<sup>4</sup> 

1 <= Q <= 10<sup>4</sup>  

The number of books on each shelf is always guaranteed to be between 1 and 1000.

**Sample Input**

    2
    2
    1 2
    2
    0 1 2 1
    0 1 2 2
    4
    4 3 2 1
    4
    0 1 1 1
    1 1 1
    0 1 1 1
    0 1 4 3

**Sample Output**

    1
    2
    4
    1
    2

**Explanation**


There are two test cases :

1. The first test case contains only two shelves which can be represented as [1, 2]. Two queries are to be processed : 

	i) The first query asks for smallest number of books between the 1<sup>st</sup> and 2<sup>nd</sup> shevles which is **1**.

  

    ii) The second query asks for the 2<sup>nd</sup> smallest number of books between the 1<sup>st</sup> and 2<sup>nd</sup> shevles which is **2**.

  

2. The second test case contains four shelves which can be represented as [4, 3, 2, 1]. Four queries are to be processed :

  

     i) The first query asks for the smallest number of books in the 1<sup>st</sup> shelf which is **4**.

   

     ii) The second query updates the number of books in the 1<sup>st</sup> shelf to **1**. Hence the shelves now look like [1, 3, 2, 1].

   

     iii) The third query asks for the smallest number of books in the 1<sup>st</sup> shelf which is now **1**.

   

     iv) The last query asks for the 3<sup>rd</sup> smallest number of books between the 1<sup>st</sup> and 4<sup>th</sup> shelves which is **2**.

## Sample Tests

### Test 1

```
2
2
1 2
2
0 1 2 1
0 1 2 2
4
4 3 2 1
4
0 1 1 1
1 1 1
0 1 1 1
0 1 4 3
```

### Test 2

```
1
2
4
1
2
```
