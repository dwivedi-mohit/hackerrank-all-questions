# Security - Message Space and Ciphertext Space

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9649954142464078
- **Total Submissions:** 6542
- **Solved Count:** 6313
- **URL:** https://www.hackerrank.com/challenges/security-message-space-and-ciphertext-space

## Problem Statement

To better understand *Message Spaces* and *Cipher Spaces*, we will first explain the *alphabet of definitions*.

$A$ denotes a finite set called the *alphabet of definition*. For example, $A=\{0,1\}$ is the *binary alphabet*. It is a frequently used alphabet of definition.

$M$ denotes a set called *message space*. $M$ consists of strings composed of symbols from an alphabet of definition.

$C$ denotes a set called the *ciphertext space*. $C$ consists of strings composed of symbols from an alphabet of definition which might or might not differ from that of $M$.

For example, consider the following encryption: You get a message composed of lowercase English characters only. For any letter in the message, you shift it one time and create a new message that you then transmit. If you get "$abz$" then you transform it to "$bca$". <br>
Here, $A$ is $\{$'$a$', '$b$', '$c$', ... , '$z$'$\}$.

Both $C$ and $M$ are sets of all strings composed of lowercase English characters.

For example:

$\{abc, degg, fe, ...\} \in M$

and 

$\{bcd, efhh, gf, ....\} \in C$ (corresponding to the strings in $M$)

For every possible string in $M$, there is a string in $C$.  

In this task, your alphabet of definition is $A = \{0, 1, 2, ..., 9\}$. <br>
$M$ and $C$ are both sets of all strings consisting of decimal digits. Given a coded message, you need to find the new message you obtain if you shift each digit in the message string. You must shift $1$ to the right, and it is cyclic.

**Constraints** 

$1\le$ *Length of the string* $\le 10$

## Input Format

Input consists of a single line that contains the string.

## Output Format

Output a single line, the shifted string.

## Constraints

Length of the string
