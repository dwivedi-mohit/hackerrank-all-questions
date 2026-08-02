# Detect HTML Tags

- **Domain:** ai
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.933702385659681
- **Total Submissions:** 15174
- **Solved Count:** 14168
- **URL:** https://www.hackerrank.com/challenges/detect-html-tags

## Problem Statement

In this challenge, we're using regular expressions to detect the various *tags* used in an HTML document.

- Tags come in pairs. Some tag name, $\texttt{t}$, will have an opening tag, $\texttt{<t>}$, followed by some intermediate text, followed by a closing tag, $\texttt{</t>}$. The forward slash in a closing tag will always come *before* the tag name.
- The exception to this is *self-closing* tags, which consist of a *single tag* (not a pair) with a forward slash *after* the tag name:  $\texttt{<p/>}$

Here are a few examples of tags:

- The $\texttt{p}$ tag is for paragraphs: $\texttt{<p>This is a paragraph</p>}$  
- There may be $1$ or more spaces before or after a tag name: $\texttt{<  p >This is also a paragraph</p>}$  
- A *void* or *empty tag* involves an opening and closing tag with no intermediate characters: $\texttt{<p></p>}$
    
Some tags can also have *attributes*, such as the $\texttt{a}$ tag, which is used to add a hyperlink to another document: $\texttt{<a href="http://www.google.com">Google</a>}$	  
    
In the above case, $\texttt{a}$ is the tag name and $\texttt{href}$ is an attribute having the value $\texttt{http://www.google.com}$. 

**Task**		
Given $N$ lines of HTML, find the tag names (ignore any attributes) and print them as a single line of lexicographically ordered semicolon-separated values (e.g.: $\texttt{tag1;tag2;tag3}$).
  


## Input Format

The first line contains an integer, $N$, the number of HTML fragments. 		
Each of the $N$ subsequent lines contains a fragment of an HTML document.

## Output Format

Print a single line containing *all* of the unique tag names found in the input. Your output tags should be semicolon-separated and ordered lexicographically (i.e.: alphabetically). Do not print the same tag name more than once.

## Constraints

- $1 \le N \le 100$  
- Each fragment contains $\lt 10000$ ASCII characters.
- The fragments are chosen from [Wikipedia](http://www.wikipedia.com), so analyzing and observing their markup structure may help.
- Leading and trailing spaces/indentation have been trimmed from the HTML fragments.

## Sample Input

<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

## Sample Output

a;div;p

## Explanation

The first line contains  tag names: .

The second line contains  tag names: .

Our set of unique tag names is .

When we order these alphabetically and print them as semicolon-separated values, we get "".

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
