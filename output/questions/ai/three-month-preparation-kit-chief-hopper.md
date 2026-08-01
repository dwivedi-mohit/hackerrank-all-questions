# Chief Hopper

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.9361702127659575
- **Total Submissions:** 2115
- **Solved Count:** 1980
- **URL:** https://www.hackerrank.com/challenges/three-month-preparation-kit-chief-hopper

## Problem Statement

Chief's bot is playing an old DOS based game.  There is a row of buildings of different heights arranged at each index along a number line.  The bot starts at building $0$ and at a height of $0$.  You must determine the minimum energy his bot needs at the start so that he can jump to the top of each building without his energy going below zero.  

Units of height relate directly to units of energy.  The bot's energy level is calculated as follows:  

- If the bot's $botEnergy$ is less than the height of the building, his $newEnergy = botEnergy - (height - botEnergy)$  
- If the bot's $botEnergy$ is greater than the height of the building, his $newEnergy = botEnergy + (botEnergy - height)$  

**Example**  

$arr = [2,3,4,3,2]$   

Starting with $botEnergy = 4$, we get the following table:

<pre>
	botEnergy	height	delta
    4				2		+2
    6				3		+3
    9				4		+5
    14				3		+11
    25				2		+23
    48
</pre>

That allows the bot to complete the course, but may not be the minimum starting value.  The minimum starting $botEnergy$ in this case is $3$.  

**Function Description**  

Complete the *chiefHopper* function in the editor below.  

chiefHopper has the following parameter(s):  

- *int arr[n]:* building heights   

**Returns**  

- *int:* the minimum starting $botEnergy$    



## Input Format

The first line contains an integer $n$, the number of buildings. 

The next line contains $n$ space-separated integers $arr[1]..arr[n]$, the heights of the buildings.  

## Output Format

  

## Constraints

+ $1 \le n \le 10^5$  
+ $1 \le arr[i] \le 10^5$ where $1 \le i \le n$  

## Sample Input

3 4 3 2 4

sample Output

4

## Explanation

Sample 1

If initial energy is 4, after step 1 energy is 5, after step 2 it's 6, after step 3 it's 9 and after step 4 it's 16, finally at step 5 it's 28.

You can verify for lower initial energy bot will have -ve energy in the end.

Sample 2

In the second test case if bot has energy 4, it's energy is changed by (4 - 4 = 0) at every step and remains 4.
