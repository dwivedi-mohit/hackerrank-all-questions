# K-Means Clustering

## Metadata

- **ID:** 1542120
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Binary Search, Sorting, Greedy
- **Skills:** Problem Solving (Intermediate)
- **Languages:** c, ,, c, l, o, j, u, r, e, ,

## Summary

This coding question evaluates binary search, sorting, and greedy algorithm concepts, ideal for mid-level roles. The problem requires determining the optimal placement of cluster centers to minimize the maximum distance between data points and their nearest center in a k-means clustering scenario.

## Problem Statement

In a k-means clustering problem, determine the best possible clustering quality by optimally placing cluster centers.

Quality is measured by the maximum distance between any data point and its nearest cluster center. The goal is to minimize this maximum distance.

Example

n = 5 (number of data points)

location = [4, 1, 6, 7, 2] (data point locations)

k = 2 (number of clusters)

 

	If cluster centers are placed at points 3 and 7:
	
		
			Current Location
			Closest Cluster Center
			Distance
		
	
	
		
			4
			3
			|4 - 3| = 1
		
		
			1
			3
			|1 - 3| = 2
		
		
			6
			7
			|6 - 7| = 1
		
		
			7
			7
			|7 - 7| = 0
		
		
			2
			3
			|2 - 3| = 1
		
	

 

The maximum distance is 2.

 

Function Description

Complete the function getMaximumDistance in the editor with the following parameters:

    int location[n]: the feature locations of all the data points

    int k: the number of clusters

 

Returns

    int: the maximum distance between any data point and its nearest cluster center after optimally placing the k clusters

 

Constraints

	
- 1 ≤ n ≤ 105

	
- 1 ≤ k ≤ n

	
- 1 ≤ location[i] ≤ 109

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, that denotes the number of data points.

Each line i of the n subsequent lines contains an integer describing location[i].

The next line contains an integer, k.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

STDIN           FUNCTION
-----           --------
5        →      location[] size n = 5
1        →      location = [1, 9, 3, 10, 14]
9
3
10
14
2        →      k = 2

```

Sample Output

3
```

Explanation

Let the cluster centers be placed at points 3 and 12.

	
		
			Current Location
			Closest Cluster Center
			Distance
		
	
	
		
			1
			3
			|1 - 3| = 2
		
		
			9
			12
			|9 - 12| = 3
		
		
			3
			3
			|3 - 3| = 0
		
		
			10
			12
			|10 - 12| = 2
		
		
			14
			12
			|14 - 12| = 2
		
	

 

Sample Case 1

Sample Input For Custom Testing

STDIN          FUNCTION
-----          --------
3        →     location[] size n = 3
5        →     location = [5, 3, 8]
3
8
3        →      k = 3

```

Sample Output

0
```

Explanation

Let the cluster centers be placed at points 3, 5, and 8.

	
		
			Current Location
			Closest Cluster Center
			Distance
		
	
	
		
			3
			3
			|3 - 3| = 0
		
		
			5
			5
			|5 - 5| = 0
		
		
			8
			8
			|8 - 8| = 0

## Sample Input/Output

## Preview

In a k-means clustering problem, determine the best possible clustering qualit
