# The Captain's Room 

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9194613384486592
- **Total Submissions:** 180373
- **Solved Count:** 165846
- **URL:** https://www.hackerrank.com/challenges/py-the-captains-room

## Problem Statement

Mr. Anant Asankhya is the manager at the *INFINITE* hotel. The hotel has an infinite amount of rooms. 

One fine day, a *finite* number of tourists come to stay at the hotel. <br>
The tourists consist of:<br>
&#8594; A Captain.<br>
&#8594; An unknown group of families consisting of $K$ members per group where $K$ &#x2260; $1$.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear $K$ times per group except for the Captain's room. 

Mr. Anant needs you to help him find the Captain's room number.
<br>*The total number of tourists or the total number of groups of families is not known to you.*
<br>*You only know the value of $K$ and the room number list.*

## Input Format

The first line consists of an integer, $K$, the size of each group.<br>
The second line contains the unordered elements of the room number list.<br>
<br>

__Constraints__

$1 < K < 1000 $

## Output Format

Output the Captain's room number.

## Sample Input

1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

## Explanation

The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .

 Hence,  is the Captain's room number.
