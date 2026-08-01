# Toll Cost Digits

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.7445611402850713
- **Total Submissions:** 2666
- **Solved Count:** 1985
- **URL:** https://www.hackerrank.com/challenges/toll-cost-digits

## Problem Statement

The mayor of Farzville is studying the city's road system to find ways of improving its traffic conditions. Farzville's road system consists of $n$ junctions connected by $e$ bidirectional toll roads, where the $i^{th}$ toll road connects junctions $x_i$ and $y_i$. In addition, some junctions may not be reachable from others and there may be multiple roads connecting the same pair of junctions.   

Each toll road has a toll rate that's paid each time it's used. This rate varies depending on the direction of travel:  

- If traveling from $x_i$ to $y_i$, then the toll rate is $r_i$. 
- If traveling from $y_i$ to $x_i$, then the toll rate is $1000 - r_i$. It is guaranteed that $0 < r_i < 1000$.  

![image](https://s3.amazonaws.com/hr-challenge-images/0/1484787161-bee88db398-tollroads.png)

For each digit $d \in \{0,1,\ldots,9\}$, the mayor wants to find the number of ordered pairs of $(x,y)$ junctions such that $x \ne y$ and a path exists from $x$ to $y$ where the total cost of the tolls (i.e., the sum of all toll rates on the path) ends in digit $d$. Given a map of Farzville, can you help the mayor answer this question? For each digit $d$ from $0$ to $9$, print the the number of valid ordered pairs on a new line.

**Note**: Each toll road can be traversed an unlimited number of times in either direction. 

## Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of junctions) and $e$ (the number of roads). 		
Each line $i$ of the $e$ subsequent lines describes a toll road in the form of three space-separated integers, $x_i$, $y_i$, and $r_i$.  

## Output Format

Print ten lines of output. Each line $j$ (where $0 \le j \le 9$) must contain a single integer denoting the answer for $d = j$. For example, the first line must contain the answer for $d = 0$, the second line must contain the answer for $d = 1$, and so on.

## Constraints

* $1 \le n \le 10^5$  
* $1 \le e \le 2\cdot 10^5$  
* $1 \le x_i, y_i \le n$  
* $x_i \ne y_i$  
* $0 < r_i < 1000$  


## Sample Input

3 3
1 3 602
1 2 256
2 3 411

## Sample Output

0
2
1
1
2
0
2
1
1
2

## Explanation

The table below depicts the distinct pairs of junctions for each :

- - - - - - - - - -

Note the following:

- There may be multiple paths between each pair of junctions.

- Junctions and roads may be traversed multiple times. For example, the path  is also valid, and it has total cost of .

- An ordered pair can be counted for more than one . For example, the pair  is counted for  and .

- Each ordered pair must only be counted once for each . For example, the paths  and  both have total costs that end in , but the pair  is only counted once.
