# Easy sum

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 20
- **Success Ratio:** 0.5836909871244635
- **Total Submissions:** 5825
- **Solved Count:** 3400
- **URL:** https://www.hackerrank.com/challenges/easy-sum

## Problem Statement

Little Kevin had never heard the word 'Infinitum'. So he asked his mentor to explain the word to him. His mentor knew that 'Infinitum' is a very large number. To show him how big [Infinitum](http://en.wikipedia.org/wiki/Ad_infinitum) can be, his mentor gave him a challenge: to sum the numbers from _1_ up to _N_. The sum started to get really large and was out of `long long int` range. And so the lesson was clear.

Now his mentor introduced him to the concept of *mod* and asked him to retain only the remainder instead of the big number. And then, he gave him a formula to compute:

$$\sum_{i=1}^{N} (i\%m)$$

**Input Format**  
The first line contains _T_, the number of test cases.  
_T_ lines follow, each containing 2 space separated integers _N m_

**Output Format**  
Print the result on new line corresponding to each test case.  

**Constraint**  
1 &le; _T_ &le; 1000  
1 &le; _N_ &le; 10<sup>9</sup>  
1 &le; _m_ &le; 10<sup>9</sup>

**Sample Input**  

	3
	10 5
	10 3
	5 5

**Sample Output**  

	20
    10
    10
    
**Explanation**  
Case 1: _N_ = 10 _m_ = 5,  
1%5 + 2%5 + 3%5 + 4%5 + 5%5 + 6%5 + 7%5 + 8%5 + 9%5 + 10%5 = 20.  
Similar explanation follows for Case 2 and 3. 
    
    


## Input Format

The first line contains T, the number of test cases.

T lines follow, each containing 2 space separated integers N m

## Output Format

Print the result on new line corresponding to each test case.

Constraint

1 ≤ T ≤ 1000

1 ≤ N ≤ 109

1 ≤ m ≤ 109

## Sample Input

10 5
10 3
5 5

## Sample Output

10
10

## Explanation

Case 1: N = 10 m = 5,

1%5 + 2%5 + 3%5 + 4%5 + 5%5 + 6%5 + 7%5 + 8%5 + 9%5 + 10%5 = 20.

Similar explanation follows for Case 2 and 3.
