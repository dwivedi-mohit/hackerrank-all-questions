# Collections.namedtuple()

---

| Field | Value |
|---|---|
| **Slug** | `py-collections-namedtuple` |
| **Domain** | python |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/py-collections-namedtuple |

---

## Preview

You need to turn tuples into convenient containers using collections.namedtuple().

## Problem Statement

###<sub>__[collections.namedtuple()](https://docs.python.org/2/library/collections.html#collections.namedtuple)__</sub>


Basically, _namedtuples_ are easy to create, lightweight object types.

They turn tuples into convenient containers for simple tasks.

With *namedtuples*, you don’t have to use integer indices for accessing members of a tuple.


**Example**

<sub>__Code 01__</sub>

	>>> from collections import namedtuple
    >>> Point = namedtuple('Point','x,y')
    >>> pt1 = Point(1,2)
    >>> pt2 = Point(3,4)
    >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
    >>> print dot_product
    11
  

<sub>__Code 02__</sub>

    >>> from collections import namedtuple
    >>> Car = namedtuple('Car','Price Mileage Colour Class')
    >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
    >>> print xyz
    Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
    >>> print xyz.Class
    Y

---
__Task__

Dr. John Wesley has a spreadsheet containing a list of student's $IDs$, $marks$, $class$ and $name$.


Your task is to help Dr. Wesley calculate the average marks of the students.

<sub>$$Average = \frac{Sum \ of \ all \ marks }{ Total \ Students }$$</sub>

__<sub>Note:

1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.

2. Column names are `ID`, `MARKS`, `CLASS` and `NAME`. (The spelling and case type of these names won't change.)</sub>__

## Input Format

The first line contains an integer $N$, the total number of students. <br>
The second line contains the names of the columns in any order.

The next $N$ lines contains the $marks$, $IDs$, $name$ and $class$, under their respective column names.

__Constraints__

$ 0 < N \le 100$

## Output Format

Print the average marks of the list corrected to 2 decimal places.

## Sample Tests

### Test 1

```
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```

### Test 2

```
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```

### Test 3

```
5
ID MARKS NAME CLASS 
1 97 Raymond 7 
2 50 Steven 4 
3 91 Adrian 9 
4 72 Stewart 5 
5 80 Peter 6
```

### Test 4

```
5
MARKS CLASS NAME ID 
92 2 Calum 1 
82 5 Scott 2 
94 2 Jason 3 
55 8 Glenn 4 
82 2 Fergus 5
```

### Test 5

```
78.00
```

### Test 6

```
81.00
```
