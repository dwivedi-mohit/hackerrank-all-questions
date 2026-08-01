# Random

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.5682819383259912
- **Total Submissions:** 227
- **Solved Count:** 129
- **URL:** https://www.hackerrank.com/challenges/random

## Problem Statement

Given an array 'D' with n elements: d[0], d[1], ..., d[n-1], you can perform the following two steps on the array.  

1. Randomly choose two indexes (l, r) with l < r, swap (d[l], d[r])   
2. Randomly choose two indexes (l, r) with l < r, reverse (d[l...r]) (both inclusive)   

After you perform the first operation **a** times and the second operation **b** times, you randomly choose two indices _l_ & _r_ with _l_ < _r_ and calculate the S = sum(d[l...r]) (both inclusive).  

Now, you are to find the expected value of S.

**Input Format**  
The first line of the input contains 3 space separated integers - n, a and b.  
The next line contains n space separated integers which are the elements of the array *d*.   

    n a b
    d[0] d[1] ... d[n-1]

**Output Format**  
Print the expected value of S.  

    E(S)

**Constraints**  

2 <= n <= 1000  
1 <= a <= 10<sup>9</sup>  
1 <= b <= 10  

The answer will be considered correct, if the absolute or relative error doesn't exceed 10<sup>-4</sup>.  

**Sample Input #00:**

    3 1 1 
    1 2 3

**Sample Output #00:**

    4.666667

**Explanation #00:**

At step 1):  
You have three choices:  
1. swap(0, 1), 2 1 3  
2. swap(0, 2), 3 2 1  
3. swap(1, 2), 1 3 2  

At step 2):  
For every result you have three choices for reversing:   
1. [2 1 3] -> [1 2 3] [3 1 2] [2 3 1]  
2. [3 2 1] -> [2 3 1] [1 2 3] [3 1 2]  
3. [1 3 2] -> [3 1 2] [2 3 1] [1 2 3]  

So you have 9 possible arrays with each having a 1/9 probability.

For the last step:  
Each of the 9 arrays will have 3 possible sums with equal probability. For [1 2 3], you can get 1+2, 2+3 and 1+2+3.  
Since there will be 27 outcome for this input, one can calculate the expected value by finding sum of all 27 S and dividing it by 27. 

## Input Format

The first line of the input contains 3 space separated integers - n, a and b.

The next line contains n space separated integers which are the elements of the array d.

n a b
d[0] d[1] ... d[n-1]

## Output Format

Print the expected value of S.

E(S)

## Constraints

2 <= n <= 1000

1 <= a <= 109

1 <= b <= 10

The answer will be considered correct, if the absolute or relative error doesn't exceed 10-4.

Sample Input #00:

3 1 1
1 2 3

Sample Output #00:

4.666667

Explanation #00:

At step 1):

You have three choices:

1. swap(0, 1), 2 1 3

2. swap(0, 2), 3 2 1

3. swap(1, 2), 1 3 2

At step 2):

For every result you have three choices for reversing:

1. [2 1 3] -> [1 2 3] [3 1 2] [2 3 1]

2. [3 2 1] -> [2 3 1] [1 2 3] [3 1 2]

3. [1 3 2] -> [3 1 2] [2 3 1] [1 2 3]

So you have 9 possible arrays with each having a 1/9 probability.

For the last step:

Each of the 9 arrays will have 3 possible sums with equal probability. For [1 2 3], you can get 1+2, 2+3 and 1+2+3.

Since there will be 27 outcome for this input, one can calculate the expected value by finding sum of all 27 S and dividing it by 27.
