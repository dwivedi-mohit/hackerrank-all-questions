# Vanity Number Search

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.8801791713325868
- **Total Submissions:** 893
- **Solved Count:** 786
- **URL:** https://www.hackerrank.com/challenges/vanity-number-search

## Problem Statement

Twilio customers sometimes request to purchase vanity phone numbers. These vanity numbers are designed to be unique to the customer's brand and memorable to their end user. An example of this is 1-800-FLOWERS, which translates to 1-800-3569377. Here, each letter in the vanity code (FLOWERS) corresponds to a digit on the ** [T9 keypad map](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/220px-Telephone-keypad2.svg.png)**. So, F maps to 3, L to 5, O to 6 and so on, giving us 3569377. Customers typically search Twilio's phone number inventory for such vanity codes.

 

![](https://s3.amazonaws.com/istreet-assets/coMM7hRH7WY_jly_eo3tOg/t9.png)

 

**Given an array of one or more vanity codes and an array of phone numbers, write a function to find all phone numbers that match one or more vanity codes. ****The output must be a sorted array of unique phone numbers from the input array of numbers.**

 

Function Description

Complete the function _vanity_ in the editor below.

_vanity_ has the following parameter(s):

_    codes[codes[0],...codes[c-1]]_: an array of strings (vanity codes)

_    numbers[numbers[0],...numbers[n-1]]:_  an array of strings (phone numbers)

_vanity _should return a sorted array of phone numbers that match one or more vanity codes.

 

Constraints

- The input numbers array may have repeat elements.
- The output must be a sorted array of unique numbers.
- **Vanity codes will only consist of uppercase letters (A-Z).**
- **All vanity codes will be of shorter length than all phone numbers.**
- **The output array should be subset of the input array of phone numbers.**
- **Vanity codes can appear anywhere in the number, including country or area codes.**
- **Phone numbers will be in the [E.164 format](http://www.twilio.com/docs/glossary/what-e164) i.e. a plus (+) followed by up to 15 digits (0-9).**

 

  Input Format For Custom Testing

The first line contains an integer, _c_, denoting the number of elements in _codes_.

The next _c_ subsequent lines contain one vanity code per line.

The next line contains an integer, _n_, denoting the number of elements in _numbers_.

The final _n_ subsequent lines contain one phone number per line.

  Sample Case

Sample Input For Custom Testing

3 TWLO CODE HTCH 5 +17474824380 +14157088956 +919810155555 +15109926333 +1415123456

Sample Output

+14157088956 +15109926333 +17474824380

Explanation

**TWLO matches +14157088956 (+1415708-TWLO)**

**CODE matches +15109926333 (+151099-CODE-3)**

**HTCH matches +17474824380 (+1747-HTCH-380)**

Extra Credit

A naive solution may cause matching to time out on large arrays of phone numbers. Try to optimize for this once you have a working solution that is passing most test cases.

    


## Constraints

- The input numbers array may have repeat elements.

- The output must be a sorted array of unique numbers.

- Vanity codes will only consist of uppercase letters (A-Z).

- All vanity codes will be of shorter length than all phone numbers.

- The output array should be subset of the input array of phone numbers.

- Vanity codes can appear anywhere in the number, including country or area codes.

- Phone numbers will be in the E.164 format i.e. a plus (+) followed by up to 15 digits (0-9).

Input Format For Custom Testing

The first line contains an integer, c, denoting the number of elements in codes.

The next c subsequent lines contain one vanity code per line.

The next line contains an integer, n, denoting the number of elements in numbers.

The final n subsequent lines contain one phone number per line.

Sample Case

Sample Input For Custom Testing

3 TWLO CODE HTCH 5 +17474824380 +14157088956 +919810155555 +15109926333 +1415123456

## Sample Output

+14157088956 +15109926333 +17474824380

## Explanation

TWLO matches +14157088956 (+1415708-TWLO)

CODE matches +15109926333 (+151099-CODE-3)

HTCH matches +17474824380 (+1747-HTCH-380)

Extra Credit

A naive solution may cause matching to time out on large arrays of phone numbers. Try to optimize for this once you have a working solution that is passing most test cases.
