# No Idea!

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.9008250882774534
- **Total Submissions:** 286030
- **Solved Count:** 257663
- **URL:** https://www.hackerrank.com/challenges/no-idea

## Problem Statement

There is an array of $n$ integers. There are also $2$ **disjoint sets**, $A$ and $B$, each containing $m$ integers. You like all the integers in set $A$ and dislike all the integers in set $B$. Your initial happiness is $0$. For each $i$ integer in the array, if $i\in A$, you add $1$ to your happiness. If $i\in B$, you add $-1$ to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.  

**Note:** Since $A$ and $B$ are sets, they have no repeated elements. However, the array might contain duplicate elements.  

**Constraints**  
$1\le n\le 10^5$  
$1\le m\le 10^5$  
$1\le Any\ integer\ in\ the\ input\le 10^9$  

## Input Format

The first line contains integers $n$ and $m$ separated by a space.  
The second line contains $n$ integers, the elements of the array.  
The third and fourth lines contain $m$ integers, $A$ and $B$, respectively.

## Output Format

Output a single integer, your total happiness.

## Sample Input

3 2
1 5 3
3 1
5 7

## Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
