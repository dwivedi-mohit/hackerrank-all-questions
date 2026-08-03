# Hotel Prices

---

| Field | Value |
|---|---|
| **Slug** | `hotel-prices` |
| **Domain** | cpp |
| **Difficulty** | Medium |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/hotel-prices |

---

## Preview

Debug the existing class definitions so the total hotel's profit is calculated correctly.

## Problem Statement

In this challenge, the task is to debug the existing code to successfully execute all provided test files.
________________________________________________________________________________________

The given code defines two classes `HotelRoom` and `HotelApartment` denoting respectively a standard hotel room and a hotel apartment. An instance of any of these classes has two parameters: `bedrooms` and `bathrooms` denoting respectively the number of bedrooms and the number of bathrooms in the room.

The prices of a standard hotel room and hotel apartment are given as: 

- Hotel Room: $50 \cdot bedrooms$ + $100 \cdot bathrooms$.
- Hotel Apartment: The price of a standard room with the same number bedrooms and bathrooms plus $100$. 

For example, if a standard room costs $200$, then an apartment with the same number of bedrooms and bathrooms costs $300$.

In hotel's codebase, there is a piece of code reading the list of rooms booked for today and calculates the total profit for the hotel. However, sometimes calculated profits are lower than they should be.

Debug the existing `HotelRoom` and `HotelApartment` classes' implementations so that the existing code computing the total profit returns a correct profit.

Your function will be tested against several cases by the locked template code.

## Input Format

The input is read by the provided locked code template.  

In the first line, there is a single integer $n$ denoting the number of rooms booked for today.  

After that $n$ lines follow. Each of these lines begins with a `room_type` which is either `standard` or `apartment`, and is followed by the number of bedrooms and the number of bathrooms in this room.

## Output Format

The output is produced by the provided and locked code template. It calculates the total profit by iterating through the vector of all rooms read from the input.

## Constraints

- $1 \leq n \leq 100$
- There is at least $1$ and at most $5$ bedrooms in a room
- There is at least $1$ and at most $5$ bathrooms in a room

## Sample Tests

### Test 1

```
2
standard 3 1
apartment 1 1
```

### Test 2

```
500
```
