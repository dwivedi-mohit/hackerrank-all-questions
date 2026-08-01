# Shashank and List

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.6605555555555556
- **Total Submissions:** 1800
- **Solved Count:** 1189
- **URL:** https://www.hackerrank.com/challenges/shashank-and-list

## Problem Statement

Shashank is a newbie to mathematics, and he is very excited after knowing that a given l of cardinality _N_ has (_2<sup>N</sup> - 1_) non-empty sublist. He writes down all the non-empty sublists for a given set _A_. For each sublist, he calculates sublist\_sum, which is the sum of elements and denotes them by S<sub>1</sub>, S<sub>2</sub>, S<sub>3</sub>, ... , S<sub>(2<sup>N</sup>-1)</sub>.

He then defines a special\_sum, _P_.

P = 2<sup>S<sub>1</sub> </sup> + 2<sup>S<sub>2</sub> </sup> + 2<sup>S<sub>3</sub> </sup> .... + 2<sup>S<sub>(2<sup>N</sup>-1)</sub> </sup>and reports P % (10<sup>9</sup> + 7).  

**Input Format**  
The first line contains an integer _N_, i.e., the size of list _A_.  
The next line will contain _N_ integers, each representing an element of list _A_.  

**Output Format**  
Print special\_sum, P _modulo (10<sup>9</sup> + 7)_.  

**Constraints**  
1 &le; _N_ &le; 10<sup>5</sup>  
0 &le; _a<sub>i</sub>_ &le; 10<sup>10</sup> , where _i &isin; [1 .. N]_  

**Sample Input**  

	3
	1 1 2
    
**Sample Output**  

	44

**Explanation**  

For given list, sublist and calculations are given below  
1. {1} and 2<sup>1</sup> = 2  
2. {1} and 2<sup>1</sup> = 2  
3. {2} and 2<sup>2</sup> = 4  
4. {1,1} and 2<sup>2</sup> = 4  
5. {1,2} and 2<sup>3</sup> = 8  
6. {1,2} and 2<sup>3</sup> = 8  
7. {1,1,2} and 2<sup>4</sup> = 16  
So total sum will be 44.

## Input Format

The first line contains an integer N, i.e., the size of list A.

The next line will contain N integers, each representing an element of list A.

## Output Format

Print special_sum, P modulo (109 + 7).

## Constraints

1 ≤ N ≤ 105

0 ≤ ai ≤ 1010 , where i ∈ [1 .. N]

## Sample Input

1 1 2

## Explanation

For given list, sublist and calculations are given below

1. {1} and 21 = 2

2. {1} and 21 = 2

3. {2} and 22 = 4

4. {1,1} and 22 = 4

5. {1,2} and 23 = 8

6. {1,2} and 23 = 8

7. {1,1,2} and 24 = 16

So total sum will be 44.
