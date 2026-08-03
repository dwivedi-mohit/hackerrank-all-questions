# Square Segments

---

| Field | Value |
|---|---|
| **Slug** | `square-segments` |
| **Contest** | hourrank-2 |
| **Difficulty** | Hard |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/square-segments |

---

## Problem Statement

Debbie received an array $A$ as her birthday present. She wants to calculate the number of *square segments* in her array. A *square segment* is a segment of the array where the product of those numbers is a square. 

For example: Array $[7,6,10,15,2]$ has a segment $[6,10,15]$ that is a square segment because $6*10*15=900=30^2$ 

Can you help Debbie find the number of square segments?

## Input Format

The first line contains $N$, the size of the array.<br>
The second line contains $N$ integers. The $i^{th}$ integer is $A_i$.

**Constraints**<br>
$1 \le N \le 5*10^5$<br>
$1 \le A_i \le 10^6$<br>

## Output Format

Print the number of *square segments* in the array.

**Sample Input 1**<br>

    4
    3 4 4 3

**Sample Output 1**<br>
	
    4

**Sample Input 2**<br>

    5
    7 1 8 2 9

**Sample Output 2**<br>

	6
