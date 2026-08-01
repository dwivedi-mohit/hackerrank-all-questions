# Accessory Collection

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 60
- **Success Ratio:** 0.5745299910474485
- **Total Submissions:** 4468
- **Solved Count:** 2567
- **URL:** https://www.hackerrank.com/challenges/accessory-collection

## Problem Statement

[Victoria](http://dontnodentertainment.wikia.com/wiki/Victoria_Chase) is splurging on expensive accessories at her favorite stores. Each store stocks $A$ types of accessories, where the $i^{th}$ accessory costs $i$ dollars ($1 \le i \le A$). Assume that an item's type identifier is the same as its cost, and the store has an unlimited supply of each accessory.

Victoria wants to purchase a total of $L$ accessories according to the following rule:

> Any $N$-element subset of the purchased items must contain *at least* $D$ different types of accessories. 

For example, if $L = 6$, $N = 3$, and $D = 2$, then she must choose $6$ accessories such that *any* subset of $3$ of the $6$ accessories will contain *at least* $2$ distinct types of items. 

Given $L$, $A$, $N$, and $D$ values for $T$ shopping trips, find and print the maximum amount of money that Victoria can spend during each trip; if it's not possible for Victoria to make a purchase during a certain trip, print `SAD` instead. You must print your answer for each trip on a new line.

## Input Format

The first line contains an integer, $T$, denoting the number of shopping trips. 	 	
Each of the $T$ subsequent lines describes a single shopping trip as four space-separated integers corresponding to $L$, $A$, $N$, and $D$, respectively.

## Output Format

For each shopping trip, print a single line containing either the maximum amount of money Victoria can spend; if there is no collection of items satisfying her shopping rule for the trip's $L$, $A$, $N$, and $D$ values, print `SAD` instead.


## Constraints

- $1 \le T \le 10^6$  
- $1 \le D \le N \le L \le 10^5$  
- $1 \le A \le 10^9$  
- The sum of the $L$'s for all $T$ shopping trips $\le 8\cdot 10^6$.  

## Sample Input

6 5 3 2
2 1 2 2

## Sample Output

SAD

## Explanation

Shopping Trip 1:

We know that:

- Victoria wants to buy  accessories.

- The store stocks the following  types of accessories: .

- For any grouping of  of her  accessories, there must be at least  distinct types of accessories.

Victoria can satisfy her shopping rule and spend the maximum amount of money by purchasing the following set of accessories: . The total cost is , so we print  on a new line.

Shopping Trip 2:

We know that:

- Victoria wants to buy  accessories.

- The store stocks  type of accessory: .

- For any grouping of  of her  accessories, there must be at least  distinct types of accessories.

Because the store only carries  type of accessory, Victoria cannot make a purchase satisfying the constraint that there be at least  distinct types of accessories. Because Victoria will not purchase anything, we print that she is SAD on a new line.
