# XML2 - Find the Maximum Depth

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.960137179745814
- **Total Submissions:** 49570
- **Solved Count:** 47594
- **URL:** https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth

## Problem Statement

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as $0$.

**Input Format**

The first line contains $N$, the number of lines in the XML document. <br>
The next $N$ lines follow containing the XML document.

**Output Format**

Output a single line, the integer value of the maximum level of nesting in the XML document.

**Sample Input**  
```xml
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```
    
**Sample Output**  
```xml  
1
```  

**Explanation**

Here, the root is a *feed* tag, which has depth of $0$. <br>
The tags *title, subtitle, link* and *updated* all have a depth of $1$. <br>

Thus, the maximum depth is $1$.

## Input Format

The first line contains , the number of lines in the XML document.

The next  lines follow containing the XML document.

## Output Format

Output a single line, the integer value of the maximum level of nesting in the XML document.

## Sample Input

<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

## Explanation

Here, the root is a feed tag, which has depth of .

The tags title, subtitle, link and updated all have a depth of .

Thus, the maximum depth is .

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
