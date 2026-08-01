# Journey to the Moon

- **Domain:** c
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.6294421170114682
- **Total Submissions:** 61823
- **Solved Count:** 38914
- **URL:** https://www.hackerrank.com/challenges/journey-to-the-moon

## Problem Statement

The member states of the UN are planning to send $2$ people to the moon. They want them to be from different countries.  You will be given a list of pairs of astronaut ID's.  Each pair is made of astronauts from the same country.  Determine how many pairs of astronauts from different countries they can choose from.

__Example__  

$n = 4$  
$astronaut = [1, 2], [2, 3]$   

There are $4$ astronauts numbered $0$ through $3$.  Astronauts grouped by country are $[0]$ and $[1, 2, 3]$.  There are $3$ pairs to choose from: $[0,1], [0,2]$ and $[0,3]$.

**Function Description**  

Complete the *journeyToMoon* function in the editor below.    

journeyToMoon has the following parameter(s):  

- *int n:* the number of astronauts  
- *int astronaut[p][2]:* each element $astronaut[i]$ is a $2$ element array that represents the ID's of two astronauts from the same country  

**Returns**  
- *int:* the number of valid pairs

## Input Format

The first line contains two integers $n$ and $p$, the number of astronauts and the number of pairs.  
Each of the next $p$ lines contains $2$ space-separated integers denoting astronaut ID's of two who share the same nationality. 


## Output Format

  

## Constraints

* $1 \le n \le 10^5$  
* $1 \le p \le 10^4$  


## Sample Input

5 3
0 1
2 3
0 4

## Sample Output

6

## Explanation

Persons numbered  belong to one country, and those numbered  belong to another. The UN has  ways of choosing a pair:
