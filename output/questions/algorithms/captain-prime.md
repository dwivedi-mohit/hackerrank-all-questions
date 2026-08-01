# Captain Prime

- **Domain:** algorithms
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9297520661157025
- **Total Submissions:** 968
- **Solved Count:** 900
- **URL:** https://www.hackerrank.com/challenges/captain-prime

## Problem Statement

Captain Prime is going on a trip to Primeland and needs support of his troops to make this voyage successful. To prevent the wrath of evil spirits, he has to throw out some people from his troop into the sea. This decision will depend on the identification number of the troop member.  
<br>
His ship is divided into three parts: *Left, right, and central.* Every person on the ship is assigned an identification number (referred as _id_), and according to their _id_  they get to work in one part of the ship, or end up getting thrown out of the ship.  
<br>


A person's fate depends on the following conditions:   

-  *CENTRAL:* He will be working in central part if (a) his _id_ is a prime number, (b) it doesn't contain 0 as one of the digits, and (c) when the _left_ digits are successively taken off, then all the resulting numbers are also prime. (d) And same goes for the digits on the _right_ side. For example person with _id_ 3137 will work in central part, as 3137, {313, 31, 3}, {137, 37, and 7} are all prime numbers.

- *LEFT:* He will be working in left part if (a) his _id_ is a prime number, (b) and doesn't contain 0 as one of the digits. (c) Also when the _left_ digits are successively taken off, then all the resulting numbers are prime, but this doesn't hold true for the _right_ digits. For example, person with _id_ 1367 will work here, since 1367, 367, 67 and 7 are all prime numbers. While 136 is not a prime number, which we get after removing one digit on the right.

- *RIGHT:* He will be working on right part if (a) his _id_ is a prime number, (b) and doesn't contain 0 digit as one of the digits. (c) Also on successively stripping _right_ digits, all the resulting numbers are prime, but this does not hold true for the _left_ digits. For example, person with _id_ 2333 belongs to this category, as 2333, 233, 23 and 2 are all prime numbers, while 333 is not a prime number.

- *DEAD:* If a person is *not* eligible to work anywhere on the ship, then he will be thrown out of the ship. Sad!

**Input Format:**    
The first line contains *T*, the number of persons on the ship, followed by the their _id_ numbers in the next _T_ lines.  

**Output Format:**    
Print `LEFT`, `RIGHT`, `CENTRAL`, or `DEAD` according to the fate of the person on the ship.    

**Constraints:**    
$1 \le T \le 50$    
$1 \le id \le 10^6$    

**Sample Input #00**  

	5
	3137
	1367
	2333
	101
	12
	
**Sample Output #00**

    CENTRAL
	LEFT
    RIGHT
    DEAD
    DEAD


**Sample input #01**  

    4
    43
    23
    66
    29
    
**Sample Output #01**  

    LEFT
    CENTRAL
    DEAD
    RIGHT

---
**Tested by** [Abhiranjan](https://www.hackerrank.com/abhiranjan)  


## Input Format

The first line contains T, the number of persons on the ship, followed by the their id numbers in the next T lines.

## Output Format

Print LEFT, RIGHT, CENTRAL, or DEAD according to the fate of the person on the ship.

## Constraints

Sample Input #00

5
3137
1367
2333
101
12

Sample Output #00

CENTRAL
LEFT
RIGHT
DEAD
DEAD

Sample input #01

4
43
23
66
29

Sample Output #01

LEFT
CENTRAL
DEAD
RIGHT

Tested by Abhiranjan
