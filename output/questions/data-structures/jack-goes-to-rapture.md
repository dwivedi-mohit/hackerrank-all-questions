# Jack goes to Rapture 

- **Domain:** data-structures
- **Difficulty:** Medium
- **Max Score:** 80
- **Success Ratio:** 0.7248898915028467
- **Total Submissions:** 9309
- **Solved Count:** 6748
- **URL:** https://www.hackerrank.com/challenges/jack-goes-to-rapture

## Problem Statement

Jack has just moved to a new city called Rapture. He wants to use the public public transport system. The fare rules are as follows:  

1. Each pair of connected stations has a fare assigned to it regardless of direction of travel.  
2. If Jack travels from station A to station B, he only has to pay the  difference between (the fare from A to B) and (the cumulative fare paid to reach station A),  [_fare(A,B) - total fare to reach station A_].  If the difference is negative, travel is free of cost from A to B.  

Jack is low on cash and needs your help to figure out the most cost efficient way to go from the first station to the last station. Given the number of stations $g\_nodes$ (numbered from $1$ to $g\_nodes$), and the fares (weights) between the $g\_edges$ pairs of stations that are connected, determine the lowest fare from station $1$ to station $g\_nodes$.  

**Example**     
$g\_nodes = 4$   
$g\_from = [1, 1, 2, 3]$  
$g\_to = [2, 3, 4, 4]$   
$g\_weight = [20, 5, 30, 40]$   
   
   
The graph looks like this:

![image](https://s3.amazonaws.com/hr-assets/0/1543613276-d83580f86b-raptureexample.png)  
Travel from station $1 \rightarrow 2 \rightarrow 4$ costs $20$ for the first segment ($1 \rightarrow 2$) then the cost differential, an additional $30-20=10$ for the remainder.  The total cost is $30$.   

Travel from station $1 \rightarrow 3 \rightarrow 4$ costs $5$ for the first segment, then an additional $40 - 5 = 35$ for the remainder, a total cost of $40$.   

The lower priced option costs $30$.  

**Function Description**  
Complete the _getCost_ function in the editor below.  

getCost has the following parameters:

- *int g_nodes:* the number of stations in the network  
- *int g_from[g_edges]:* end stations of a bidirectional connection  
- *int g_to[g_edges]:* $g\_from[i]$ is connected to $g\_to[i]$  at cost $g\_weight[i]$  
- *int g_weight[g_edges]:* the cost of travel between associated stations  

**Prints**   
- *int or string:* the cost of the lowest priced route from station $1$ to station $g\_nodes$ or `NO PATH EXISTS`.  No return value is expected.

## Input Format

The first line contains two space-separated integers, $g\_nodes$ and $g\_edges$, the number of stations and the number of connections between them.    
Each of the next $g\_edges$ lines contains three space-separated integers, $g\_from\text{, } g\_to$ and $g\_weight$, the connected stations and the fare between them.  


## Constraints

* $1 \le g\_nodes \le 50000$  
* $1 \le g\_edges \le 500000$  
* $1 \le g\_weight[i] \le 10^7$
