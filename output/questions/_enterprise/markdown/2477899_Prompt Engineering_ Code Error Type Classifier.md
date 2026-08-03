# Prompt Engineering: Code Error Type Classifier

## Metadata

- **ID:** 2477899
- **Type:** prompt_engineering
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Prompt Engineering, Easy
- **Skills:** Prompt Engineering (Basic)

## Summary

This prompt engineering question evaluates error classification, prompt writing, and priority handling concepts, ideal for junior-level roles. The task requires writing a prompt that classifies error messages or stack traces into specific error type labels based on defined criteria.

## Problem Statement

A developer tooling platform processes error messages and short stack trace snippets from build logs, CI pipelines, and runtime reports. The candidate must write a prompt that reads a single error message or short stack trace snippet and classifies it into exactly one error type label.

 

Task

Write a prompt that reads a single error message or short stack trace snippet and outputs exactly one error type label based on the nature of the failure.

 

Error type definitions:

	
- 
	
SYNTAX_ERROR — The code could not be parsed; the interpreter or compiler rejected it before execution

	
	
- 
	
NETWORK_ERROR — The failure involves a network connection, remote host, or communication issue

	
	
- 
	
PERMISSION_ERROR — The failure involves access being denied or insufficient privileges to perform an operation

	
	
- 
	
RUNTIME_ERROR — The code was valid and started executing but failed due to a type mismatch, missing reference, null value, or missing key

	
	
- 
	
UNKNOWN_ERROR — The error does not clearly fit any of the above categories

	

 

Allowed output values:

	
- 
	
SYNTAX_ERROR

	
	
- 
	
NETWORK_ERROR

	
	
- 
	
PERMISSION_ERROR

	
	
- 
	
RUNTIME_ERROR

	
	
- 
	
UNKNOWN_ERROR

	

Rules:

	
- 
	
Apply categories in this priority order and stop at the first match: SYNTAX_ERROR → NETWORK_ERROR → PERMISSION_ERROR → RUNTIME_ERROR → UNKNOWN_ERROR.

	
	
- 
	
Output must be exactly one label. No explanation, no punctuation, no other text.

	

 

NOTE: The {testcase input} field is a placeholder that will be auto-filled with various inputs to test the prompt.

 

Sample Case 1

 

Sample Input

`TypeError: Cannot read property 'length' of undefined
    at processItems (app.js:42)`
```

 

Sample Output

`RUNTIME_ERROR`
```

 

Explanation

The code executed but failed when trying to access a property on an undefined value. No syntax, network, or permission issue is involved → RUNTIME_ERROR.

Sample Case 2

 

Sample Input

`SyntaxError: Unexpected token '}'
    at parseConfig (config-loader.js:18)`
```

Sample Output

`SYNTAX_ERROR`
```

 

Explanation

The parser rejected the code before it could run due to a syntax problem. This is the highest-priority category → SYNTAX_ERROR.

## Sample Input/Output

## Preview

A developer tooling platform processes error messages and short stack trace
