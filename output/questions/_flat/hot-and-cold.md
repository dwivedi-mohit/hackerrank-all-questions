# Hot and Cold

---

| Field | Value |
|---|---|
| **Slug** | `hot-and-cold` |
| **Contest** | hourrank-20 |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/hot-and-cold |

---

## Problem Statement

Carl, Caroline, Helen, and Han are four friends sharing a one-room workspace. The workspace has a single thermostat which they can set to any integer temperature between $35$ degrees to $95$ degrees Fahrenheit, inclusive. 

The four friends can't agree on the room's temperature! Carl and Caroline don't want it to be too cold, while Helen and Han don't want it to be too hot. Specifically:

- Carl wants it to be *at least* $c_1$ degrees Fahrenheit.  
- Caroline wants it to be *at least* $c_2$ degrees Fahrenheit.  
- Helen wants it to be *at most* $h_1$ degrees Fahrenheit.  
- Han wants it to be *at most* $h_2$ degrees Fahrenheit.  

Given $c_1$, $c_2$, $h_1$, and $h_2$, is there a satisfactory temperature that all four friends will be happy with? If it's possible, print `YES`; otherwise, print `NO`.

## Input Format

Four space-separated integers describing the respective values of $c_1$, $c_2$, $h_1$, and $h_2$.

## Output Format

Print `YES` if it's possible to satisfy all four friends' conditions; otherwise, print `NO` instead.

## Constraints

- $35 \le c_1, c_2, h_1, h_2 \le 95$
