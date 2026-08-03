# Strings

---

| Field | Value |
|---|---|
| **Slug** | `c-tutorial-strings` |
| **Domain** | cpp |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/c-tutorial-strings |

---

## Preview

Learn how to input and output strings.

## Problem Statement

C++ provides a nice alternative data type to manipulate strings, and the data type is conveniently called _string_. Some of its widely used features are the following:

- *Declaration:*
	
    	string a = "abc";
      

- *Size:* 

		int len = a.size();

- *Concatenate two strings:*

		string a = "abc";
        string b = "def";
        string c = a + b; // c = "abcdef".

- *Accessing $i^{th}$ element:*

        string s = "abc";
        char   c0 = s[0];	// c0 = 'a'
        char   c1 = s[1];	// c1 = 'b'
        char   c2 = s[2];	// c2 = 'c'
      

        s[0] = 'z';			// s = "zbc"



*P.S.:* We will use _cin/cout_ to read/write a string.

## Input Format

You are given two strings, $a$ and $b$, separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').

## Output Format

In the first line print two space-separated integers, representing the length of $a$ and $b$ respectively.

In the second line print the string produced by concatenating $a$ and $b$ ($a+b$).

In the third line print two strings separated by a space, $a'$ and $b'$. $a'$ and $b'$ are the same as $a$ and $b$, respectively, except that their first characters are swapped.

## Sample Tests

### Test 1

```
string a = "abc";
```

### Test 2

```
int len = a.size();
```

### Test 3

```
string a = "abc";
string b = "def";
string c = a + b; // c = "abcdef".
```

### Test 4

```
string s = "abc";
char c0 = s[0]; // c0 = 'a'
char c1 = s[1]; // c1 = 'b'
char c2 = s[2]; // c2 = 'c'
s[0] = 'z'; // s = "zbc"
```

### Test 5

```
abcd
ef
```

### Test 6

```
4 2
abcdef
ebcd af
```
