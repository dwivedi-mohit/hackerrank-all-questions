# HTML Parser - Part 2

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9766964702742377
- **Total Submissions:** 59948
- **Solved Count:** 58551
- **URL:** https://www.hackerrank.com/challenges/html-parser-part-2

## Problem Statement


<sup>`*`This section assumes that you understand the basics discussed in __HTML Parser - Part 1__</sup>


[*.handle\_comment(data)*](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_comment)  
This method is called when a comment is encountered (e.g. &lt;!--comment-->).  
The *data* argument is the content inside the comment tag:

	from html.parser import HTMLParserr

	class MyHTMLParser(HTMLParser):
    	def handle_comment(self, data):
    	  	  print("Comment  :", data)
<br>

[*.handle\_data(data)*](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser.handle_data)  
This method is called to process arbitrary data (e.g. text nodes and the content of &lt;script>...&lt;/script> and &lt;style>...&lt;/style>).  
The *data* argument is the text content of HTML.

	from html.parser import HTMLParserr

	class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
        	print("Data     :", data)
            
---
__Task__

You are given an *HTML* code snippet of $N$ lines.  
Your task is to print the *single-line comments, multi-line comments* and the *data*. 

Print the result in the following format:

	>>> Single-line Comment  
    Comment
    >>> Data                 
    My Data
    >>> Multi-line Comment  
    Comment_multiline[0]
    Comment_multiline[1]
    >>> Data
    My Data
    >>> Single-line Comment:  
    
    
**Note**: Do not print *data* if `data == '\n'`.  

## Input Format

The first line contains integer $N$, the number of lines in the *HTML* code snippet.  
The next $N$ lines contain *HTML* code.

__Constraints__

$0 < N < 100$

## Output Format

 Print the *single-line comments, multi-line comments* and the *data* in order of their occurrence from top to bottom in the snippet.<br>

Format the answers as explained in the problem statement.


## Sample Input

<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

## Sample Output

>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
