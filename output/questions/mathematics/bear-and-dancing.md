# Bear and Dancing

---

| Field | Value |
|---|---|
| **Slug** | `bear-and-dancing` |
| **Domain** | mathematics |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/bear-and-dancing |

---

## Preview

n boys, m girls, the expected value of the number of dances.

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

## Sample Tests

### Test 1

```
1 2 0.062812
```

### Test 2

```
3.0000000000
```

### Test 3

```
2 3 0.075
```

### Test 4

```
5.8901549035
```

### Test 5

```
2 2 0.05
```

### Test 6

```
3.6885245902
```
