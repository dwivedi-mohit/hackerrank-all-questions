# Blocks

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9773747366492627
- **Total Submissions:** 10917
- **Solved Count:** 10670
- **URL:** https://www.hackerrank.com/challenges/ruby-blocks

## Problem Statement

Higher order functions are one of the key components of functional programming.  

A higher order function is a tool that takes other functions as parameters or returns them as a result.

[__Blocks__](http://rubylearning.com/satishtalim/ruby_blocks.html) are nameless methods that can be passed to another method as a parameter.  
Passing a block to a method is a great way of data abstraction.

Blocks can either be defined with a keyword `do ... end` or curly braces `{ ... }`.

**Example:**

__<sub>a). Passing a block to a method that takes no parameter</sub>__  

<sub>__CODE__</sub>  

    def call_block
        puts "Start of method."
        yield
        puts "End of method."
    end 
    call_block do 
        puts "I am inside call_block method."
    end

<sub>__OUTPUT__</sub> 

    Start of method.
    I am inside call_block method.
    End of method.
    
In this example, a block is passed to the *call\_block* method.   
To invoke this block inside the method, we used a keyword, `yield`.  
Calling `yield` will execute the code within the block that is provided to the method. 

__<sub>b). Passing a block to a method that takes one or more parameters.</sub>__

<sub>__CODE__</sub>

    def calculate(a,b)
        yield(a, b)
    end

    puts calculate(15, 10) {|a, b| a - b}	

<sub>__OUTPUT__</sub>

	5
    
In this example, we have defined a method *calculate* that takes two parameters $a$ and $b$.  
The `yield` statement invokes the block with parameters $a$ and $b$, and executes it. 
    
---
__Task__  

You are given a partially complete code. Your task is to fill in the blanks (`_______`).  
The factorial method computes: `n!` { $n $ x $ n - 1 $ x $ .... 2 $ x $ 1$ }.
