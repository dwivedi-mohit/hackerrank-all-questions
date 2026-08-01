# Collections.OrderedDict()

- **Domain:** python
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9828469560050147
- **Total Submissions:** 137993
- **Solved Count:** 135626
- **URL:** https://www.hackerrank.com/challenges/py-collections-ordereddict

## Problem Statement

###<sub>[collections.OrderedDict](https://docs.python.org/2/library/collections.html#ordereddict-objects)</sub>

An *OrderedDict* is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged. 

__Example__

<sub>__Code__</sub>

    >>> from collections import OrderedDict
    >>> 
    >>> ordinary_dictionary = {}
    >>> ordinary_dictionary['a'] = 1
    >>> ordinary_dictionary['b'] = 2
    >>> ordinary_dictionary['c'] = 3
    >>> ordinary_dictionary['d'] = 4
    >>> ordinary_dictionary['e'] = 5
    >>> 
    >>> print ordinary_dictionary
    {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
    >>> 
    >>> ordered_dictionary = OrderedDict()
    >>> ordered_dictionary['a'] = 1
    >>> ordered_dictionary['b'] = 2
    >>> ordered_dictionary['c'] = 3
    >>> ordered_dictionary['d'] = 4
    >>> ordered_dictionary['e'] = 5
    >>> 
    >>> print ordered_dictionary
    OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

---
__Task__  

You are the manager of a supermarket.  
You have a list of $N$ items together with their prices that consumers bought on a particular day.  
Your task is to print each `item_name` and `net_price` in order of its first occurrence.  

<sub>`item_name` = Name of the item.</sub>  
<sub>`net_price` = Quantity of the item sold multiplied by the price of each item.</sub>


## Input Format

The first line contains the number of items, $N$.  
The next $N$ lines contains the item's name and price, separated by a space.

__Constraints__

$ 0 < N \le 100$

## Output Format

Print the `item_name` and `net_price` in order of its first occurrence.

## Sample Input

BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

## Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

## Explanation

BANANA FRIES: Quantity bought: , Price:

Net Price:

POTATO CHIPS: Quantity bought: , Price:

Net Price:

APPLE JUICE: Quantity bought: , Price:

Net Price:

CANDY: Quantity bought: , Price:

Net Price:
