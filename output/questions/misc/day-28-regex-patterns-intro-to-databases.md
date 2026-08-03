# Day 28: RegEx, Patterns, and Intro to Databases!

---

| Field | Value |
|---|---|
| **Slug** | `day-28-regex-patterns-intro-to-databases` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/day-28-regex-patterns-intro-to-databases |

---

## Problem Statement

Welcome to Day 28! Check out an [Introduction to Databases](https://youtu.be/RmEjHzVRsOA), or jump into the challenge. We haven't discussed *RegEx* (Regular Expressions) yet, but that's okay! Review the [Pattern documentation](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html), learn what it can do, and apply your new knowledge to this challenge!

*RegEx* helps us easily search for or match a *Pattern* in text. Before searching for a *Pattern*, we must specify it using some well-defined syntax.

Given a string, determine if it's a valid *Pattern* or not. The string may contain spaces. 

**Note**: This is a  java only challenge, a *RegEx* is only valid if you can *compile* it using the  [Pattern.compile](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) method. You may find using a *try-catch* block helpful here.

## Input Format

The first line of input contains an integer, $T$ (the number of test cases). 	
The $T$ subsequent lines of test cases each contain a string of characters describing a *RegEx*.

**Constraints**		
$1 \leq T \leq 100$

## Output Format

On a new line for each test case, print **Valid** if the given *RegEx*'s syntax is correct; otherwise, print **Invalid**.
