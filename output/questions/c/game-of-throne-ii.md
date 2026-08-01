# Game Of Thrones - II

- **Domain:** c
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6249445184198846
- **Total Submissions:** 2253
- **Solved Count:** 1408
- **URL:** https://www.hackerrank.com/challenges/game-of-throne-ii

## Problem Statement

This follows from [Game of Thrones - I](https://www.hackerrank.com/contests/july13/challenges/game-of-thrones).

Now that the king knows how to find out whether a given word has an [anagram](https://en.wikipedia.org/wiki/Anagram) which is a [palindrome](http://en.wikipedia.org/wiki/Palindrome) or not, he encounters another challenge. He realizes that there can be more than one palindrome anagrams for a given word. Can you help him find out how many palindrome anagrams are possible for a given word ?

The king has many words. For each given word, he needs to find out the number of palindrome anagrams of the string. As the number of anagrams can be large, the king needs the number of anagrams % (10<sup>9</sup>+ 7).

**Input format :**<br>
A single line which contains the input string<br>

**Output format :**  
A single line which contains the number of anagram strings which are palindrome % (10<sup>9</sup> + 7).

**Constraints :**  
1<=length of string <= 10^5  
Each character of the string is a lowercase alphabet.  
Each test case has at least 1 anagram which is a palindrome. 
  
**Sample Input 01 :**

    aaabbbb

**Sample Output 01 :**

    3 

**Explanation :**  
Three palindrome permutations of the given string are abbabba , bbaaabb and bababab.

**Sample Input 02 :**

    cdcdcdcdeeeef

**Sample Output 02 :**

    90


## Constraints

1<=length of string <= 10^5

Each character of the string is a lowercase alphabet.

Each test case has at least 1 anagram which is a palindrome.

## Sample Input

aaabbbb

## Sample Output

3

## Explanation

Three palindrome permutations of the given string are abbabba , bbaaabb and bababab.
