# Input and Output

---

| Field | Value |
|---|---|
| **Slug** | `cpp-input-and-output` |
| **Domain** | cpp |
| **Difficulty** | Easy |
| **Score** | 5 |
| **URL** | https://www.hackerrank.com/challenges/cpp-input-and-output |

---

## Preview

Learn to take in the input and print the output. Take three number as input and print their sum as output.

## Problem Statement

**Objective**		
In this challenge, we practice reading input from stdin and printing output to stdout. 

----

In C++, you can read a single whitespace-separated token of input using [cin](http://www.cplusplus.com/cin), and print output to stdout using [cout](http://www.cplusplus.com/printf). For example, let's say we declare the following variables:

```cpp
string s;
int n;
```
and we want to use *cin* to read the input "High 5" from stdin. We can do this with the following code:

```cpp
cin >> s >> n;
```

This reads the first word ("High") from stdin and saves it as string $s$, then reads the second word ("$5$") from stdin and saves it as integer $n$. If we want to print these values to stdout, separated by a space, we write the following code:

```cpp
cout << s << " " << n << endl;
```

This code prints the contents of string $s$, a single space ($\text{" "}$), then the integer $n$. We end our line of output with a newline using [endl](http://www.cplusplus.com/endl). This results in the following output:

	High 5
	


**Task**	
Read $3$ numbers from stdin and print their sum to stdout.

## Input Format

One line that contains $3$ space-separated integers: $a$, $b$, and $c$.

## Output Format

Print the sum of the three numbers on a single line.

## Constraints

- $1 \le a, b, c \le 1000$

## Sample Tests

### Test 1

```
string
s
;
int
n
;
```

### Test 2

```
cin
>>
s
>>
n
;
```

### Test 3

```
cout
<<
s
<<
" "
<<
n
<<
endl
;
```

### Test 4

```
High 5
```

### Test 5

```
1 2 7
```

### Test 6

```
10
```
