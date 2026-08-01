# Subsequence Weighting

- **Domain:** sql
- **Difficulty:** Advanced
- **Max Score:** 60
- **Success Ratio:** 0.7177451369591108
- **Total Submissions:** 5038
- **Solved Count:** 3616
- **URL:** https://www.hackerrank.com/challenges/subsequence-weighting

## Problem Statement

A subsequence of a sequence is a sequence which is obtained by deleting zero or more elements from the sequence. 

You are given a sequence `A` in which every element is a pair of integers  i.e  `A` = _[(a<sub>1</sub>, w<sub>1</sub>), (a<sub>2</sub>, w<sub>2</sub>),..., (a<sub>N</sub>, w<sub>N</sub>)]_.

For a subseqence `B` = _[(b<sub>1</sub>, v<sub>1</sub>), (b<sub>2</sub>, v<sub>2</sub>), ...., (b<sub>M</sub>, v<sub>M</sub>)]_ of the given sequence : 
 
- We call it increasing if for every _i_ (1 <= _i_ < _M_ ) , _b<sub>i</sub> < b<sub>i+1</sub>_.
- _Weight(B) = v<sub>1</sub> + v<sub>2</sub> + ... + v<sub>M</sub>_.  

**Task:**  
Given a sequence, output the maximum weight formed by an increasing subsequence.

**Input:**  
The first line of input contains a single integer _T_. _T_ test-cases follow. The first line of each test-case contains an integer _N_. The next line contains _a<sub>1</sub>, a<sub>2</sub> ,... , a<sub>N</sub>_ separated by a single space. The next line contains _w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>N</sub>_ separated by a single space.

**Output:**  
For each test-case output a single integer: The maximum weight of increasing subsequences of the given sequence.  

**Constraints:**  
1 <= _T_ <= 5  
1 <= _N_ <= 150000  
1 <= _a<sub>i</sub>_ <= 10<sup>9</sup>, where _i ∈ [1..N]_    
1 <= _w<sub>i</sub>_ <= 10<sup>9</sup>, where _i ∈ [1..N]_  

**Sample Input:**

    2  
    4  
    1 2 3 4  
    10 20 30 40  
    8  
    1 2 3 4 1 2 3 4  
    10 20 30 40 15 15 15 50

**Sample Output:**

    100  
    110

**Explanation:**  
In the first sequence, the maximum size increasing subsequence is 4, and there's only one of them. We choose `B = [(1, 10), (2, 20), (3, 30), (4, 40)]`, and we have `Weight(B) = 100`.

In the second sequence, the maximum size increasing subsequence is still 4, but there are now 5 possible subsequences:

    1 2 3 4  
    10 20 30 40

    1 2 3 4  
    10 20 30 50

    1 2 3 4  
    10 20 15 50

    1 2 3 4  
    10 15 15 50

    1 2 3 4  
    15 15 15 50

Of those, the one with the greatest weight is `B = [(1, 10), (2, 20), (3, 30), (4, 50)]`, with `Weight(B) = 110`.

Please note that this is not the maximum weight generated from picking the highest value element of each index. That value, 115, comes from [(1, 15), (2, 20), (3, 30), (4, 50)], which is not a valid subsequence because it cannot be created by only deleting elements in the original sequence.

## Constraints

1 <= T <= 5

1 <= N <= 150000

1 <= ai <= 109, where i ∈ [1..N]

1 <= wi <= 109, where i ∈ [1..N]

## Sample Input

2
4
1 2 3 4
10 20 30 40
8
1 2 3 4 1 2 3 4
10 20 30 40 15 15 15 50

## Sample Output

100
110

## Explanation

In the first sequence, the maximum size increasing subsequence is 4, and there's only one of them. We choose B = [(1, 10), (2, 20), (3, 30), (4, 40)], and we have Weight(B) = 100.

In the second sequence, the maximum size increasing subsequence is still 4, but there are now 5 possible subsequences:

1 2 3 4
10 20 30 40

1 2 3 4
10 20 30 50

1 2 3 4
10 20 15 50

1 2 3 4
10 15 15 50

1 2 3 4
15 15 15 50

Of those, the one with the greatest weight is B = [(1, 10), (2, 20), (3, 30), (4, 50)], with Weight(B) = 110.

Please note that this is not the maximum weight generated from picking the highest value element of each index. That value, 115, comes from [(1, 15), (2, 20), (3, 30), (4, 50)], which is not a valid subsequence because it cannot be created by only deleting elements in the original sequence.
