# Priyanka and Toys

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9282631854540202
- **Total Submissions:** 55383
- **Solved Count:** 51410
- **URL:** https://www.hackerrank.com/challenges/priyanka-and-toys

## Problem Statement


Priyanka works for an international toy company that ships by container.  Her task is to the determine the lowest cost way to combine her orders for shipping.  She has a list of item weights.  The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item.  All items meeting that requirement will be shipped in one container.

What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

For example, there are items with weights $w = [1,2,3,4,5,10,11,12,13]$.  This can be broken into two containers: $[1,2,3,4,5]$ and $[10,11,12,13]$.  Each container will contain items weighing within $4$ units of the minimum weight item.  

**Function Description**  

Complete the *toys* function in the editor below.  It should return the minimum number of containers required to ship.  

toys has the following parameter(s):  

- *w*: an array of integers that represent the weights of each order to ship  

## Input Format

The first line contains an integer $n$, the number of orders to ship.  
The next line contains $n$ space-separated integers, $w[1], w[2],\ldots, w[n]$,  representing the orders in a weight array.

## Output Format

Return the integer value of the number of containers Priyanka must contract to ship all of the toys. 



## Constraints

$1 \le n \le 10^5 $  
$0 \le w[i] \le 10^4, where\ i \in [1, n]$   

## Sample Input

1 2 3 21 7 12 14 21

## Explanation

The first container holds items weighing ,  and . (weights in range )

The second container holds the items weighing  units. ()

The third container holds the item weighing  units.  ()

The fourth container holds the items weighing  and  units. ()

 containers are required.
