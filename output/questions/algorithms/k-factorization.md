# K Factorization

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.8090593486526698
- **Total Submissions:** 6049
- **Solved Count:** 4894
- **URL:** https://www.hackerrank.com/challenges/k-factorization

## Problem Statement

At the time when Pythagoreanism was prevalent, people were also focused on different ways to factorize a number. In one class, Pythagoras asked his disciples to solve one such problem, _Reverse Factorization_. They were given a set of integer, $A = \{a_1, a_2, \cdots,  a_K\}$, and an integer $N$. They need to find the a way to reach $N$, starting from $1$, and at each step multiplying current value by any element of $A$. But soon they realised that there may exist more than one way to reach $N$. So they decided to find a way in which number of states are least. All of sudden they started on this new problem. People solved it and then started shouting their answer. CRAP!!!. There still exists multiple answers. So finally after much consideration, they settled on the lexicographically smallest series among those solutions which contains the least number of states.

For example, if $N = 12$ and $A = {2, 3, 4}$ then following ways exists  

```
(a) 1  ->  2  ->  4  ->  12
       x2     x2     x3

(b) 1  ->  4  ->  12
       x4     x3

(c) 1  ->  3  ->  12
       x3     x4
```

Here `(a)` is not the minimal state, as it has $4$ states in total. While `(b)` and `(c)` are contenders for answer, both having 3 states, `(c)` is lexicographically smaller than `(b)` so it is the answer. In this case you have to print `1 3 12`. If there exists no way to reach $N$ print `-1`.   


## Input Format

Input contains two lines where first line contains two space separated integer, $N$ and $K$, representing the final value to reach and the size of set $A$, respectively. Next line contains `K` space integers representing the set $A = \{a_1, a_2, \cdots,  a_K\}$.



## Output Format

Print the steps to reach $N$ if it exists. Otherwise print `-1`.



## Constraints

+ $1 \le N \le 10^9$  
+ $1 \le K \le 20$  
+ $2 \le a_i \le 20$, where $i \in [1,K]$  
+ $a_i \ne a_j$, where $1 \le i, j \le K$ AND $i \ne j$  

**Note:**  

* _Lexicographical order:_ If $list1 = [p_1, p_2, \cdots, p_m]$ and $list2 = [q_1, q_2, \cdots, q_n]$ are two ordered lists, then $list1$ is lexicographically smaller than $list2$ if any one of the following condition satisfies.  

  + $p_i = q_i, \forall i \in [1,m]$ AND $m < n$.  
  + $p_i = q_i, \forall i \in [1,k]$ AND $k < min(m, n)$ AND $p_{k+1} < q_{k+1}$.  
 
* You need to find the _lexigraphically smallest_ series among those solutions which contains the least number of states.  



## Sample Input

12 3
2 3 4

## Sample Output

1 3 12

## Explanation

This is the same case which is explaned above.
