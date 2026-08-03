# Python: P2P Network Encryption

## Metadata

- **ID:** 1651901
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Python, Math, Easy, Cryptography
- **Skills:** Python (Basic)
- **Languages:** p, y, t, h, o, n, 3

## Summary

This coding question evaluates decryption algorithms, string manipulation, and character shifting concepts, ideal for junior-level roles. The problem requires implementing a function to decrypt a string using a Caesar cipher with a specified shift value.

## Problem Statement

A peer-to-peer (P2P) network featuring end-to-end encryption is under development. As part of this system, a decryption function is required to activate whenever a user logs in.

 

The encryption method involves replacing each letter in a file with another letter shifted by a fixed number of positions down the alphabet. This shift value acts as the private key for each user. The decryption algorithm can be described as follows:

	
- 
secret represents the encrypted content of the file (comprising lowercase or uppercase English letters without spaces)
	
- 
shift indicates the fixed number of positions down the alphabet (the shift value)

 

Letters, whether lowercase or uppercase, are shifted left from their original positions, wrapping around the alphabet if necessary. For example, 'a' with a shift of 1 becomes 'z', and 'A' with a shift of 1 becomes 'Z'.

 

Example

Given the secret 'KcoTKQ' and a shift of 2, the function should return 'IamRIO'. The decryption process involves shifting each letter back from its original position by 2 positions:

'K' -> 'I'

'c' -> 'a'

'o' -> 'm'

'T' -> 'R'

'K' -> 'I'

'Q' -> 'O'

 

Function Description

Complete the function decipher in the editor with the following parameter(s):

    str secret: a string consisting of lowercase or uppercase English letters 

    int shift: the shift value

 

Return

str: the decrypted string

 

Constraints

	
- 1 ≤ length of secret ≤ 2*105

	
- 0 ≤ shift ≤109

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains a string, secret.

The next line contains an integer, shift.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

MPSZILEGOIVVERO
4

```

Sample Output 0

ILOVEHACKERRANK
```

The decryption process involves shifting each letter back to its original position by 4 positions. For example, 'M' to 'I', 'P' to 'L', and so on.

Sample Case 1

Sample Input For Custom Testing

JsiytJsi
5

```

Sample Output 1

EndtoEnd

```

The decryption process involves shifting each letter back to its original position by 5 positions. For example, 'J' to 'E', 's' to 'n', and so on.

## Sample Input/Output

## Preview

A peer-to-peer (P2P) network featuring end-to-end encryption is under developm
