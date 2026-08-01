# Circle City

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.6556822982678496
- **Total Submissions:** 4734
- **Solved Count:** 3104
- **URL:** https://www.hackerrank.com/challenges/circle-city

## Problem Statement

Roy lives in a city that is circular in shape on a $2D$ plane that has radius $r$. The city center is located at origin $(0,0)$ and it has suburbs lying on the lattice points (points with integer coordinates). The city Police Department Headquarters can only protect those suburbs which are located strictly inside the city. The suburbs located on the border of the city are still unprotected. So the police department decides to build at most $k$ additional police stations at some suburbs. Each of these police stations can protect the suburb it is located in.

Given the *square of radius*, $d (=r^2)$, of the city, Roy has to determine if it is possible to protect all the suburbs.

**Input Format**  
The first line of input contains integer $t$; $t$ test cases follow.  
Each of the next $t$ lines contains two space-separated integers: $d$, *the square of the radius* of the city, and $k$, the maximum number of police stations the headquarters is willing to build.

**Constraints**  
$ 1 \le t \le 10^{3} $  
$ 1 \le d \le 2 \times 10^{9} $  
$ 0 \le k \le 2\times10^{9} $  

**Output Format**  
For each test case, print in a new line `possible` if it is possible to protect all the suburbs;, otherwise, print `impossible`.

**Sample Input**

    5
    1 3
    1 4
    4 4
    25 11
    25 12

**Sample Output**

    impossible
    possible
    possible
    impossible
    possible

**Explanation**  

- For $d = 1$, there are $4$ points on circumference - _[(0,1), (0,-1), (1,0), (-1,0)]_.
- For $d = 4$, there are $4$ points on circumference - _[(0,2), (0,-2), (2,0),(-2,0)]_.
- For $d = 25$, there are $12$ points on circumference - _[(0,5), (0,-5), (3,4), (-3,4), (3,-4), (-3,-4), (4,3), (-4,3), (4,-3), (-4,-3), (5,0), (-5,0)]_.

*Test Case #01:* There are $4$ suburbs on the border, while we are allowed to construct max $k = 3$ police stations.  
*Test Case #02:* We can cover all the $4$ suburbs as exactly $4$ stations are allowed.  
*Test Case #03:* We can cover all the $4$ suburbs as exactly $4$ stations are allowed.  
*Test Case #04:* It is impossible to cover $12$ suburbs, on the border, with $11$ police stations.  
*Test Case #05:* We can to cover all $12$ suburbs, on the border, with $12$ police stations.  

**Timelimits**  

Timelimits for this challenge are given [here](https://hr-assets.s3.amazonaws.com/7bb46cae_challenge_assets/checker_limits/3926/limits.json)

## Input Format

The first line of input contains integer ;  test cases follow.

Each of the next  lines contains two space-separated integers: , the square of the radius of the city, and , the maximum number of police stations the headquarters is willing to build.

## Output Format

For each test case, print in a new line possible if it is possible to protect all the suburbs;, otherwise, print impossible.

## Sample Input

1 3
1 4
4 4
25 11
25 12

## Sample Output

impossible
possible
possible
impossible
possible

## Explanation

- For , there are  points on circumference - [(0,1), (0,-1), (1,0), (-1,0)].

- For , there are  points on circumference - [(0,2), (0,-2), (2,0),(-2,0)].

- For , there are  points on circumference - [(0,5), (0,-5), (3,4), (-3,4), (3,-4), (-3,-4), (4,3), (-4,3), (4,-3), (-4,-3), (5,0), (-5,0)].

Test Case #01: There are  suburbs on the border, while we are allowed to construct max  police stations.

Test Case #02: We can cover all the  suburbs as exactly  stations are allowed.

Test Case #03: We can cover all the  suburbs as exactly  stations are allowed.

Test Case #04: It is impossible to cover  suburbs, on the border, with  police stations.

Test Case #05: We can to cover all  suburbs, on the border, with  police stations.

Timelimits

Timelimits for this challenge are given here
