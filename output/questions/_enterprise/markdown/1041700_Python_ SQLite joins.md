# Python: SQLite joins

## Metadata

- **ID:** 1041700
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Python, Hard, Database
- **Skills:** Python (Advanced)
- **Languages:** p, y, t, h, o, n, 3

## Summary

This coding question evaluates SQL joins, filtering, and sorting concepts, ideal for senior-level roles. The problem requires writing a function to join two tables based on city, filter results, and sort them accordingly.

## Problem Statement

Given a SQLite database with two tables, User and Restaurants, write a function joinUsersAndRestaurants that joins these tables based on the city field. The function should:

	
- Filter the results by the specified city
	
- Order them either in ascending or descending order
	
- Apply sorting first to User.username and then to Restaurants.restaurant_name

	
- Include only the User.username and Restaurants.restaurant_name fields in the output

 

Users
username: text
city: text

```

 

Restaurants
restaurant_name: text
city: text

```

 

Given the following records,

{"username": "charlie", city: "london"}
{"username": "avery", city: "tokyo"}
{"username": "alex", city: "tokyo"}

{"name": "fancy fries", city: "london"}
{"name": "supehero", city: "tokyo"}
{"name": "green light", city: "tokyo"}

joinUsersAndRestaurants(cursor, city="tokyo", order="asc") returns

[
    ("alex", "green light"),
    ("alex" "superhero"),
    ("avery", "green light"),
    ("avery", "superhero")
]

```

 

Constraints

	
- It is guaranteed that all username and restaurant_name values are unique.
	
- It is guaranteed that the output will have at least one element.

 

Function Description 

Complete the function joinUsersAndRestaurants in the editor with the following parameter(s):

    sqlite3.Cursor cursor: an SQLite connection cursor

    string city: the city to filter to

    string order: there required order

 

Returns

    tuple[n]: list of tuples that the joined records that match the function's parameters in the specified order.

 

Constraints

	
- The city parameter contains only lowercase English letters.
	
- The order parameter is either 'asc' or 'desc'.

 

 DO NOT REMOVE THIS LINE-->

Input Format Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.

 

In the first line, there is an integer n, the number of records to prefill the users table with.

Then, n lines follow. The i-th of them contains 2 space-separated values: username, and city that denote a single record to prefill the Users table with.

In the next line, there is an integer m, the number of records to prefill the restaurants table with.

Then, m lines follow. The ith of them contains 2 space-separated values: restaurant_name, and city that make up a single record to prefill the Restaurant table with.

In the next line, there are two space-separated strings, the city, and order parameters to be passed to the joinUsersAndRestaurants function.

 

Sample Case 0

Sample Input 0

STDIN                 Function
-----                 --------
4                →    number of records in the Users table
alex london      →    first (name, city) pair
charlie london   →    ...
avery moscow
billie tokyo 
3                →    number of records in the Restaurant table
icewind london   →    first (restaurant, city) pair
blueglass moscow →    ...
redwine london
london desc

```

 

Sample Output 0

charlie redwine
charlie icewind
alex redwine
alex icewind

```

 

Explanation 0

The database is prefilled with 4 user records and 3 restaurant records. The parameters for the select function are city="london", order="desc", so the results must be the usernames with city "london" joined with restaurant_names with city "london" in descending order. The list of matching tuples in the specified order is [("charlie", "redwine"), ("charlie", "icewind"), ("alex redwine"), ("alex", "icewind")].

 

Sample Case 1

Sample Input 1

4 
alex london 
charlie london 
avery moscow 
billie tokyo
4
heaven london
blueglass moscow
redwine london
century moscow 
moscow asc

```

 

Sample Output 1

avery blueglass
avery century

```

 

Explanation 1

The database is prefilled with 4 user records and 4 restaurant records. The parameters for the select function are city="moscow", order="asc", so the results must be the usernames with city "moscow" joined with restaurant_names with city "moscow" in ascending order. The list of matching tuples in the specified order is [("avery", "blueglass"), ("avery", "century")].

## Sample Input/Output

## Preview

Given a SQLite database with two tables, User and Restaurants, write a functio
