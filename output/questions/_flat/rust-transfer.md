# Rust & his Transfer

---

| Field | Value |
|---|---|
| **Slug** | `rust-transfer` |
| **Contest** | codeagon-2016 |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/rust-transfer |

---

## Problem Statement

Detective Rust is being transferred to a new station across the country and has a limited relocation bonus to get him there. In addition to the relocation bonus, he is entitled to *one* additional luxury taxi ride between any two cities en route his destination. He may or may not choose to travel by the taxi.
 
Rust wonders about the most optimal way (in terms of time of cost) of traveling from his originating station to his new station *with or without* using his entitled taxi ride. The intercity map is given as a graph with $N$ nodes (labeled from $1$ to $N$), and Rust's initial station is node $S$. There are two undirected edges between each of the given nodes; one denotes the cost of a path using Rust's own mode of travel, and the other denotes the cost of a taxi between a pair of cities.
 
Help Rust minimize the cost of his move!

## Input Format

The first line contains $T$, the number of test cases. 

For each test case:		
The first line contains two space-separated integers, $N$ (the number of cities in the map) and $M$ (the number of roads in the map), respectively.		
The next $M$ lines each have four space separated integers $x$, $y$, $r$, and $t$, respectively; $x$ and $y$ denote two cities connected by a road, $r$ is Rust's regular travel cost to take the road, and $t$ is the cost of taking a taxi on this road.		
The last line has two space-separated integers, $S$ (Rust's starting station) and $D$ (Rust's destination station), respectively.

**Constraints**  
$1 \le T \le10$  
$2 \le N \le 3000$  
$1 \le M \le N \times (N-1)$  
$1 \le x,y,S,D \le N$  
$1 \le r,t \le 500$

## Output Format

For each test case, print a single line with Rust's minimum travel cost; if the destination ($D$) is unreachable from the source node ($S$), print $-1$.
