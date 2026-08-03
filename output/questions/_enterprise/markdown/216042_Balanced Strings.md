# Balanced Strings

## Metadata

- **ID:** 216042
- **Type:** code
- **Difficulty:** 9.444444444444445
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Regex, Medium, Algorithms, Problem Solving
- **Skills:** Problem Solving (Intermediate)
- **Languages:** j, a, v, a, ,, k, o, t, l, i

## Summary

This coding question evaluates regular expressions, algorithms, and problem-solving concepts, ideal for mid-level roles. The problem requires writing a RegEx to determine if a string composed of letters a, b, c, and d is balanced based on specific conditions.

## Problem Statement

Write a RegEx to determine if a string is "balanced".

A string, s, is composed of the letters a, b, c, and d. The string is said to be balanced if both of the following conditions are satisfied:

	
- The summed number of a's and c's is even.
	
- The summed number of b's and d's is even.

For example, the string 'abcd' (a count + c count = 1 + 1 = 2, even, b count + d count = 1 + 1 = 2, even) is balanced, but 'abc' and 'bcd' are not.

 

Complete the code by filling in the blank with a RegEx that only matches balanced strings.

 

Constraints

	
- Each character s[i] is one of {abcd}.

 

 DO NOT REMOVE THIS LINE-->

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the regex for testing.

 

The only line contains a string s, the string to test.

 

Sample Case 0

Sample Input 0

STDIN              Function Parameters 
-----              -------------------
acdbddbbbbaaac →   s = "acdbddbbbbaaac"
```

 

Sample Output 0

true
```

 

Explanation 0

There are six a's and c's in the string and eight b's and d's. Thus, the string is balanced.

 

Sample Case 1

Sample Input 1

STDIN   Function Parameters
-----   -------------------
cdba →  s = "cdba"
```

 

Sample Output 1

true
```

 

Explanation 1

There are two a's and c's in the string and two b's and d's. Thus, the string is balanced.

 

Sample Case 2

Sample Input 2

STDIN   Function Parameters
-----    -------------------
aaccb →  s = "aaccb"
```

 

Sample Output 2

false
```

 

Explanation 2

There are four a's and c's in the string and only one b (there are no d's). Thus, the string is not balanced.

 

Sample Case 3

Sample Input 3

STDIN       Function Parameters
-----       -------------------
cdcdaabb →   s = "cdcdaabb"
```

 

Sample Output 3

true
```

 

Explanation 3

There are four a's and c's in the string and four b's and d's. Thus, the string is balanced.

## Sample Input/Output

## Preview

Write a RegEx to determine if a string is "balanced".
