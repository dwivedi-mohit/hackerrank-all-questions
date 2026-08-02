# Almost Equal - Advanced

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.6203528670447385
- **Total Submissions:** 3174
- **Solved Count:** 1969
- **URL:** https://www.hackerrank.com/challenges/almost-equal-advanced

## Problem Statement

A Sumo wrestling championship is scheduled to be held this winter in the _HackerCity_ where _N_ wrestlers from different parts of the world are going to participate. The rules state that two wrestlers can fight against each other if and only if the difference in their height is less than or equal to K,  
(i.e) wrestler A and wrestler B can fight if and only if _|height(A)-height(B)|<=K_.  

<center><iframe width="560" height="315" src="hXCaZjtS-Us?rel=0" frameborder="0" allowfullscreen></iframe></center>

Given an array _H[]_, where _H[i]_ represents the height of the _i<sup>th</sup>_ fighter, for a given l, r where `0 <= l <= r < N`, can you count the number of pairs of fighters between l and r (both inclusive) who qualify to play a game?

**Input Format**  
The first line contains an integer _N_ and _K_  separated by a single space representing the number of Sumo wrestlers who are going to participate and the height difference K.  
The second line contains _N_ integers separated by a single space, representing their heights _H[0] H[1] ... H[N - 1]_.  
The third line contains _Q_, the number of queries. This is followed by _Q_ lines each having two integers _l_ and _r_ separated by a space.  

**Output Format**  
For each query Q, output the corresponding value of the number of pairs of fighters for whom the absolute difference of height is not greater that _K_.  

**Constraints**    
1 <= N <= 100000  
0 <= K <= 10<sup>9</sup>  
0 <= H[i] <= 10<sup>9</sup>  
1 <= Q <= 100000  
0 <= l <= r < N  

**Sample Input**
<pre>
5 2
1 3 4 3 0
3
0 1
1 3
0 4
</pre>
**Sample Output**  
<pre>
1
3
6
</pre>
**Explanation**  
Query #0: Between 0 and 1 we have i,j as (0,1) and |H[0]-H[1]|=2 therefore output is 1.  
Query #1: The pairs (H[1],H[2]) (H[1],H[3]) and (H[2],H[3]) are the pairs such that |H[i]-H[j]| <=2. Hence output is 3.  
Query #2: Apart from those in Query #1, we have (H[0],H[1]), (H[0], H[3]), (H[0], H[4]), hence 6.  

**Timelimits**

Timelimits are given [here](https://hr-assets.s3.amazonaws.com/7bb46cae_challenge_assets/checker_limits/1361/limits.json)


## Input Format

The first line contains an integer N and K  separated by a single space representing the number of Sumo wrestlers who are going to participate and the height difference K.

The second line contains N integers separated by a single space, representing their heights H[0] H[1] ... H[N - 1].

The third line contains Q, the number of queries. This is followed by Q lines each having two integers l and r separated by a space.

## Output Format

For each query Q, output the corresponding value of the number of pairs of fighters for whom the absolute difference of height is not greater that K.

## Constraints

1 <= N <= 100000

0 <= K <= 109

0 <= H[i] <= 109

1 <= Q <= 100000

0 <= l <= r < N

## Sample Input

5 2
1 3 4 3 0
3
0 1
1 3
0 4

## Sample Output

3
6

## Explanation

Query #0: Between 0 and 1 we have i,j as (0,1) and |H[0]-H[1]|=2 therefore output is 1.

Query #1: The pairs (H[1],H[2]) (H[1],H[3]) and (H[2],H[3]) are the pairs such that |H[i]-H[j]| <=2. Hence output is 3.

Query #2: Apart from those in Query #1, we have (H[0],H[1]), (H[0], H[3]), (H[0], H[4]), hence 6.

Timelimits

Timelimits are given here

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
