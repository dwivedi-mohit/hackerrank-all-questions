# Hanging Posters

---

| Field | Value |
|---|---|
| **Slug** | `hanging-posters` |
| **Contest** | hourrank-31 |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/hanging-posters |

---

## Problem Statement

Arthur needs to hang $n$ posters on his wall. Standing on the ground he can reach upto a height of $h$. Each poster is to be bolted at a certain height above the ground level, described by the array $wallPoints$. Each poster also has some length, defined by the array $lengths$.<br> 
<br>
To hang a poster properly, Arthur needs to hold atleast 50&percnt; of the length of the poster and poster is to be bolted at a point which is 25&percnt; from its top. <br>
<br>
![image](https://s3.amazonaws.com/hr-assets/0/1541923309-2123b246c6-HangingPostersdiagram.jpg)
<br>
Arthur wants to know what is the minimum height of the ladder he should buy, in order to hang all the wall posters. The ladder is only available in integral heights. Arthur can reach any height upto the maximum possible height.<br>
<br>

## Input Format

The first line of the input contains two space separated integers, $n$ and $h$.<br>
The next line contains $n$ space separated integers, denoting the elements of the array $wallPoints$.<br>
The last line contains $n$ space separated integers, denoting the elements of the array $lengths$.

## Output Format

Output an integer, the minimum height of the ladder required. If no ladder is required, output 0

## Constraints

1 &le; $h$ &lt; 10<sup>9</sup><br>
1 &le; $n$ &le; 10<sup>5</sup><br>
1 &le; $wallPoints$<sub>i</sub> &le; 10<sup>9</sup> (0 &le; i &lt; $n$)<br>
1 &le; $lengths$<sub>i</sub> &le; 10<sup>5</sup> (0 &le; i &lt; $n$)<br>
