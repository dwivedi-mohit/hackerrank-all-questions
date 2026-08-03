# PHP: Password Hash Generator

## Metadata

- **ID:** 1703927
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** PHP, Easy
- **Skills:** PHP (Basic)
- **Languages:** p, h, p

## Summary

This coding question evaluates PHP, object-oriented programming, and string manipulation concepts, ideal for junior-level roles. The problem requires implementing a secure password hash generator that appends a fixed salt to a password before generating an MD5 hash.

## Problem Statement

Implement a secure password hash generator with salt to protect user credentials.

 

Class requirements:

	
- Create a class named PasswordHashGenerator with:

	
		
- A constructor that accepts a string parameter representing a password
		
- A method getHash() that returns an MD5 hash of the password with a salt
	
	

Implementation details:

	
- The getHash() method must:

	
		
- Append the fixed salt string "THIS_IS_THE_SALT" to the password
		
- Generate and return an MD5 hash of the combined string
		
- Example: For password "abcdefghijklm", hash the string "abcdefghijklmTHIS_IS_THE_SALT"
	
	

Requirements:

	
- Use the MD5 algorithm for hashing
	
- Always append the same fixed salt string to every password before hashing

 

Constraints

	
- The hash should be generated using the MD5 algorithm.
	
- The salt THIS_IS_THE_SALT is a fixed string and should be appended to every password before hashing.

 

Input Format for Custom Testing

Input from stdin will be processed as follows and used to instantiate the PasswordHashGenerator class.

 

Each line contains a string representing a password.

 

Sample Case 0

Sample Input 0

"gM994""}}>`H"
"tG178@.}"")"
pO351(#=@`
"bE200@',%@_#wUs"
qG672)=)>/

```

Sample Output 0

8464ab1864957b517d50d35faafba17c
e0371c19870510f0c460a0ce87a5ed6c
49009fba14f549953005025e91876bfa
626d1f032db1cb7534d8575fc21ed735
2aa826d2b5e24e9bc1b7c18011aae651

```

Explanation

For each input line, the PasswordHashGenerator::getHash method outputs a salted hash of the incoming password, ensuring secure storage.

Sample Case 1

Sample Input 1

"uV462(,}'*Z}92g"
kV544}{#)?!?J5kW
gZ125&!@/$a/JnD)
nF625{`%<+I=aW~Y
"lE780)@&!""Th>"
"hN626+.,>/"
aB675/})(`
qI366&~{<@0Er
gT767&+`%@<C}d/H
mI572#'_/<@FB$s'

```

Sample Output 1

e614ff3572c39c6be815ccfa137e2fbb
c8e3c378f6fe817376f84ef74990db49
2431f7e75a309e39413d93bd6514ec76
78aead4fe3280e1dabc204f3fe5fc938
75ee2a90e1a3e6a745103cba05c51916
207a0cb8f752794945d992be2d7d5aa5
d887473cf6e8a4e039c268b3506c9b35
bb013a66a823577da8c429038523a966
cea99741ae636fbf6b876bb8e522a481
e993d010a7fc1a68b40509fe9d62418a

```

Explanation

For each input line, the PasswordHashGenerator::getHash method outputs a salted hash of the incoming password, ensuring secure storage.

## Sample Input/Output

## Preview

Implement a secure password hash generator with salt to protect user credentia
