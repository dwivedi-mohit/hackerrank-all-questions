# Forward References

---

| Field | Value |
|---|---|
| **Slug** | `forward-references` |
| **Domain** | regex |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/forward-references |

---

## Preview

Back reference to a group which appear later in regex.

## Problem Statement

__<sub>NOTE - `Forward reference is supported by JGsoft, .NET, Java, Perl, PCRE, PHP, Delphi and Ruby regex flavors.`</sub>__ 

[Forward reference](http://www.regular-expressions.info/backref2.html#forward) creates a back reference to a regex that would appear later.

Forward references are only useful if they're inside a repeated group.

Then there may arise a case in which the regex engine evaluates the backreference after the group has been matched already.

<img src="https://s3.amazonaws.com/hr-challenge-images/14820/1449647867-1c44daf341-ach21.png" title="ach21.png" />
<sub>$$In\ the \ above \ image, \ Regex \ Pattern \ is \ matched \ with \ the \ Test \ String. $$</sub>

___
__Task__ 

You have a test string $S$.  

Your task is to write a regex which will match $S$, with following condition(s):

- $S$ consists of __`tic`__ or __`tac`__.

- __`tic`__ should not be immediate neighbour of itself.

- The first __`tic`__ must occur only when __`tac`__ has appeared at least twice before.

__Valid $S$__
	
    tactactic
    tactactictactic
  

__Invalid $S$__

	tactactictactictictac
	tactictac
  

__Note__


This is a regex only challenge. You are not required to write any code. 

You only have to fill the regex pattern in the blank (`_________`).

## Sample Tests

### Test 1

```
tactactic
tactactictactic
```

### Test 2

```
tactactictactictictac
tactictac
```
