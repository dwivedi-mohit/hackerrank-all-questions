# Fighting Armies

- **Domain:** cpp
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.7712665406427222
- **Total Submissions:** 529
- **Solved Count:** 408
- **URL:** https://www.hackerrank.com/challenges/fighting-armies

## Problem Statement

Your country is at war! 

As a General, you initially have $N$ armies numbered from $1$ to $N$ under your command. Each army consists of some number of soldiers, and each soldier is assigned an integer, $c$, representative of his or her combat ability. Since, you are responsible for all of them, you want to give orders to your armies and query them about their current state. You must handle $Q$ events, where each event is one of the $4$ following types:

1. $\texttt{findStrongest(i)}$ - Print the maximum combat ability of any soldier in army $i$.
2. $\texttt{strongestDied(i})$ - A soldier with the maximum combat ability among all soldiers in army $i$ has died, so the soldier is removed from the army.
3. $\texttt{recruit(i, c)}$ - A soldier with combat ability $c$ has joined army $i$.
4. $\texttt{merge(i, j)}$ - Armies $i$ and $j$ are merged into a single army $i$, and army $j$ is removed (ceases to exist).

**Note:** The input can be quite large, so we suggest you use fast I/O methods.

## Input Format

The first line contains $2$ space-separated integers, $N$ (the number of armies you command) and $Q$ (the number of events taking place), respectively. Each of the $Q$ subsequent lines describes a single event. 		

Each event first contains an integer, $t$, describing the event type. 	
If $t = 1$ or $t = 2$, the line contains $1$ more integer denoting the parameter of the event. 	
If $t = 3$ or $t = 4$, the line contains $2$ more integers denoting the respective parameters of the event.

## Output Format

For each event of type $1$, print a single line containing $1$ integer denoting the answer for the event.

## Constraints

- $1 \leq N \leq 1100000$  
- $1 \leq Q \leq 2200000$  
- $1 \leq c \leq 10^7$  
- $1 \leq i, j \leq N \text{, where } i \neq j$  
- $\text{Indices of armies in the input represent valid armies at the time they are given.}$

## Sample Input

2 6
3 1 10
3 2 20
4 1 2
1 1
2 1
1 1

## Sample Output

10

## Explanation

Here is a breakdown of each event:

- A soldier having combat ability  is added to army .

- A soldier having combat ability  is added to army .

- Armies  and  are merged into army  (and army  no longer exists).

- The maximum combat ability of a soldier in army  is .

- The soldier having combat ability  is removed from army .

- The maximum combat ability of a soldier in army  is .
