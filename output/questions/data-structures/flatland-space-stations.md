# Flatland Space Stations

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 25
- **Success Ratio:** 0.8186399605412709
- **Total Submissions:** 93262
- **Solved Count:** 76348
- **URL:** https://www.hackerrank.com/challenges/flatland-space-stations

## Problem Statement

Flatland is a country with a number of cities, some of which have space stations.  Cities are numbered consecutively and each has a road of $1 km$ length connecting it to the next city.  It is not a circular route, so the first city doesn't connect with the last city.  Determine the maximum distance from any city to its nearest space station.

**Example**   
$n=3$   
$c=[1]$   

There are $n = 3$ cities and city $1$ has a space station.  They occur consecutively along a route.  City $0$ is $1-0=1$ unit away and city $2$ is $2-1=1$ units away.  City $1$ is $0$ units from its nearest space station as one is located there.  The maximum distance is $1$.

**Function Description**  

Complete the *flatlandSpaceStations* function in the editor below.   

flatlandSpaceStations has the following parameter(s):  

- *int n:* the number of cities  
- *int c[m]:* the indices of cities with a space station   

**Returns**   
- *int:* the maximum distance any city is from a space station  

## Input Format

The first line consists of two space-separated integers, $n$ and $m$. 	
The second line contains $m$ space-separated integers, the indices of each city that has a space-station. These values are *unordered* and distinct.

## Output Format


**Sample Input 0**
<pre>
STDIN	Function
-----	--------
5 2		n = 5, c[] size m = 2
0 4		c = [0, 4]
</pre>

**Sample Output 0**

    2
    
**Explanation 0**

This sample corresponds to following graphic:  

![hreasy(5).png](https://s3.amazonaws.com/hr-challenge-images/15233/1449763282-eddfbea90c-hreasy5.png)  

The distance to the nearest space station for each city is listed below:

* $c[0]$ has distance $0 \ km$, as it contains a space station.
* $c[1]$ has distance $1 \ km$ to the space station in $c[0]$.
* $c[2]$ has distance $2 \ km$ to the space stations in $c[0]$ and $c[4]$.
* $c[3]$ has distance $1 \ km$ to the space station in $c[4]$.
* $c[4]$ has distance $0 \ km$, as it contains a space station.

We then take $max(0,1,2,1,0) = 2$.

**Sample Input 1**

    6 6
    0 1 2 4 3 5
    
**Sample Output 1**

    0

**Explanation 1**

In this sample, $n = m$ so every city has space station and we print $0$ as our answer.

## Constraints

- $1 \le n \le 10^5$
- $1 \le m \le n$
- There will be at least $1$ city with a space station.
- No city has more than one space station.

## Sample Input

STDIN   Function
-----   --------
5 2     n = 5, c[] size m = 2
0 4     c = [0, 4]

## Sample Output

2

## Explanation

This sample corresponds to following graphic:

The distance to the nearest space station for each city is listed below:

-  has distance , as it contains a space station.

-  has distance  to the space station in .

-  has distance  to the space stations in  and .

-  has distance  to the space station in .

-  has distance , as it contains a space station.

We then take .
