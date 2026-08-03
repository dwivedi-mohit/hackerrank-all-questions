# Oil Well

---

| Field | Value |
|---|---|
| **Slug** | `oil-well` |
| **Domain** | algorithms |
| **Difficulty** | Hard |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/oil-well |

---

## Preview

Given RxC matrix with 0/1. Rearrange the cells having 1 so that the manhattan disctance sum of adjacent cells in this list is minimal. Fidn the sum

## Problem Statement

Mr. Road Runner bought a piece of land in the middle of a desert for a nominal amount. It turns out that the piece of land is now worth millions of dollars as it has an oil reserve under it. Mr. Road Runner contacts the ACME corp to set up the oil wells on his land. Setting up oil wells is a costly affair and the charges of setting up oil wells are as follows. 

The rectangular plot bought by Mr. Road Runner is divided into *r* * *c* blocks. Only some blocks are suitable for setting up the oil well and these blocks have been marked. ACME charges nothing for building the first oil well. For every subsequent oil well built, the cost would be the maximum **ACME distance** between the new oil well and the existing oil wells. 

If *(x,y)* is the position of the block where a new oil well is setup and *(x1, y1)* is the position of the block of an existing oil well, the *ACME distance* is given by 

    max(|x-x1|, |y-y1|)

the maximum *ACME distance* is the maximum among all the *ACME distance* between existing oil wells and new wells. 

If the distance of any two adjacent blocks (horizontal or vertical) is considered 1 unit, what is the minimum cost *(E)* in units it takes to set up oil wells across all the marked blocks?

## Input Format

The first line of the input contains two space separated integers *r* *c*.

*r* lines follow each containing *c* space separated integers. 

1 indicates that the block is suitable for setting up an oil well, whereas 0 isn't. 

    r c

    M11 M12 ... M1c

    M21 M22 ... M2c

    ...

    Mr1 Mr2 ... Mrc

## Output Format

Print the minimum value E as the answer.

## Constraints

1 <= r, c <= 50

## Sample Tests

### Test 1

```
max(|x-x1|, |y-y1|)
```

### Test 2

```
r c 
M11 M12 ... M1c 
M21 M22 ... M2c 
... 
Mr1 Mr2 ... Mrc
```

### Test 3

```
1 <= r, c <= 50
```

### Test 4

```
3 4
1 0 0 0
1 0 0 0
0 0 1 0
```

### Test 5

```
3
```
