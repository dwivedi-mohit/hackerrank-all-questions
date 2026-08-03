# Attending Workshops

---

| Field | Value |
|---|---|
| **Slug** | `attending-workshops` |
| **Domain** | cpp |
| **Difficulty** | Medium |
| **Score** | 35 |
| **URL** | https://www.hackerrank.com/challenges/attending-workshops |

---

## Preview

Define a structure for the workshop and find the number of workshops that the student can attend.

## Problem Statement

A student signed up for $n$ workshops and wants to attend the maximum number of workshops where no two workshops overlap. You must do the following:

Implement $2$ [structures](http://www.cplusplus.com/doc/tutorial/structures/): 

1. <em>struct Workshop</em> having the following members:
	- The workshop's start time.
	- The workshop's duration.
	- The workshop's end time.

2. <em>struct Available_Workshops</em> having the following members:
	- An integer, $n$ (the number of workshops the student signed up for).
    - An array of type <em>Workshop</em> array having size $n$.


Implement $2$ [functions](http://www.cplusplus.com/doc/tutorial/functions/):

1. <em>Available_Workshops&#42; initialize (int start_time[], int duration[], int n)</em>  <br> 
    Creates an <em>Available_Workshops</em> object and initializes its elements using the elements in the $start\_time[]$ and $duration[]$ parameters (both are of size $n$). Here, $start\_time[i]$</em> and $duration[i]$ are the respective start time and duration for the $i^{th}$ workshop. This function must return a pointer to an <em>Available_Workshops</em> object.

2. <em>int CalculateMaxWorkshops(Available_Workshops&#42; ptr)</em> <br/> 
	Returns the maximum number of workshops the student can attend&mdash;without overlap. The next workshop cannot be attended until the previous workshop ends.

**Note:** An array of unknown size ($n$) should be declared as follows:

	DataType* arrayName = new DataType[n];

## Input Format

Input from stdin is handled by the locked code in the editor; you simply need to write your functions to meet the specifications of the problem statement above.

**Constraints** 


- $1 \le N \le 10^5$ 

- $0 \le start\_time_i \le 10^3$

- $0 \le duration_i \le 10^3$

## Output Format

Output to stdout is handled for you.

Your <em>initialize</em> function must return a pointer to an <em>Available_Workshops</em> object.	
Your <em>CalculateMaxWorkshops</em> function must return maximum number of non-overlapping workshops the student can attend.

## Sample Tests

### Test 1

```
DataType* arrayName = new DataType[n];
```

### Test 2

```
6
1 3 0 5 5 8
1 1 6 2 4 1
```
