# Signal Tower

- **Domain:** fp
- **Difficulty:** Advanced
- **Max Score:** 80
- **Success Ratio:** 0.7905982905982906
- **Total Submissions:** 234
- **Solved Count:** 185
- **URL:** https://www.hackerrank.com/challenges/signal-tower

## Problem Statement

Mobile Towers are on the rise in HacksVille and there are N such mobile towers. Each mobile tower 
is named according to its position in the 2D plane of HacksVille i.e. (A[i],B[i]) is the position
of the i<sup>th</sup> tower. The city due to its growing power needs, is not able to power all the mobile towers and it can power only a set of towers between a range, say [L..R] (both inclusive). 

All the Mobile Towers are monitored by a wireless control room. For the controller room to connect to all the active mobile towers, it has to position itself such that the sum of its distance to all the active mobile towers (S) is minimized. 

If the wireless control room is positioned at (X,Y). Then, its distance to the mobile tower *i*
is given by

    max(|X-A[i]|,|Y-B[i]|) where |x| means absolute value of x. 

**Input Format**  

The first line contains two integers, N and Q separated by a space where Q is the indices of the mobile towers that are active at different points of time.  
The second line contains integers A<sub>1</sub> to A<sub>N</sub> all separated by a single space.   
The third line contains integers B<sub>1</sub> to B<sub>N</sub> all separated by a single space where (Ai,Bi) is the position of the i<sup>th</sup> tower.
Q lines follow each containing the range L and R separated by a single space which are the range of towers that are active. 

    N Q
    A1 A2 ... An
    B1 B2 ... Bn
    L1 R1
    L2 R2
    ...
    LQ RQ

**Constraints**  
1 <= N <= 100000  
1 <= Q <= 100000  
-1000000000 <= A[i], B[i] <= 1000000000  
1 <= Li <= Ri <= N  

**Output Format**

Your task is to find the optimal position and print its cumulative distance (S) to all the mobile towers. 

    S1
    S2
    ...
    SQ

Error of at most 10<sup>-3</sup> is tolerated. 

**Sample Input**  

    4 2
    1 2 0 1
    4 3 1 1
    1 4
    3 4

**Sample Output**

    5.0000000
    1.0000000

**Explanation**

In the testcase, there are 4 mobile towers in the city of HacksVille positioned at (1,4), (2,3), (0,1) and (1,1)

At time T1, all the mobile towers are active ( indicated by L = 1 and R = 4 ). So, one possible location for the mobile control room would be at 

    1.5 2.5 

The cumulative distance (S) is 

    = max(|1.5-1|, |2.5-4|) + max(|1.5-2|,|2.5-3|) + max(|1.5-0|,|2.5-1|) + max(|1.5-1|,|2.5-1|)
    = max(0.5, 1.5) + max(0.5,0.5) + max(1.5,1.5) + max(0.5,1.5)
    = 1.5 + 0.5 + 1.5 + 1.5
    = 5.0

At time T2, only the mobile towers indexed between 3 and 4 ( L = 3 and R = 4) are indexed. So, one possible location for the mobile control room would be, 

    1 1

The cumulative distance (S) is 

    = max(|1-0|,|1-1|) + max(|1-1|,|1-1|)
    = max(1,0) + max(0,0)
    = 1.0


## Input Format

The first line contains two integers, N and Q separated by a space where Q is the indices of the mobile towers that are active at different points of time.

The second line contains integers A1 to AN all separated by a single space.

The third line contains integers B1 to BN all separated by a single space where (Ai,Bi) is the position of the ith tower.
Q lines follow each containing the range L and R separated by a single space which are the range of towers that are active.

N Q
A1 A2 ... An
B1 B2 ... Bn
L1 R1
L2 R2
...
LQ RQ

## Output Format

Your task is to find the optimal position and print its cumulative distance (S) to all the mobile towers.

S1
S2
...
SQ

Error of at most 10-3 is tolerated.

## Constraints

1 <= N <= 100000

1 <= Q <= 100000

-1000000000 <= A[i], B[i] <= 1000000000

1 <= Li <= Ri <= N

## Sample Input

4 2
1 2 0 1
4 3 1 1
1 4
3 4

## Sample Output

5.0000000
1.0000000

## Explanation

In the testcase, there are 4 mobile towers in the city of HacksVille positioned at (1,4), (2,3), (0,1) and (1,1)

At time T1, all the mobile towers are active ( indicated by L = 1 and R = 4 ). So, one possible location for the mobile control room would be at

1.5 2.5

The cumulative distance (S) is

= max(|1.5-1|, |2.5-4|) + max(|1.5-2|,|2.5-3|) + max(|1.5-0|,|2.5-1|) + max(|1.5-1|,|2.5-1|)
= max(0.5, 1.5) + max(0.5,0.5) + max(1.5,1.5) + max(0.5,1.5)
= 1.5 + 0.5 + 1.5 + 1.5
= 5.0

At time T2, only the mobile towers indexed between 3 and 4 ( L = 3 and R = 4) are indexed. So, one possible location for the mobile control room would be,

1 1

The cumulative distance (S) is

= max(|1-0|,|1-1|) + max(|1-1|,|1-1|)
= max(1,0) + max(0,0)
= 1.0
