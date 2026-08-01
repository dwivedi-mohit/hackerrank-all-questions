# Beautiful Binary String

- **Domain:** regex
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9507333544370581
- **Total Submissions:** 94770
- **Solved Count:** 90101
- **URL:** https://www.hackerrank.com/challenges/beautiful-binary-string

## Problem Statement

Alice has a [binary string](https://www.ics.uci.edu/~alspaugh/cls/shr/binaryString.html). She thinks a binary string is beautiful if and only if it doesn't contain the [substring](https://en.wikipedia.org/wiki/Substring) $\texttt{"010"}$. 

In one step, Alice can change a $0$ to a $1$ or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

**Example**    

$b=\text{010}$    

She can change any one element and have a beautiful string.

**Function Description**  

Complete the *beautifulBinaryString* function in the editor below.   

beautifulBinaryString has the following parameter(s):  

- *string b*: a string of binary digits   

**Returns**   

- *int:* the minimum moves required

## Input Format

The first line contains an integer $n$, the length of binary string. 	
The second line contains a single binary string $b$.

## Output Format

Print the minimum number of steps needed to make the string beautiful.

**Sample Input 0**

	STDIN		Function
    -----		--------
    7			length of string n = 7
    0101010		b = '0101010'
    
**Sample Output 0**

    2  
    
**Explanation 0:** 

In this sample, $b= \text{"0101010"}$

The figure below shows a way to get rid of each instance of $\text{"010"}$:

<img src="https://s3.amazonaws.com/hr-challenge-images/20389/1462078460-7a0995ab28-binary.png" title="binary.png" />

Make the string beautiful by changing $2$ characters ($b[2]$ and $b[5]$).
    
**Sample Input 1**

	5
    01100
    
**Sample Output 1**

    0
    
**Sample Case 1:**

In this sample $b = \text{"01100"}$		

**Explanation 1**

The substring $\text{"010"}$ does not occur in $b$, so the string is already beautiful in $0$ moves.

**Sample Input 2**

	10
    0100101010
    
**Sample Output 2**

    3
    
**Explanation 2**  

In this sample $b = \text{"0100101010"}$

One solution is to change the values of $b[2], b[5] \text{ and }b[9]$ to form a beautiful string.


## Constraints

* $1 \le n \le 100$
* $b[i] \in \{0, 1\}$.



## Sample Input

STDIN       Function
-----       --------
7           length of string n = 7
0101010     b = '0101010'

## Sample Output

2

## Explanation

In this sample,

The figure below shows a way to get rid of each instance of :

Make the string beautiful by changing  characters ( and ).
