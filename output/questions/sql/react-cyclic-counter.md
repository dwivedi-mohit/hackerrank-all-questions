# React: Cyclic Counter

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 50
- **Success Ratio:** 0.6852497096399536
- **Total Submissions:** 861
- **Solved Count:** 590
- **URL:** https://www.hackerrank.com/challenges/react-cyclic-counter

## Problem Statement

Overview

 

In this task, the goal is to build a simple cyclic counter component. The component must be rendered as <button> with text content corresponding to the current count. Initially, the count is always 0. The component receives a prop cycle defining the counting cycle. After the component is clicked with the mouse, the count value is incremented by one, and if it reaches the value cycle, it is reset to 0 instead. Please see the below animation to see how this is supposed to work when the given cycle value is 4.

 

 

User Interface Elements

 

The project is initially filled with boilerplate code with the following elements in the interface. Their properties and behavior must be defined as given. Each of these elements must have the given data-testid property, which will be used while testing the solution.

 

The <button> rendered by CycleCount component:

- data-testid: cycle-counter

- initial text content: 0

 

Expected Behavior

 

Clicking on <button> rendered by the CycleCount component must result in the appropriate user interface changes:

- If the text content of <button> before the click was integer k, then it is updated to k + 1, unless k + 1 = cycle, in which case, it is reset to 0 instead.
