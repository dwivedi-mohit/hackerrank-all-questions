# Roy and alpha-beta trees

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 120
- **Success Ratio:** 0.9047120418848168
- **Total Submissions:** 2865
- **Solved Count:** 2592
- **URL:** https://www.hackerrank.com/challenges/roy-and-alpha-beta-trees

## Problem Statement

Roy has taken a liking to the [Binary Search Trees](https://en.wikipedia.org/wiki/Binary_search_tree)(*BST*). He is interested in knowing the number of ways an array $A$ of $N$ integers can be arranged to form a *BST*. Thus, he tries a few combinations, and notes down the numbers at the odd levels and the numbers at the even levels. 

You're given two values, *alpha* and *beta*. Can you calculate the sum of *Liking* of all possible *BST's* that can be formed from an array of $N$ integers? *Liking* of each *BST* is defined as follows 

    (sum of numbers on even levels * alpha) - (sum of numbers on odd levels * beta)


**Note** 

+ The root element is at level $0$ ( Even )
+ The elements smaller or equal to the parent element are present in the left subtree, elements greater than or equal to the parent element are present in the right subtree.  Explained [here](https://www.hackerrank.com/contests/w4/challenges/roy-and-alpha-beta-trees/forum/questions/6070)

If the answer is no less than $10^9+9$, output the answer % $10^9+9$. 

(If the answer is less than $0$, keep adding $10^9+9$ until the value turns non negative.)

**Input Format**  
The first line of input file contains an integer, $T$, denoting the number of test cases to follow.  
Each testcase comprises of $3$ lines.  
The first line contains $N$, the number of integers.  
The second line contains two space separated integers, _alpha_ and _beta_.  
The third line contains space separated $N$ integers_, denoting the $i^{th}$ integer in array $A[i]$.  

**Output Format**  
Output $T$ lines. Each line contains the answer to its respective test case. 

**Constraints**  

$1 \le T \le 10$  
$1 \le N \le 150$  
$1 \le A[i] \le 10^9$  
$1 \le alpha,beta \le 10^{9}$  

**Sample Input**

<pre>
4
1
1 1
1
2
1 1
1 2
3
1 1
1 2 3
5
1 1
1 2 3 4 5
</pre>

**Sample Output**

<pre>
1
0
6
54
</pre>

**Explanation**

There are $4$ test cases in total. 

+ For the first test case, only $1$ BST can be formed with `1` as the root node. Hence the *Liking* / sum is $1$. 

+ For the second test case, we get 2 BSTs of the form, the *Liking* of the first tree is $1 * 1 - 2 * 1 = -1$ and $2 * 1 - 1 * 1 = 1$, this sums to $0$, hence the answer. 


<pre>
1                  2 
 \                /
  2              1
</pre>

+ For the third test case, we get $5$ BSTs. The *Liking* of each of the BST from left  to right are $2, -2, 4, 2, 0$ which sums to $6$ and hence the answer.  

<pre>
1            2                 3          3      1
 \          / \               /          /        \
  2        1   3             1          2          3
   \                          \        /          /
    3                          2      1          2
</pre>

+ Similarly, for the fourth test case, the answer is $54$.  

## Input Format

The first line of input file contains an integer, , denoting the number of test cases to follow.

Each testcase comprises of  lines.

The first line contains , the number of integers.

The second line contains two space separated integers, alpha and beta.

The third line contains space separated  integers_, denoting the  integer in array .

## Output Format

Output  lines. Each line contains the answer to its respective test case.

## Sample Input

1
1 1
1
2
1 1
1 2
3
1 1
1 2 3
5
1 1
1 2 3 4 5

## Sample Output

0
6
54

## Explanation

There are  test cases in total.

- For the first test case, only  BST can be formed with 1 as the root node. Hence the Liking / sum is .

- For the second test case, we get 2 BSTs of the form, the Liking of the first tree is  and , this sums to , hence the answer.

1                  2
 \                /
  2              1

- For the third test case, we get  BSTs. The Liking of each of the BST from left  to right are  which sums to  and hence the answer.

1            2                 3          3      1
 \          / \               /          /        \
  2        1   3             1          2          3
   \                          \        /          /
    3                          2      1          2

- Similarly, for the fourth test case, the answer is .
