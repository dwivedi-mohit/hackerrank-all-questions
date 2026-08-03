# While Language

---

| Field | Value |
|---|---|
| **Slug** | `while-language-fp` |
| **Domain** | fp |
| **Difficulty** | Expert |
| **Score** | 150 |
| **URL** | https://www.hackerrank.com/challenges/while-language-fp |

---

## Preview

Write interpreter for While language.

## Problem Statement

Here you have to design an interpreter for a subset of the _While_ language. It is a simple imperative language which only supports integer literals.


We will use similar grammar which its authors<sup>[1][1],[2][2],[3][3]</sup> have used. Below is the description of grammar that we will use.

*   x, y &isin; **Var** (variables)
*   n &isin; **Num** (numerals/integers)

*   op<sub>a</sub> &isin; **Op<sub>a</sub>** (arithmetic operators)

	op<sub>a</sub> ::= `+` | `-` | `*` | `/`


*   op<sub>b</sub> &isin; **Op<sub>b</sub>** (boolean operators)

    op<sub>b</sub> ::= `and` | `or`


*   op<sub>r</sub> &isin; **Op<sub>r</sub>** (relational operators)

	op<sub>r</sub> ::= `>` | `<`


*   a &isin; **AExp** (arithmetic expressions)

	a ::= x | n | a<sub>1</sub> op<sub>a</sub> a<sub>2</sub> | ( a )

*   b &isin; **BExp** (boolean expressions)

    b ::= **true** | **false** | b<sub>1</sub> op<sub>b</sub> b<sub>2</sub> | a<sub>1</sub> op<sub>r</sub> a<sub>2</sub>  | ( b )

*   S &isin; **Stmt** (statements)

    S ::= x := a | S<sub>1</sub> **;** S<sub>2</sub> | **if** b **then {** S<sub>1</sub> **} else {** S<sub>2</sub> **}** | **while** b **do {** S **}**

  


Here all operators are left associative. Their *precedence order* is as follows.

1. *Arithmetic Operators:* (`*`, `/`) > (`+`, `-`) > (`>`, `<`)  

2. *Boolean Operators:* `and` > `or`


You can safely assume that all variables have integer type and are initialized properly. All variables name will consist of only lowercase letter ('a'-'z') and it's length will not exceed 10.

Note that "`;`" is more like of a sequencing operator. It is used to concatenate two statements. That's why there will be no "`;`" at the end of block of statements.

All divisions are integers divisions, that is, `a/b = floor(a/b)`. Intermediate values of any variable will always be in range [0, 2\*10<sup>18</sup>].


All test cases are *valid* programs. All of them will execute no more than 10<sup>6</sup> operations. All operators and operand will be separated by at least one white space.

**Input**

Input will be the multiline *While* program. You have to read it to the end of file.

**Output**

At the end of program, you have to print each variable's name and its value, in different lines, sorted by the lexicographical order of name.

**Sample Input #00**


    fact := 1 ;
    val := 10000 ;
    cur := val ;
    mod := 1000000007 ;

    while ( cur > 1 )
      do
       {
          fact := fact * cur ;
          fact := fact - fact / mod * mod ;
          cur := cur - 1
       } ;

    cur := 0


**Sample Output #00**


    cur 0
    fact 531950728
    mod 1000000007
    val 10000

**Sample Input #01**


    a := 10 ;
    b := 100 ;

    if ( a < b ) then
        {
            min := a ;
            max := b
        }
    else {
        min := b ;
        max := a
        }

**Sample Output #01**


    a 10
    b 100
    max 100
    min 10

**Explanation**

*Sample Case #00:*  This programs calculate the factorial of a number. Here it calculate the value of `10000! % (10^9+7)` using _while_ statement. Using the property `a % b == a - (a/b)*b` we calcuated the modulo of solution.

*Sample Case #01:*  This program finds the maximum and minimum of `a` and `b` using _if else_ statement.


[1]: http://lbtweb.pbworks.com/w/page/52117907/Hanne%20Riis%20Nielson "Hanne Riis Nielson"
[2]: http://www.doc.ic.ac.uk/~clh/ "Chris Hankin"
[3]: http://lbtweb.pbworks.com/w/page/52415334/Flemming%20Nielson "Flemming Nielson"

## Sample Tests

### Test 1

```
fact := 1 ;
val := 10000 ;
cur := val ;
mod := 1000000007 ;
while ( cur > 1 )
 do
 {
 fact := fact * cur ;
 fact := fact - fact / mod * mod ;
 cur := cur - 1
 } ;
cur := 0
```

### Test 2

```
cur 0
fact 531950728
mod 1000000007
val 10000
```

### Test 3

```
a := 10 ;
b := 100 ;
if ( a < b ) then
 {
 min := a ;
 max := b
 }
else {
 min := b ;
 max := a
 }
```

### Test 4

```
a 10
b 100
max 100
min 10
```
