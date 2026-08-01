# Ruby - Enumerable - Introduction

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 10
- **Success Ratio:** 0.988842631140716
- **Total Submissions:** 18015
- **Solved Count:** 17814
- **URL:** https://www.hackerrank.com/challenges/ruby-enumerable-introduction

## Problem Statement

In control structures
[tutorial](https://www.hackerrank.com/domains/ruby/control-structures), we
learned about various methods to iterate over a collection like `unless`,
`loop` and the most commonly used `each`
[method](https://www.hackerrank.com/challenges/ruby-tutorial-each).

Ruby, however, provides an `Enumerable` module which packages a bunch of
methods which can be used with any other class by including it (referred to as
*mixing in*). That means that programmers don't have to write all those methods
many different times for different objects. As long as the custom object
defines an `each` method and includes `Enumerable` module, it can get access
to all of its magic.

In this challenge, you have been provided with a custom object called `colors` that
defines its own `each` method. You need to iterate over the items and return
an `Array` containing the values.
