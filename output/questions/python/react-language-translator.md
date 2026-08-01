# React: Language Translator

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 50
- **Success Ratio:** 0.9526774595267746
- **Total Submissions:** 803
- **Solved Count:** 765
- **URL:** https://www.hackerrank.com/challenges/react-language-translator

## Problem Statement

Overview

 

In this task, the goal is to build a very simple language translator. This translator takes a translations Map object as a prop, and renders one text input field and one read-only text field for the translation output. Once a translatable word is typed in the input, the corresponding translation is shown in the output field. Otherwise, the output field is empty.

 

User Interface Elements

 

The project is initially filled with boilerplate code with the following elements in the interface. Their properties and behavior must be defined as given. Each of these elements must have the given data-testid property, which will be used while testing the solution.

 

Input Text

  - data-testid: text-input

  - initial value: "", i.e. empty string

 

Output Text

  - data-testid: text-output

  - readOnly

 

Expected Behavior

 

The component Translator receives a prop translations, which is a Map from input words to their translations. Once a word is typed in the input for which a translation exists in the translations Map, the corresponding translation must be shown in the output field. Otherwise, the output field must be empty.
