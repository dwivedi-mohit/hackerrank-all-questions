# React: Autocorrection App

## Metadata

- **ID:** 830922
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Front-End Frameworks, React, JavaScript
- **Skills:** React (Basic)

## Summary

This front-end development question evaluates React, component state management, and user input handling concepts, ideal for junior-level roles. The problem requires creating an autocorrection application that modifies user input based on a provided corrections object.

## Problem Statement

Create a basic autocorrection application per the requirements below. The finished application must pass all of the unit tests.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

 

Complete the implementation of src/components/AutocorrectTextarea.js according to the following requirements:

	
- AutocorrectTextarea is a component that takes a corrections Object that maps strings to their corrections. For example, the object below denotes that 'really' is a correction for 'realy', and 'weird' is a correction of 'wierd':
	
`const corrections = {
  'realy': 'really',
  'wierd': 'weird',
};
`
```

	
	
- Assume that no value of the corrections object appears as the property in the corrections object.
	
- AutocorrectTextarea renders a textarea element and lets users write text in it.
	
- Assume that the text consists only of words separated by a single space character.
	
- Once a space character is typed, the word preceding it is considered to be complete and must be autocorrected according to the corrections object if a correction exists.

 

Initially, the file is filled with boilerplate code. Note the following:

	
- The textarea element must have `data-testid="textarea"`.

 

Please note that the component has these data-testid attributes for test cases, and certain classes and ids for rendering purposes. You should not change them.

## Preview

Create a basic autocorrection application per the requirements below. The fini
