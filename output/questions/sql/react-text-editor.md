# React: Text Editor

- **Domain:** sql
- **Difficulty:** Easy
- **Max Score:** 50
- **Success Ratio:** 0.9487603305785124
- **Total Submissions:** 605
- **Solved Count:** 574
- **URL:** https://www.hackerrank.com/challenges/react-text-editor

## Problem Statement

Overview

 

In this task, the goal is to build a very simple text editor.

 

User Interface Elements

 

The project is initially filled with boilerplate code with the following elements in the interface. Their properties and behavior must be defined as given. Each of these elements must have the given data-testid property, which will be used while testing the solution.

 

Text Field

  - data-testid: text-field

  - initial text content: "", i.e. empty string

 

Word Input

  - data-testid: word-input

  - initial value: "", i.e. empty string

 

Append Button

  - data-testid: append-button

  - disabled when the Word Input is empty

 

Undo Button

  - data-testid: undo-button

  - disabled when the current text content of the editor is empty

 

Expected Behavior

 

When the Word Input has a non-empty value and the Append Button is clicked, the Word Input is emptied so its value becomes "". Additionally, the word typed in the input must appear in the content of Text Field as the last word, where the content of the Text Field consists of all typed words that have not been undone, joined by a single space character.

 

When the Undo Button is clicked, the last appended and not already undone word from the content of the Text Field is removed (along with the space character preceding it if it exists).
