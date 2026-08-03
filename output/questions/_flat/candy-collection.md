# Candy Collection

---

| Field | Value |
|---|---|
| **Slug** | `candy-collection` |
| **Contest** | hourrank-22 |
| **Difficulty** | Hard |
| **Score** | 70 |
| **URL** | https://www.hackerrank.com/challenges/candy-collection |

---

## Problem Statement

Halloween is here! Mancunian runs a candy shop and his friend Liverbird is here to buy candies to give to the children. There are $n$ *boxes* of candies in a line. The $i^\text{th}$ box contains $V_i$ candies, and the $i^\text{th}$ box has color $T_i$. Liverbird wants to buy all the boxes! But the problem is that he does not have a lot of money. :(


Liverbird will carry all the boxes home using crates. A *crate* will contain a contiguous sequence of candy boxes. (*Note:* Don't confuse boxes with crates; crates will contain boxes and boxes contain candies.) Each box belongs to exactly one crate. Liverbird is also choosy about the boxes in a single crate. He does not want any two boxes in the same crate to have the same color. The cost of a crate is the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the number of candies in the boxes it contains (don't ask Mancunian why). For example, the cost of a crate containing three boxes, containing 1, 2 and 3 candies respectively, is 1 OR 2 OR 3 = 3.  

What is the minimum total cost needed to buy all the boxes?

## Input Format

The first line of input contains $n$, the number of candy boxes.  
The second line contains $n$ space-separated integers, the $i^\text{th}$ of which represents $T_i$, the color of the $i^\text{th}$ box. Colors are represented as positive integers.   
The third line contains $n$ space-separated integers, the $i^\text{th}$ of which represents the number of candies $V_i$ in the $i^\text{th}$ box.

## Output Format

Print a single integer which is the answer to the given problem.

## Constraints

- $1 \le n \le 500000$  
- $1 \le T_i \le 10^{6}$  
- $0 \le V_i \le 10^{6}$  

**Subtask**  

- For 30% of the maximum points, $1 \le n \le 5000$
