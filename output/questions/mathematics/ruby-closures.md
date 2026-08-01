# Closures

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9836332312404288
- **Total Submissions:** 10448
- **Solved Count:** 10277
- **URL:** https://www.hackerrank.com/challenges/ruby-closures

## Problem Statement

[__Closure__](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function/method that:  

__► Can be passed around like an object.__  
<blockquote>
It can be treated like a variable, which can be assigned to another variable, passed as an argument to a method. </blockquote>

__► Remembers the value of variables no longer in scope.__  
<blockquote>
It remembers the values of all the variables that were in scope when the function was defined. It is then able to access those variables when it is called even if they are in a different scope.</blockquote>

**Example:**

    def plus_1(y)
       x = 100
       y.call   	#remembers the value of x = 1
    end

    x = 1
    y = -> { x + 1 }
    puts plus_1(y)	#2

In this example, the variable $x$, which is closed within the lambda $y$, remembers its values. Here, $x$ remembers its value as $1$.

Blocks, Procs and Lambdas are closures in Ruby.    

---

__Task__  

You are given a partially complete code. Your task is to fill in the blanks (`______`).  

$→$ *block\_message\_printer* prints the message if the block exists.  
$→$ *proc\_message\_printer* prints the message inside a Proc.  
$→$ *lambda\_message\_printer* prints the message inside a Lambda.
