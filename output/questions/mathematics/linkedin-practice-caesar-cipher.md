# Caesar Cipher: Encryption

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 40
- **Success Ratio:** 0.8170713316241894
- **Total Submissions:** 6631
- **Solved Count:** 5418
- **URL:** https://www.hackerrank.com/challenges/linkedin-practice-caesar-cipher

## Problem Statement

Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, $K$, making it unreadable by his enemies. Given a string, $S$, and a number, $K$, encrypt $S$ and print the resulting string.   

**Note:** The cipher *only* encrypts letters; symbols, such as `-`, remain unencrypted.	

## Input Format

The first line contains an integer, $N$, which is the length of the unencrypted string.		
The second line contains the unencrypted string, $S$.	
The third line contains the integer encryption key, $K$, which is the number of letters to rotate.

**Constraints**   
$1 \le N \le 100$  
$0 \le K \le 100$  
$S$ is a valid ASCII string and doesn't contain any spaces.  

## Output Format

For each test case, print the encoded string.  

## Constraints

is a valid ASCII string and doesn't contain any spaces.

## Sample Input

middle-Outz
2

## Sample Output

okffng-Qwvb

## Explanation

Each unencrypted letter is replaced with the letter occurring  spaces after it when listed alphabetically. Think of the alphabet as being both case-sensitive and circular; if  rotates past the end of the alphabet, it loops back to the beginning (i.e.: the letter after  is , and the letter after  is ).

Selected Examples:

 (ASCII 109) becomes  (ASCII 111).

 (ASCII 105) becomes  (ASCII 107).

 remains the same, as symbols are not encoded.

 (ASCII 79) becomes  (ASCII 81).

 (ASCII 122) becomes  (ASCII 98); because  is the last letter of the alphabet,  (ASCII 97) is the next letter after it in lower-case rotation.
