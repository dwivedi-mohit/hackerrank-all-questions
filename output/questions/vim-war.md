# Vim War

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 120
- **Success Ratio:** 0.7359267734553776
- **Total Submissions:** 2185
- **Solved Count:** 1608
- **URL:** https://www.hackerrank.com/challenges/vim-war

## Problem Statement

A war has broken down between Vim and Emacs. Gedit, being Vim's ally, is captured by Emacs as a prisoner of war and it is up to Vim to rescue him by defeating Emacs.

For this task, Vim has to assemble an army of appropriate skills. He can choose a **non-empty** subset of soldiers from a set of $N$ soldiers (numbered from $1$ to $N$). Each soldier has some subset of skills out of $M$ different skills (numbered from $1$ to $M$). The skill-set of an army is the union of skill-sets of its constituent soldiers. To win the war, Vim needs to know how many different subsets of soldiers satisfy his skill-set requirement. Since the answer can be huge, print it modulo $10^9 + 7$. 

Note : The chosen army's skill-set must **exactly** match the skill-set requirement of Vim (i.e no extra skills must be present in the army's skill-set than what is required).


## Input Format

The first line contains $N$ and $M$, the number of soldiers to choose from and the number of different skills possible respectively.  
The next $N$ lines contain $M$ boolean characters each. If the $j^{th}$ character of the $i^{th}$ line is $1$, then the $i^{th}$ soldier possess the $j^{th}$ skill and if it is $0$, then not.  
The last line contains $M$ boolean characters denoting the requirement skill-set of Vim where the $j^{th}$ character being $1$ signifies that Vim wants the $j^{th}$ skill to be present in his final army and not, otherwise.


## Output Format

Output in a single line the required answer, as explained above.  


## Constraints

$1 \le N \le 10^5$  
$1 \le M \le 20 $  


## Sample Input

4 2
00
10
01
11
11

## Explanation

Vim wants both the skills to be present in his selected army. Hence, he can choose the following subsets of soldiers:

-

-

-

-

-

-

-

-

-

-

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
