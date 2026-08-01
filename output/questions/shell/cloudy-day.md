# Cloudy Day 

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 45
- **Success Ratio:** 0.5176527879230582
- **Total Submissions:** 8214
- **Solved Count:** 4252
- **URL:** https://www.hackerrank.com/challenges/cloudy-day

## Problem Statement

Quibdó in Colombia is one among the cities that receive maximum rainfall in the world.
____________________________________________________________________________________

All year round, the city is covered in clouds. The city has many towns, located on a one-dimensional line. The positions and populations of each town on the number line are known to you. 
Every cloud covers all towns located at a certain distance from it. A town is said to be in *darkness* if there exists *at least* one cloud such that the town is within the cloud's range. Otherwise, it is said to be *sunny*.

![image](https://s3.amazonaws.com/hr-assets/0/1517215384-44e72c8b06-cloudyday.png)

The city council has determined that they have enough money to remove *exactly one* cloud using their latest technology. Thus they want to remove the cloud such that the fewest number of people are left in darkness after the cloud is removed. What is the maximum number of people that will be in a sunny town after removing exactly one cloud?

*Note:* If a town is not covered by any clouds, then it is already considered to be sunny, and the population of this town must also be included in the final answer.

Complete the function `maximumPeople` which takes four arrays representing the populations of each town, locations of the towns, locations of the clouds, and the extents of coverage of the clouds respectively, and returns the maximum number of people that will be in a sunny town after removing exactly one cloud.





## Input Format

The first line of input contains a single integer $n$, the number of towns.

The next line contains $n$ space-separated integers $p_i$. The $i^\text{th}$ integer in this line denotes the population of the $i^\text{th}$ town.  

The next line contains $n$ space-separated integers $x_i$ denoting the location of the $i^\text{th}$ town on the one-dimensional line.

The next line consists of a single integer $m$ denoting the number of clouds covering the city.  

The next line contains $m$ space-separated integers $y_i$ the $i^\text{th}$ of which denotes the location of the $i^\text{th}$ cloud on the coordinate axis.

The next line consists of $m$ space-separated integers $r_i$ denoting the range of the $i^\text{th}$ cloud. 

*Note:* The range of each cloud is computed according to its location, i.e., the $i^\text{th}$ cloud is located at position $y_i$ and it covers every town within a distance of $r_i$ from it. In other words, the $i^\text{th}$ cloud covers every town with location in the range $[y_i-r_i, y_i+r_i]$.




## Output Format

Print a single integer denoting the maximum number of people that will be in a sunny town by removing exactly one cloud.


## Constraints

- $1 \le n \le 2 \times 10^5$
- $1 \le m \le 10^5$
- $1 \le x_i, y_i, r_i, p_i, \le 10^9$

<!-- TODO add subtask -->

## Sample Input

2
10 100
5 100
1
4
1

## Sample Output

110

## Explanation

In the sample case, there is only one cloud which covers the first town. Our only choice is to remove this sole cloud which will make all towns sunny, and thus, all  people will live in a sunny town.

As you can see, the only cloud present, is at location  on the number line and has a range , so it covers towns located at ,  and  on the number line. Hence, the first town is covered by this cloud and removing this cloud makes all towns sunny.
