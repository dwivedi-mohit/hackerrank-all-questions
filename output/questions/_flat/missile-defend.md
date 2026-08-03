# HackerX

---

| Field | Value |
|---|---|
| **Slug** | `missile-defend` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/missile-defend |

---

## Preview

Find the minimum number of hackerX missiles you must launch to keep Nation B safe.

## Problem Statement

**Update:** A slight modification in the problem statement (see below)


Evil Nation A is angry and plans to launch **N** guided-missiles at the peaceful Nation B in an attempt to wipe out all of Nation B's people. Nation A's missile _i_ will arrive in nation B at time t<sub>i</sub>. Missile _i_ communicates with its headquarters by unique radio signals with a frequency equal to f<sub>i</sub>. Can you help the peaceful Nation B survive by building a defensive system that will stop the missiles dead in the sky?

**Defensive system:**


The only way to defend Nation B from the attacking missile is by counter attacking them with a _hackerX_ missile. You have a lot of _hackerX_ missiles and each one of them has its own radio frequency. An individual _hackerX_ missile can destroy Evil Nation A’s attacking missile if the radio frequency of both of the missiles match. Each _hackerX_ missile can be used an indefinite number of times. Its invincible and doesn't get destroyed in the collision.

The good news is you can adjust the frequency of the _hackerX_ missile to match the evil missiles' frequency. When changing the _hackerX_ missile's initial frequency fA to the new defending frequency fB, you will need \|fB - fA\| units of time to do. 

<strike>Each _hackerX_ missile can only destroy one of Nation A's missile at a time. So if two evil missiles with same frequency arrive at the same time, you need at least two _hackerX_ missiles with the same frequency as the evil missiles to avoid damage.</strike> 

If two evil missles with same frequency arrive at the same time, we can destroy them both with one _hackerX_ missile. You can set the frequency of a _hackerX_ missile to any value when its fired.


What is the minimum number of _hackerX_ missiles you must launch to keep Nation B safe?


**Input Format:**

The first line contains a single integer **N** denoting the number of missiles. 

This is followed by **N** lines each containing two integers t<sub>i</sub> and f<sub>i</sub> denoting the time & frequency of the i<sup>th</sup> missile.

**Output Format:**

A single integer denoting the minimum number of _hackerX_ missiles you need to defend the nation.

**Constraints:**

1 <=  N  <= 100000

0 <= t<sub>i</sub> <= 100000

0 <= f<sub>i</sub> <= 100000

t<sub>1</sub> <= t<sub>2</sub> <= ... <= t<sub>N</sub>


**Sample Input #00**


    4
    1 1
    2 2
    3 1
    5 1

**Sample Output #00**


    1

**Explanation #00**

A _HackerX_ missile is launched at t = 1 with a frequency f = 1, and destroys the first missile. It re-tunes its frequency to f = 2 in 1 unit of time, and destroys the missile that is going to hit Nation B at t = 2. It re-tunes its frequency back to 1 in 1 unit of time and destroys the missile that is going to hit the nation at t = 3. It is relaunched at t = 5 with f = 1 and destroys the missile that is going to hit nation B at t = 5. Hence, you need only 1 _HackerX_ to protect nation B. 

**Sample Input #01**

 
    4
    1 1
    2 3
    3 1
    5 1
 
**Sample Output #01**

 
    2
 
**Explanation #01**
 
Destroy 1 missile at t = 1, f = 1. now at t = 2, there is a missile with frequency 3. The launched missile takes 2 units of time to destroy this, hence we need a new hackerX missile to destroy this one. The first hackerX missile can destroy the 3rd missile which has the same frequency as itself. The same hackerX missile destroys the missile that is hitting its city at t = 5. Thus, we need atleast 2 hackerX missiles.

## Sample Tests

### Test 1

```
4
1 1
2 2
3 1
5 1
```

### Test 2

```
1
```

### Test 3

```
4
1 1
2 3
3 1
5 1
```

### Test 4

```
2
```
