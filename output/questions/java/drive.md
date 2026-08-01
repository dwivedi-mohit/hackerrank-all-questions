# Drive

- **Domain:** java
- **Difficulty:** Expert
- **Max Score:** 90
- **Success Ratio:** 0.7816666666666666
- **Total Submissions:** 1800
- **Solved Count:** 1407
- **URL:** https://www.hackerrank.com/challenges/drive

## Problem Statement

HackerRank is starting a bus service in [MountainView, California](https://maps.google.com/maps?q=152+E+Dana+St,+Mountain+View,+CA&hl=en&ll=37.386646,-122.06583&spn=0.005336,0.009645&sll=37.387156,-122.066474&layer=c&cbp=13,353.31,,0,12.73&cbll=37.387138,-122.066472&hnear=152+E+Dana+St,+Mountain+View,+California+94041&t=m&z=17&iwloc=A&panoid=JqZF-MbOw32l_4cdg7gnXA). The bus starts at time T = 0 at *station<sub>1</sub>* and goes through *station<sub>2</sub>*, *station<sub>3</sub>*, *station<sub>4</sub>* in that order and reaches the headquarters located at *station<sub>n</sub>*. At every station, the bus waits for various commuters to arrive before it departs to the next station. Ignoring the acceleration, the bus moves at 1 meter / second. i.e., if *station<sub>i</sub>* and *station<sub>j</sub>* are 1000 meters apart, the bus takes 1000 seconds to travel from *station<sub>i</sub>* to *station<sub>j</sub>*. 

The bus is equipped with **K** units of Nitro (N<sub>2</sub>O). If going from *station<sub>i</sub>* to *station<sub>j</sub>* takes *x* seconds, then using *t* units of nitro can decrease the time taken to max(x-t, 0) seconds where max(a,b) denotes the greater of the two values between a & b. The Nitro can be used all at once or in multiples of 1 unit. 

If the bus driver travels optimally, what is the minimum sum of travelling time for all commuters? The travelling time equals to the time he/she arrived at the destination minus the time he/she arrived the start station. 

Please remember that the driver must take all passengers to their destination.  


## Input Format

The first line contains 3 space separated integers n, m and K which indicate the number of stations, total number of people who board the bus at various stations and the total units of Nitro (N<sub>2</sub>O) present in the bus.  

The second line contains n-1 space separated integers where the i<sup>th</sup> integer indicates the distance between *station<sub>(i-1)</sub>* to *station<sub>i</sub>*.  

m lines follow each containing 3 space separated integers. The i<sup>th</sup> line contains t<sub>i</sub>, s<sub>i</sub> and e<sub>i</sub> in that order indicating the arrival time of the commuter at s<sub>i</sub> at time t<sub>i</sub> with his destination being e<sub>i</sub>. 


    n m K  
    d1 d2 ... dn-1   // di: the distance between station_i to station_(i+1).
    t1 s1 e1         // commuter 1 arrives at his boarding point at s1 and his destination is e1
    t2 s2 e2
    ...
    tm sm em


## Output Format

The minimal total travel time. 


## Constraints

0 < n <= 100000  
0 < m <= 100000  
0 <= K <= 10000000  
0 < d<sub>i</sub> <= 100  
0 <= t<sub>i</sub> <= 10000000  
1 <= s<sub>i</sub> < e<sub>i</sub> <= n  


## Sample Input

3 3 2
1 4
1 1 3
2 1 2
5 2 3

## Explanation

The bus waits for the 1st and the 2nd commuter to arrive at station1 and travels to station2 carrying 2 passengers. The travel time from station1 to station2 is 1 second. It then waits for the 3rd commuter to board the bus at time = 5, 2nd commuter deboards the bus. The 3rd commuter boards the bus at t = 5. The bus now uses 2 units of nitro, this reduces the commute time to travel to station3 from 4 to 2.

Hence, the total time spent by each of the passengers on the bus is

- 1 (time spent waiting for commuter 2) + 1 (travel time from station1 to station2) + 2 (time spent waiting for commuter 3) + 2 (travel time from station2 to station3) = 6

- 1 (travel time from station1 to station2)

- 2 (travel time from station2 to station3)

6+1+2 = 9

hence the answer.

Timelimits

Timelimits for this challenge can be seen here
