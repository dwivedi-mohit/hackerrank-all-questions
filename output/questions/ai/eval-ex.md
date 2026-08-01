# Evaluating e^x

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9531737773152965
- **Total Submissions:** 18259
- **Solved Count:** 17404
- **URL:** https://www.hackerrank.com/challenges/eval-ex

## Problem Statement

The series expansion of $e$<sup>$x$</sup> is given by:

$1 + x + x$<sup>$2$</sup>$/2! + x$<sup>$3$</sup>$/3! + x$<sup>$4$</sup>$/4!$ $+ .......$

Evaluate $e$<sup>$x$</sup> for given values of $x$ by using the above expansion _for the first $10$ terms_. 

**Input Format**

The first line contains an integer $N$, the number of test cases. <br>
$N$ lines follow. Each line contains a value of $x$ for which you need to output the value of $e$<sup>$x$</sup> using the above series expansion. These input values have exactly $4$ decimal places each.

**Output Format**

Output $N$ lines, each containing the value of $e$<sup>$x$</sup>, computed by your program.

**Constraints**

$1 <= N <= 50$  
$-20.00 <= x <= 20.00$ <br>
_Var_, _Val_ in Scala and _def_ and _defn_ in Clojure are blocked keywords. The challenge is to accomplish this without either mutable state or direct declaration of local variables.


**Sample Input**

    4
    20.0000
    5.0000
    0.5000
    -0.5000

**Sample Output**

    2423600.1887
    143.6895
    1.6487
    0.6065

**Explanation**

The output has the computed values of $e$<sup>$x$</sup> corresponding to each test case. They are correct up to $4$ decimal places and on separate lines.

**Scoring**

All test cases carry an equal weight in the final score. For your solution to pass a given test case, all the values of $e$<sup>$x$</sup> computed by you must be within $+/- 0.1$ of the expected answers. This tolerance level has been kept to account for slightly different answers across different languages.


## Input Format

The first line contains an integer , the number of test cases.

 lines follow. Each line contains a value of  for which you need to output the value of  using the above series expansion. These input values have exactly  decimal places each.

## Output Format

Output  lines, each containing the value of , computed by your program.

## Constraints

Var, Val in Scala and def and defn in Clojure are blocked keywords. The challenge is to accomplish this without either mutable state or direct declaration of local variables.

## Sample Input

20.0000
5.0000
0.5000
-0.5000

## Sample Output

2423600.1887
143.6895
1.6487
0.6065

## Explanation

The output has the computed values of  corresponding to each test case. They are correct up to  decimal places and on separate lines.

Scoring

All test cases carry an equal weight in the final score. For your solution to pass a given test case, all the values of  computed by you must be within  of the expected answers. This tolerance level has been kept to account for slightly different answers across different languages.
