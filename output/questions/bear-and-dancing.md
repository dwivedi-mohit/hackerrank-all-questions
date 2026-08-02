# Bear and Dancing

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.8252427184466019
- **Total Submissions:** 103
- **Solved Count:** 85
- **URL:** https://www.hackerrank.com/challenges/bear-and-dancing

## Problem Statement

Bear Limak is a dance teacher.
Today is the first day of the course.
The course will take one or more days.
Your task will be to calculate the expected value of the number of dances in the course.

There are $n$ boys and $m$ girls.
A classroom is very small and thus only one pair can dance at each moment.
For each new dance Limak chooses uniformly at random one boy and one girl.
The chosen pair will dance, unless the following will happen.

It's possible that the chosen pair has already danced with each other on the same day.
Then, with probability $r$ they will now get upset about it and they will refuse to dance (but otherwise they dance like a normal pair).
In such a situation Limak will apologize them and there will be no more dances on that day.
Classes will start again on the next day though, and Limak won't care who danced the day before and who got angry.
So, the situation will be exactly as on the first day.

Limaks waits for the possibility to say _"Nice, kids. Every person has danced today. The course is over!"_.
So, the course ends immediately when there is a situation that every person has danced on that day.
What is the expected value of the number of dances in the course?

## Input Format

The only line of the input contains two integers $n$, $m$, and one real number $r$.

**Constraints**  

- $1 \le n \le 30$  
- $1 \le m \le 30$  
- $0.001 \le r \le 0.1$  
- $r$ is given with at most $6$ places after the decimal point.

## Output Format

Find and print the expected value of the number of dances in the course.
The answer will be considered correct if the absolute or relative error doesn't exceed $10^{-6}$.

**Sample Input 0**

    1 2 0.062812
    
**Sample Output 0**
    
    3.0000000000

**Sample Input 1**

    2 3 0.075
    
**Sample Output 1**
    
    5.8901549035


**Sample Input 2**

    2 2 0.05
    
**Sample Output 2**
    
    3.6885245902

## Constraints

-

-

-

-  is given with at most  places after the decimal point.

## Sample Input

1 2 0.062812

## Sample Output

3.0000000000

## Explanation

Sample 0

It may be surprising but any value of  would give the same answer.
With probability  there will be two dances only.
With probability  there will be three dances (the course will end in one day or two days but we don't care about it).
With probability  there will be four dances, and so on.
The expected value of the numbers of dances is exactly .

Sample 1

There are 2 boys and 3 girls.
There are 6 possible pairs and for each new dance each pair has probability  to be chosen.
Let's name boys  and .
Similarly, let's name girls , , .
One of possible scenarios is:

Day 0

-  and  are chosen (probability ). They dance together.

-  and  are chosen (prob. ). They dance.

-  and  are chosen (prob. ). They have already danced on that day. Unfortunately, they get upset about it (prob. ) and they don't dance now.

Day 1

- A new day starts.  and  are chosen (prob. ). They dance.

-  and  are chosen (prob. ). They dance. Note that it's not relevant what they did on the previous day.

-  and  are chosen (prob. ). They have already danced on that day but they don't get upset about it (prob. ). They dance.

-  and  are chosen (prob. ). They dance. Each person has danced on that day. The classes end.

There were 6 dances. The probability of the given scenario is

Technical note:

In this problem using a Run Code button will run your program only for the sample case 0. If you want to run others, run them as custom input.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
