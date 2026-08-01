# House Location

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.5838509316770186
- **Total Submissions:** 322
- **Solved Count:** 188
- **URL:** https://www.hackerrank.com/challenges/house-location

## Problem Statement

 Adam and Martha are planning to leave the city after their retirement and build a house in a huge land belonging to their family. To keep everyone happy, they want to build the house at a location having distance _a*d1_ from aunt Kimberly's house, where _a_ is some ratio and _d1_ is the distance of that location to uncle Bob's house. Also, the house should be at a distance _b*d2_ from uncle Jack's house where b is some ratio and _d2_ is the distance of the location to aunt Janet's house.

You need to help them find the location of their house.

**Input Format**  
The first line of input contains two integers _a_ and _b_ (the ratios above). In the next four lines, there are 4 pairs of integers that indicate the coordinates of Kimberly's, Bob's, Jack's, and Janet's houses, respectively.

**Output Format**  
You must output the coordinate of house with exactly two points after decimal point (rounded to closest one hundredth). If there is no location satisfying the above constraints, output **Impossible!** If there are more than one possible locations, output a location with minimum  x-coordinate and among the ones having the minimum x-coordinate, a location with minimum y-coordinate. 


**Constraints**  

1 < _a_, _b_ <= 1000

-1000 <= all input coordinates <= 1000


**Sample Input**  
<pre>
3 4

4 0

0 0

-2 -4

-2 -1
</pre>


**Sample Output**  
<pre>-2.00 0.00</pre>


**Explanation**  
As required, the point (-2.00, 0.00) has distance 2 from Bob's house and distance 3\*2=6 from Kimberly's house. It also has distance 1 from Janet's house and distance 4\*1=4 from Jack's house.

## Input Format

The first line of input contains two integers a and b (the ratios above). In the next four lines, there are 4 pairs of integers that indicate the coordinates of Kimberly's, Bob's, Jack's, and Janet's houses, respectively.

## Output Format

You must output the coordinate of house with exactly two points after decimal point (rounded to closest one hundredth). If there is no location satisfying the above constraints, output Impossible! If there are more than one possible locations, output a location with minimum  x-coordinate and among the ones having the minimum x-coordinate, a location with minimum y-coordinate.

## Constraints

1 < a, b <= 1000

-1000 <= all input coordinates <= 1000

## Sample Input

3 4

4 0

0 0

-2 -4

-2 -1

## Sample Output

-2.00 0.00

## Explanation

As required, the point (-2.00, 0.00) has distance 2 from Bob's house and distance 3*2=6 from Kimberly's house. It also has distance 1 from Janet's house and distance 4*1=4 from Jack's house.
