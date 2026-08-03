# Occupations

---

| Field | Value |
|---|---|
| **Slug** | `occupations` |
| **Domain** | sql |
| **Difficulty** | Medium |
| **Score** | 30 |
| **URL** | https://www.hackerrank.com/challenges/occupations |

---

## Preview

Pivot the Occupation column so the Name of each person in OCCUPATIONS is displayed underneath their respective Occupation.

## Problem Statement

[Pivot](https://en.wikipedia.org/wiki/Pivot_table) the *Occupation* column in **OCCUPATIONS** so that each *Name* is sorted alphabetically and displayed underneath its corresponding *Occupation*. The output should consist of four columns (*Doctor*, *Professor*, *Singer*, and *Actor*) in that specific order, with their respective names listed alphabetically under each column.

**Note:** Print **NULL** when there are no more names corresponding to an occupation.

## Input Format

The **OCCUPATIONS** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12889/1443816414-2a465532e7-1.png" />

*Occupation* will only contain one of the following values: **Doctor**, **Professor**, **Singer** or **Actor**.

## Sample Tests

### Test 1

```
Jenny Ashley Meera Jane
Samantha Christeen Priya Julia
NULL Ketty NULL Maria
```
