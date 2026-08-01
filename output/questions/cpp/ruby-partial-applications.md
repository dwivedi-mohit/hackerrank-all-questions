# Partial Applications

- **Domain:** cpp
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9646279306829766
- **Total Submissions:** 9810
- **Solved Count:** 9463
- **URL:** https://www.hackerrank.com/challenges/ruby-partial-applications

## Problem Statement

In [__Partial Application__](http://rosettacode.org/wiki/Partial_function_application), we create a lambda that takes a parameter and returns a lambda that does something with it.

**Example**:

    multiply_function = -> (number) do
       -> (another_number) do
           number * another_number
       end
    end

    doubler = multiply_function.(2)
    tripler = multiply_function.(3)

    puts doubler.(4)
    puts tripler.(4)

In the above example, the lambda will take *number* as a parameter, and return a lambda. When you call this lambda with *another\_number*, it will return the product of the two.

---
__Task__  

You are given a partially complete code. Your task is to fill in the blanks (`_______`). 

Here, *combination* is a variable that stores a partial application which computes combination __[$^nC_r$](https://en.wikipedia.org/wiki/Combination)__.
