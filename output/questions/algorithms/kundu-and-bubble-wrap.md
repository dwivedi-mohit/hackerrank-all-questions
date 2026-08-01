# Kundu And Bubble Wrap

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.9255079006772009
- **Total Submissions:** 886
- **Solved Count:** 820
- **URL:** https://www.hackerrank.com/challenges/kundu-and-bubble-wrap

## Problem Statement

Kundu has a Bubble Wrap and like all of us she likes popping it. The Bubble wrap has dimensions _NxM_, i.e. it has _N_ rows and each row has _M_ cells which has a bubble. Initially all bubbles in filled with air and can be popped.  
<br>
What Kundu does is randomly picks one cell and tries to pop it, there might be a case that the bubble Kundu selected is already popped. In that case he has to ignore this. Both of these steps take 1 second of time. Tell the total [expected number](http://en.wikipedia.org/wiki/Expected_value) of seconds in which Kundu would be able to pop them all.   

**Input:**   
Input contains a single line containing two space seperated integers, _N M_, representing the dimension of Bubble wrap.

**Output:**   
Output the required answer in one line. The answer will be considered correct, if its absolute  error doesn't exceed 10<sup>-2</sup>.   

**Constraints:**   
1 &le; _N, M_ &le; 1000      

**Sample Input #00**

    1 1

**Sample Output #00**

	1
    
**Sample Input #01**

	1 2
    
**Sample Output #01**

	3
    
**Sample Input #02**

	2 2

**Sample Output #02**

	8.3333333333

**Explanation**   
*Test Case #00:* There is only one bubble, so he needs only one chance to pop it.  
*Test Case #01:* Expected number of steps of popping two bubbles is 3.  
*Test Case #02:* There are 4 bubbles with equal probability of popping out. Expected number of steps to pop all of them is 8.333333...

---

**Tested by:** [Lalit Kundu](/darkshadows)

## Constraints

1 ≤ N, M ≤ 1000

Sample Input #00

1 1

Sample Output #00

1

Sample Input #01

1 2

Sample Output #01

3

Sample Input #02

2 2

Sample Output #02

8.3333333333

## Explanation

Test Case #00: There is only one bubble, so he needs only one chance to pop it.

Test Case #01: Expected number of steps of popping two bubbles is 3.

Test Case #02: There are 4 bubbles with equal probability of popping out. Expected number of steps to pop all of them is 8.333333...

Tested by: Lalit Kundu
