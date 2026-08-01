# Ruby - Strings - Encoding

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9786760615612832
- **Total Submissions:** 10786
- **Solved Count:** 10556
- **URL:** https://www.hackerrank.com/challenges/ruby-strings-encoding

## Problem Statement

In Ruby, strings are objects of the *[String](http://ruby-doc.org/core-2.3.1/String.html)* class, which defines a powerful set of operations and methods for manipulating text (e.g., indexing, searching, modifying, etc.). Here are a few easy ways to create Strings:

```ruby
my_string = "Hello." # create a string from a literal
my_empty_string = String.new # create an empty string
my_copied_string = String.new(my_string) # copy a string to a new variable
```

Until Ruby $1.8$, Strings were nothing but a collection of bytes. Data was indexed by byte count, size was in terms of number of bytes, and so
on. Since Ruby $1.9$, Strings have additional
[encoding](http://ruby-doc.org/core-2.2.2/Encoding.html) information attached
to the bytes which provides information on how to interpret them. For example, this code:

```ruby
str = "With ♥!"
print("My String's encoding: ", str.encoding.name) 
print("\nMy String's size: ", str.size)
print("\nMy String's bytesize: ", str.bytesize)
```

produces this output:

    My String's encoding: UTF-8
    My String's size: 7
    My String's bytesize: 9

You can make the following observations about the above code:

- The string literal creates an object which has several accessible methods.
- The string has attached *encoding* information indicating it's an
  [UTF-8](https://en.wikipedia.org/wiki/UTF-8) string.
- A String's *size* corresponds to the umber of characters we see.
- A String's *bytesize* corresponds to the actual space taken by the
characters in memory (the ♥ symbol requires $3$ bytes instead of $1$).

Although $\text{UTF-8}$ is the most popular (and recommended)
encoding style for content, Ruby supports $100$ other encodings (try $\texttt{puts Encoding.list}$ for the full list). With this in mind, we should learn how to convert between different encodings.

**Task** 	
In this challenge, we practice setting the encoding information for some string of text using Ruby's [Encoding](http://ruby-doc.org/core-2.2.2/Encoding.html#class-Encoding-label-Changing+an+encoding) methods. Write a function named *transcode* which takes a $\text{ISO-8859-1}$ encoded string as a parameter, converts it to an $\text{UTF-8}$ encoded string, and returns the result.

## Input Format

Our hidden code checker will call your function, passing it an $\text{ISO-8859-1}$ encoded string as an argument.

## Output Format

Your function must return an $\text{UTF-8}$ encoded string.

## Constraints

- Your function must be named *transcode*.
