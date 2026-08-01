# Detect HTML Tags, Attributes and Attribute Values

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9733477399603818
- **Total Submissions:** 61083
- **Solved Count:** 59455
- **URL:** https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values

## Problem Statement

You are given an *HTML* code snippet of $N$ lines.<br> Your task is to detect and print all the *HTML* tags, attributes and attribute values.

Print the detected items in the following format:

```
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
```

<br>

The `->` symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. <br>
The ` > ` symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

**Note:** Do not detect any *HTML* tag, attribute or attribute value inside the *HTML* comment tags (`<!-- Comments -->`). Comments can be multiline.<bR>
All attributes have an attribute value.

## Input Format

The first line contains an integer $N$, the number of lines in the *HTML* code snippet.<br>
The next $N$ lines contain *HTML* code.

__Constraints__

$0 < N < 100$

## Output Format

Print the *HTML* tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.<br>

Format your answers as explained in the problem statement.


## Sample Input

<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

## Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high

## Explanation

- head tag: Print the head tag only because it has no attribute.

- title tag: Print the title tag only because it has no attribute.

- object tag: Print the object tag. In the next  lines, print the attributes type, data, width and                     height along with their respective values.

- <!-- Comment  --> tag: Don't detect anything inside it.

- param tag: Print the param tag. In the next  lines, print the attributes name along with                     their respective values.
