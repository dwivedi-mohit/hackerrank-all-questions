# The Story of a Tree

- **Domain:** java
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.628792161296401
- **Total Submissions:** 5307
- **Solved Count:** 3337
- **URL:** https://www.hackerrank.com/challenges/the-story-of-a-tree

## Problem Statement

One day Bob drew a [tree](https://en.wikipedia.org/wiki/Tree_(data_structure)), $T$, with $n$ nodes and $n-1$ edges on a piece of paper. He soon discovered that parent of a node depends on the root of the tree. The following images shows an example of that:

![image](https://s3.amazonaws.com/hr-assets/0/1487245443-a6966b94d1-treestory.png)

Learning the fact, Bob invented an exciting new game and decided to play it with Alice. The rules of the game is described below:


1. Bob picks a random node to be the tree's *root* and keeps the identity of the chosen node a secret from Alice. Each node has an equal probability of being picked as the root.
2. Alice then makes a list of $g$ guesses, where each guess is in the form ``u v`` and means Alice guesses that $parent(v)=u$ is *true*. It's guaranteed that an undirected edge connecting $u$ and $v$ exists in the tree. 
3. For each correct guess, Alice earns one point. Alice wins the game if she earns at least $k$ points (i.e., at least $k$ of her guesses were *true*).

Alice and Bob play $q$ games. Given the tree, Alice's guesses, and the value of $k$ for each game, find the probability that Alice will win the game and print it on a new line as a reduced fraction in the format `p/q`.

## Input Format

The first line contains an integer, $q$, denoting the number of different games. The subsequent lines describe each game in the following format:

1. The first line contains an integer, $n$, denoting the number of nodes in the tree.
2. The $n-1$ subsequent lines contain two space-separated integers, $u$ and $v$, defining an undirected edge between nodes $u$ and $v$. 
3. The next line contains two space-separated integers describing the respective values of $g$ (the number of guesses) and $k$ (the minimum score needed to win).
4. Each of the $g$ subsequent lines contains two space-separated integers, $u$ and $v$, indicating Alice guesses $parent(v)=u$.

## Output Format

Print the probability as a reduced fraction in the format `p/q`.

**Note:** Print `0/1` if the probability is $0$ and print `1/1` if the probability is $1$.

## Constraints

- $1 \leq q \leq 5 $
- $1 \leq n \leq 10^5 $
- $1 \leq u,v \leq n$
- $1 \leq g,k \leq 10^5$
- The sum of $n$ over all test cases won't exceed $2 \times 10^5$.
- No two guesses will be identical. 

**Scoring**

- For $25\%$ of the maximum score, $1 \leq n \leq 10^3$.
- For $100\%$ of the maximum score, $1 \leq n \leq 10^5$.

## Sample Input

2
4
1 2
1 3
3 4
2 2
1 2
3 4
3
1 2
1 3
2 2
1 2
1 3

## Sample Output

1/2
1/3

## Explanation

Alice and Bob play the following  games:

- Alice makes two guesses,  and , meaning she guessed that  and . To win the game, at least  of her guesses must be true.

In the diagrams below, you can see that at least  guesses are true if the root of the tree is either node  or :

There are  nodes in total and the probability of picking node  or  as the root is , which reduces to .

- In this game, Alice only wins if node  is the root of the tree. There are  nodes in total, and the probability of picking node  as the root is .
