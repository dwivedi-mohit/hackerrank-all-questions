# Hard Disk Drives

- **Domain:** python
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.7634827810266407
- **Total Submissions:** 1539
- **Solved Count:** 1175
- **URL:** https://www.hackerrank.com/challenges/hard-drive-disks

## Problem Statement

There are $n$ *pairs* of hard disk drives (HDDs) in a cluster. Each HDD is located at an integer coordinate on an infinite straight line, and each pair consists of one *primary* HDD and one *backup* HDD.

Next, you want to place $k$ computers at integer coordinates on the same infinite straight line. Each *pair* of HDDs must then be connected to a single computer via *wires*, but a computer can have any number (even zero) of HDDs connected to it. The *length* of a wire connecting a single HDD to a computer is the absolute value of the distance between their respective coordinates on the infinite line. We consider the *total length* of wire used to connect all the HDDs to computers to be the sum of the lengths of all the wires used to connect HDDs to computers. Note that both the primary and secondary HDDs in a pair *must* connect to the same computer.

Given the locations of $n$ pairs (i.e., primary and backup) of HDDs and the value of $k$, place all $k$ computers in such a way that the total length of wire needed to connect each pair of HDDs to computers is *minimal*. Then print the total length on a new line.

## Input Format

The first line contains two space-separated integers denoting the respective values of $n$ (the number of *pairs* of HDDs) and $k$ (the number of computers). 		
Each line $i$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $a_i$ (coordinate of the primary HDD) and $b_i$ (coordinate of the backup HDD) for a pair of HDDs.

## Output Format

Print a single integer denoting the minimum total length of wire needed to connect all the pairs of HDDs to computers.

## Constraints

+ $2 \le k \le n \le 10^5$  
+ $4 \le k \times n \le 10^5$  
+ $-10^9 \le a_i, b_i \le 10^9$  

## Sample Input

5 2
6 7
-1 1
0 1
5 2
7 3

## Explanation

For the given Sample Case, it's optimal to place computers at positions  and  on our infinite line. We then connect the second () and the third () pairs of HDDs to the first computer (at position ) and then connect the remaining pairs to the second computer (at position ).

We calculate the wire lengths needed to connect the drives to each computer. The amount of wire needed to connect the second and third drives to the first computer is , and the amount of wire needed to connect the rest of the drives to the second computer is . When we sum the lengths of wire needed to connect all pairs of drives to the two computers, we get a total length of . Thus, we print  as our answer.
