# The Value of Friendship

- **Domain:** data-structures
- **Difficulty:** Hard
- **Max Score:** 55
- **Success Ratio:** 0.6804770872567483
- **Total Submissions:** 3186
- **Solved Count:** 2168
- **URL:** https://www.hackerrank.com/challenges/value-of-friendship

## Problem Statement

You're researching friendships between groups of $n$ new college students where each student is distinctly numbered from $1$ to $n$. At the beginning of the semester, no student knew any other student; instead, they met and formed individual friendships as the semester went on. The friendships between students are:

- *Bidirectional.* If student $a$ is friends with student $b$, then student $b$ is also friends with student $a$.
- *Transitive.* If student $a$ is friends with student $b$ and student $b$ is friends with student $c$, then student $a$ is friends with student $c$. In other words, two students are considered to be friends even if they are only indirectly linked through a network of mutual (i.e., directly connected) friends. 

The purpose of your research is to find the maximum total value of a group's friendships, denoted by $total$. Each time a direct friendship forms between two students, you sum the number of friends that *each* of the $n$ students has and add the sum to $total$. 

You are given $q$ queries, where each query is in the form of an unordered list of $m$ distinct direct friendships between $n$ students. For each query, find the maximum value of $total$ among all possible orderings of formed friendships and print it on a new line.


## Input Format

The first line contains an integer, $q$, denoting the number of queries. The subsequent lines describe each query in the following format:

1. The first line contains two space-separated integers describing the respective values of $n$ (the number of students) and $m$ (the number of distinct *direct* friendships).
2. Each of the $m$ subsequent lines contains two space-separated integers describing the respective values of $x$ and $y$ (where $x \ne y$) describing a friendship between student $x$ and student $y$.

## Output Format

For each query, print the maximum value of $total$ on a new line.

## Constraints

+ $1 \le q \le 16$  
+ $1 \le n \le 10^5$   
+ $1 \le m \le \min(\frac{n \cdot (n-1)}{2}, 2 \times 10^5)$  

## Sample Input

1
5 4
1 2
3 2
4 2
4 3

## Sample Output

32

## Explanation

The value of  is maximal if the students form the  direct friendships in the following order:

- Students  and  become friends:

We then sum the number of friends that each student has to get .

- Students  and  become friends:

We then sum the number of friends that each student has to get .

- Students  and  become friends:

We then sum the number of friends that each student has to get .

- Students  and  become friends:

We then sum the number of friends that each student has to get .

When we add the sums from each step, we get . We then print  on a new line.
