# Weighted Uniform Strings

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.7756387590198929
- **Total Submissions:** 76359
- **Solved Count:** 59227
- **URL:** https://www.hackerrank.com/challenges/weighted-uniform-string

## Problem Statement

A weighted string is a string of lowercase English letters where each letter has a *weight*.  Character weights are $1$ to $26$ from $a$ to $z$ as shown below:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1484319110-9529e3b407-uniform.png)

- The _weight of a string_ is the sum of the weights of its characters.  For example: 

    ![image](https://s3.amazonaws.com/hr-challenge-images/0/1484319417-dadc155c1a-uniform1.png)
- A *uniform string* consists of a single character repeated zero or more times. For example, ``ccc`` and ``a`` are uniform strings, but ``bcb`` and `cd` are not.

Given a string, $s$, let $U$ be the set of weights for all possible uniform contiguous  [substrings](https://en.wikipedia.org/wiki/Substring) of string $s$. There will be $n$ queries to answer where each query consists of a single integer. Create a return array where for each query, the value is ``Yes`` if $query[i] \in U$.  Otherwise, append ``No``.

**Note:** The $\in$ symbol denotes that $x[i]$ is an [element of](https://en.wikipedia.org/wiki/Element_(mathematics)) set $U$.

**Example**   
$s = \text{'abbcccdddd'}$   
$queries = [1, 7, 5, 4, 15]$. 

Working from left to right, weights that exist are:

	string	weight
    a		1
    b		2
    bb		4
    c		3
    cc		6
    ccc		9
    d		4
    dd		8
    ddd		12
    dddd	16

Now for each value in $queries$, see if it exists in the possible string weights.  The return array is `['Yes', 'No', 'No', 'Yes', 'No']`.

**Function Description**  

Complete the *weightedUniformStrings* function in the editor below. 

weightedUniformStrings has the following parameter(s):  
- *string s:* a string  
- *int queries[n]:* an array of integers   

**Returns**  
-	*string[n]:* an array of strings that answer the queries

## Input Format

The first line contains a string $s$, the original string. 	
The second line contains an integer $n$, the number of queries.		
Each of the next $n$ lines contains an integer $queries[i]$, the weight of a uniform subtring of $s$ that may or may not exist.

## Output Format

  

## Constraints

* $ 1 \le length of s, n \le 10^5 $
* $ 1 \le queries[i] \le 10^7 $
* $s$ will only contain lowercase English letters, ascii[a-z].

## Sample Input

abccddde
6
1
3
12
5
9
10

## Sample Output

Yes
Yes
Yes
Yes
No
No

## Explanation

The weights of every possible uniform substring in the string abccddde are shown below:

We print Yes on the first four lines because the first four queries match weights of uniform substrings of . We print No for the last two queries because there are no uniform substrings in  that have those weights.

Note that while de is a substring of  that would have a weight of , it is not a uniform substring.

Note that we are only dealing with contiguous substrings. So ccc is not a substring of the string ccxxc.
