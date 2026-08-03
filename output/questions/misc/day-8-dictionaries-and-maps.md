# Day 8: Dictionaries and Maps!

---

| Field | Value |
|---|---|
| **Slug** | `day-8-dictionaries-and-maps` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/day-8-dictionaries-and-maps |

---

## Problem Statement

Welcome to Day 8! Check out a [video review of dictionaries and hashmaps here](https://youtu.be/nbDhDMYxUEw), or just jump right into the problem. 

You are given a phone book that consists of your friend's names and their phone number. After that you will be given your friend's name as query. For each query, print the phone number of your friend.

## Input Format

The first line will have an integer $N$ denoting the number of entries in the phone book. Each entry consists of two lines: a name and the corresponding phone number. <br>

After these, there will be some queries. Each query will contain name of a friend.     Read the queries until end-of-file.

**Constraints**<br>
A name consists of only lower-case English letters and it may be in the format  
'first-name last-name' or in the format 'first-name'. Each phone number has exactly 8 digits without any leading zeros.<br>

$1 \le N \le 10^{4}$<br>
$1 \le queries \le 10^{4}$<br>

## Output Format

For each case, print *"Not found"* without quotes, if the friend has no entry in the phone book. Otherwise, print the friend's name and phone number. See sample output for the exact format.

To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.
