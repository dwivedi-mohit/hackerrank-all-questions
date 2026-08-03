# Day 12: Inheritance!

---

| Field | Value |
|---|---|
| **Slug** | `day-12-inheritance` |
| **Contest** | 30-days-of-code |
| **Difficulty** | Easy |
| **Score** | 75 |
| **URL** | https://www.hackerrank.com/challenges/day-12-inheritance |

---

## Problem Statement

Welcome to Day 12! Check out [this video](https://youtu.be/wlA66hZ4Z74) reviewing inheritance, or just jump right into the problem.

You are given two classes, *Student* and *Grade*, where *Student* is the base class and *Grade* is the derived class. Completed code for *Student* and stub code for *Grade* are provided for you in the editor. Note that *Grade* inherits all the properties of *Student*.

Complete the *Grade* class by writing a class constructor (`Grade(String,String,int,int)`) and a `char calculate()` method. The *calculate* method should return the *character* representative of a Student's *Grade. *Score* as defined in this chart:
<img src="https://s3.amazonaws.com/hr-challenge-images/15842/1452223182-c26672abcc-ScreenShot2016-01-08at8.49.10AM.png" title="Screen Shot 2016-01-08 at 8.49.10 AM.png" />

## Input Format

Input is already handled for you by the code pre-filled in the editor. There are $4$ lines of input containing $first \ name$, $last \ name$, $phone$, and $score$, respectively.

**Constraints**   
$ 4 \le |first$ $name|, |last$ $name| \le 10$    
*phone* contains exactly $7$ digits  
$1 \le score \le 100$

## Output Format

Output is already handled for you by the code pre-filled in the editor. Your output will be correct if your *Grade* class constructor and *calculate* method are properly written.
