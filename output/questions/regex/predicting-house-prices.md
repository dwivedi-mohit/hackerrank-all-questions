# Day 6: Multiple Linear Regression: Predicting House Prices

- **Domain:** regex
- **Difficulty:** Expert
- **Max Score:** 10
- **Success Ratio:** 0.8698538238824942
- **Total Submissions:** 14161
- **Solved Count:** 12318
- **URL:** https://www.hackerrank.com/challenges/predicting-house-prices

## Problem Statement

**Objective** <br>
In this challenge, we practice using multiple linear regression to predict housing prices. Check out the [Resources](/contests/intro-to-statistics/challenges/predicting-house-prices/resources) tab for helpful videos!

**Task**  

Charlie is looking to buy a house and has collected data on desirable features in the area. For each house, he recorded feature values on a scale from $0$ to $1$, along with the price per square foot for some houses. However, some of the houses lack pricing data. You need to estimate the price per square foot for these houses based on the available feature data and the pricing information for the other houses.

The data is structured such that:  

- There are $F$ features for each house.  
- Each row contains $F$ feature values followed by the price per square foot (totaling $F+1$ columns).  
- Charlie has observed data for $N$ houses, resulting in a table with $N$ rows and $(F+1)$ columns.  

The price per square foot is approximately linearly related to the features. Your task is to predict the missing prices using a regression-based technique.

**Hints**  
- Focus on using regression to model the relationship between the features and the price per square foot.
- You don't need to address bias-variance trade-offs at this stage.

## Input Format

The first line contains $2$ space-separated integers, $F$ (the number of observed features) and $N$ (the number of rows/houses for which Charlie has noted *both* the features and price per square foot).  
The $N$ subsequent lines each contain $F+1$ space-separated floating-point numbers describing a row in the table; the first $F$ elements are the noted features for a house, and the very last element is its price per square foot.	

The next line (following the table) contains a single integer, $T$, denoting the number of houses for for which Charlie noted features but *does not* know the price per square foot.		
The $T$ subsequent lines each contain $F$ space-separated floating-point numbers describing the features of a house for which pricing is not known.

## Output Format

Print $T$ lines, where each line $i$ contains the predicted price for the $i^{th}$ house (from the second table of houses with unknown prices per square foot).  

## Constraints

- $1 \le F \le 10$  
- $5 \le N \le 100$ 
- $1 \le T \le 100$  
- $0 \le \text{ Price Per Square Foot }\le 10^6$  
- $0 \le \text{ Factor Values } \le 1$  

**Scoring**  

For each test case, we will compute the following:

- $d = \text{Normalized Distance from Expected answer} = \frac{abs( Computed-Expected)}{Expected  }$

There are multiple ways to approach this problem that account for bias, variance, various subjective factors, and "noise". We take a realistic approach to scoring and permit up to a $\pm 10\%$ swing of our expected answer.   

- $d_{adjusted} = max(d - 0.1, 0)$  
- $\text{Score for each test case} \equiv \textit{max(}1-d_{adjusted},0)$
- $\text{Score for the test case} \equiv \text{(Average score for all the tests it contains)} \times M$, where $M$ is the maximum possible score for the test case.    

Consider a test case in which we only need to find the pricing for $1$ house. Suppose our expected answer is $10$, and your answer is $9.5$:  

$d = \frac{(10 - 9.5)}{10} = 0.05$  
$d_{adjusted} = max(0.05 - 0.1,0) = 0$ 

The score for a test case with $10$ points $= max(1,0) \times 10
= 10$

## Sample Input

STDIN                  Function
-----                  --------
2 7                     F = 2, N = 7
0.18 0.89 109.85    Features = [0.18, 0.89] Square foot cost = 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4                       T = 4
0.49 0.18             Features for the first property
0.57 0.8
0.56 0.64
0.76 0.18

## Sample Output

105.22
142.68
132.94
129.71
