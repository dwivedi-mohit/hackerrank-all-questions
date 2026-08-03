# TypeScript: Enum Implementation

## Metadata

- **ID:** 1479598
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Freeze
- **Skills:** TypeScript (Basic)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates class implementation, immutability, and object handling concepts, ideal for junior-level roles. The problem requires creating an immutable Enum class that prevents changes to its data after instantiation.

## Problem Statement

Implement a class named Enum that:

	
- Accepts an object in its constructor and saves it in a member called data

	
- Makes the stored object immutable once the class is instantiated

Example

const colorEnum = new Enum({"Red": "ABC"});
colorEnum.data.Red = "DEF"; // This should not change the value
console.log(colorEnum.data.Red); // Should still print "ABC"

```

Function Description

Complete the class Enum. It should contain a constructor() method and a data member.

constructor() has a single parameter, inputData, of the Object type.

 

Constraints

	
- 1 ≤ |str1|, |str2|, |str3| ≤ 10
	
- Strings contain only uppercase English letters [A-Z].

 

Note: |x| is the length of string x.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

There are 3 lines, each with a string. The strings are passed to the constructor of the Enum class and stored in variables.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

GX
GP
UA

```

Sample Output

True
```

Explanation

When properly implemented, the values in Enum cannot be changed after instantiation. True indicates success.

Sample Case 1

Sample Input For Custom Testing

KXKSZHKBP
PHYKINKEZ
PLVFJAQMO

```

Sample Output

True
```

Explanation

When properly implemented, the values in Enum cannot be changed after instantiation. True indicates success.

## Sample Input/Output

## Preview

Implement a class named Enum that:
