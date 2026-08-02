# XOR love

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.5888501742160279
- **Total Submissions:** 287
- **Solved Count:** 169
- **URL:** https://www.hackerrank.com/challenges/xor-love

## Problem Statement

Devendra loves the XOR operation very much which is denoted by $\wedge$ sign in most of the programming languages. He has a list $A$ of $N$ numbers and he wants to know the answers of $M$ queries. Each query will be denoted by three numbers i.e. $K,P,R$ .

For query $K,P \text{ and } R$, he has to print the value of the $KPRsum$ which can be described as given below. As the value of the $KPRsum$ can be large. So, print it modulus $(10^9 + 7)$.

$$ KPRsum = \sum_{i=P}^{R-1} \sum_{j=i+1}^{R} (K \oplus (A[i] \oplus A[j]) )$$

**Input Format**  
The first line contains an integer $N$, i.e., the number of the elements in the list. List is numbered from $1$ to $N$.  
Next line will contain $N$ space seperated integers.  
Third line will contain a number $M$ i.e. number of queries followed by $M$ lines each containing  integers $K,P \& R$.

**Output Format**  
Print $M$ lines, $i^{th}$ line will be answer of $i^{th}$ query. **Answer will be 0 in case of P=R.**

**Constraints**  
$1 \le N \le 10^5$  
$1 \le A[i] \le 10^6$  
$1 \le M \le 10^5$  
$0 \le K \le 10^6$  
$1 \le P \le R \le N$

**Sample Input**  

	3
    1 2 3
    2
    1 1 3
    2 1 3

    
**Sample Output**  

	5
    4

**Explanation**

For first query, it will will be $$(1 \oplus( 1 \oplus 2) ) + (1 \oplus( 1 \oplus 3) ) + (1 \oplus( 2 \oplus 3) )  =  5 $$

## Input Format

The first line contains an integer , i.e., the number of the elements in the list. List is numbered from  to .

Next line will contain  space seperated integers.

Third line will contain a number  i.e. number of queries followed by  lines each containing  integers .

## Output Format

Print  lines,  line will be answer of  query. Answer will be 0 in case of P=R.

## Sample Input

1 2 3
2
1 1 3
2 1 3

## Sample Output

4

## Explanation

For first query, it will will be

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
