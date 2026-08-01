# Ruby Control Structures - Case (Bonus Question)

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.9556400506970849
- **Total Submissions:** 33138
- **Solved Count:** 31668
- **URL:** https://www.hackerrank.com/challenges/ruby-case

## Problem Statement

This is a bonus question. Feel free to skip to the next challenge.

HackerRank is written in [RoR](http://rubyonrails.org/) and we have various classes defined in it. Some of them are 

1. `Hacker`
2. `Submission`
3. `TestCase`
4. `Contest`

etc. 

You have been given a function where an object which may or may not be of the above mentioned type is sent as an argument. You have to use the `case` control structure in Ruby to identify the class to which the object belongs and print the following output: 

+ if `Hacker`, output "It's a Hacker!"  
+ if `Submission`, output "It's a Submission!"
+ if `TestCase`, output "It's a TestCase!"  
+ if `Contest`, output "It's a Contest!"  
+ for any other object, output "It's an unknown model" 

**Note**

+ use `case` (switch statement of Ruby)
+ use `puts` for printing
+ Ruby Docs on [case](http://ruby-doc.org/docs/keywords/1.9/Object.html#method-i-case)
