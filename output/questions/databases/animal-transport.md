# Animal Transport

- **Domain:** databases
- **Difficulty:** Hard
- **Max Score:** 70
- **Success Ratio:** 0.8763754045307444
- **Total Submissions:** 1545
- **Solved Count:** 1354
- **URL:** https://www.hackerrank.com/challenges/animal-transport

## Problem Statement

Capeta is working part-time for an animal shipping company. He needs to pick up animals from various zoos and drop them to other zoos. The company ships four kinds of animals: elephants, dogs, cats, and mice.

There are $m$ zoos, numbered $1$ to $m$. Also, there are $n$ animals. For each animal $i$, Capeta knows its type $t_i$ (`E` for elephant, `D` for dog, `C` for cat and `M` for mouse), source zoo $s_i$ where Capeta has to pick it up from, and destination zoo $d_i$ where Capeta needs to deliver it to. 

![image](https://s3.amazonaws.com/hr-assets/0/1512382341-9d32c6b251-zoo.png)

Capeta is given a truck with a huge capacity where $n$ animals can easily fit. He is also given additional instructions:

1. He must visit the zoos in **increasing** order. He also cannot skip zoos. 

2. **Dogs** are scared of **elephants**, so he is not allowed to bring them together at the same time. 
3. **Cats** are scared of **dogs**, so he is not allowed to bring them together at the same time. 
4. **Mice** are scared of **cats**, so he is not allowed to bring them together at the same time. 
5. **Elephants** are scared of **mice**, so he is not allowed to bring them together at the same time. 

Also, loading and unloading animals are complicated, so once an animal is loaded onto the truck, that animal will only be unloaded at its destination. 

Because of these reasons, Capeta might not be able to transport all animals. He will need to ignore some animals. Which ones? The company decided to leave that decision for Capeta. He is asked to prepare a report and present it at a board meeting of the company.

Capeta needs to report the minimum number of zoos that must be reached so that she is able to transport $x$ animals, for each $x$ from $1$ to $n$. 

Complete the function `minimumZooNumbers` and return an integer array where the $x^\text{th}$ integer is the minimum number of zoos that Capeta needs to reach so that she is able to transport $x$ animals, or $-1$ if it is impossible to transport $x$ animals. 

He is good at driving, but not so much at planning. Hence, he needs your help.

## Input Format

The first line contains a single integer $t$, the number of test cases.

Each test case consists of four lines. The first line contains two space-separated integers $m$ and $n$. The second line contains $n$ space-separated characters $t_1, t_2, \ldots, t_n$. The third line contains $n$ space-separated integers $s_1, s_2, \ldots, s_n$. The fourth line contains $n$ space-separated integers $d_1, d_2, \ldots, d_n$.  

$t_i$, $s_i$ and $d_i$ are the details for the $i$th animal, as described in the problem statement.


## Output Format

For each case, print a single line containing $n$ space-separated integers, where the $x^\text{th}$ integer is the minimum number of zoos that Capeta needs to reach so that she is able to transport $x$ animals. If it is not possible to transport $x$ animals at all, then put $-1$ instead.

## Constraints

- $1 \leq t \leq 10$  
- $1 \le m, n \le 5\cdot 10^4$  
- $1 \le s_i, d_i \le m$  
- $s_i \neq d_i$
- $t_i$ is either `E`, `D`, `C` or `M`

**Subtasks**  

- For $30\%$ of the total score, $m, n \le 10^3$  

## Sample Input

2
10 3
E D C
4 1 4
7 5 8
10 6
E D C M E D
1 1 1 2 9 7
2 2 2 4 10 10

## Sample Output

5 8 -1
2 2 4 10 -1 -1

## Explanation

First Test Case

Capeta can transport one animal by traveling up to zoo number . Just drop the dog there. Next, in order to transport  animals (elephant and cat), Capeta has to go up to zoo number .

Second Test Case

-  Animal: Drop the elephant to zoo .

-  Animal: Drop the elephant and cat to zoo .

-  Animal: Drop the elephant and cat to zoo . Then drop the mouse to zoo .

-  Animal: Drop the elephant and cat to zoo . Then drop the mouse to zoo . Finally, drop either the elephant or the dog to .

- It is impossible to transport  or  animals.
