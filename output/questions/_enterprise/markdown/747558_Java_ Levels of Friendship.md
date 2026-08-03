# Java: Levels of Friendship

## Metadata

- **ID:** 747558
- **Type:** code
- **Difficulty:** 7.222222222222222
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, OOPS, Easy, OOP
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates object-oriented programming, class inheritance, and method overriding concepts, ideal for junior-level roles. The task requires implementing a hierarchy of friendship levels using Java classes.

## Problem Statement

This task involves defining different levels of friendship using Java classes.

 

The friendship levels are organized hierarchically:

	
- 
Acquaintance: Someone you know slightly but not closely.
	
- 
Friend: Someone you have a strong bond with.
	
- 
Best Friend: Your closest friend.

As the levels of friendship increase, you learn more about the person. Based on the knowledge you have about someone: Best Friend > Friend > Acquaintance.

 

Implement these levels using three Java classes:

Class Acquaintance:

	
- Attribute: name (String type)
	
- Constructor: Acquaintance(String name)

	
- Method: public void getStatus(), which prints "[name] is just an acquaintance."

Class Friend:

	
- Inherits from Acquaintance

	
- Constructor: Friend(String name, String homeTown)

	
- Attribute: homeTown (String type)
	
- Method: public void getStatus(), which prints "[name] is a friend and he is from [homeTown]."

Class BestFriend:

	
- Inherits from Friend

	
- Constructor: BestFriend(String name, String homeTown, String favoriteSong)

	
- Attribute: favoriteSong (String type)
	
- Method: public void getStatus(), which prints "[name] is my best friend. He is from [homeTown] and his favorite song is [favoriteSong]."

Note: Input handling is not required as the code stub takes care of it.

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of friends

Each line i of the n subsequent lines (where 0 < i < n) contains data for a friend in differing formats based on level:

	
- Acquaintance FriendName

	
- Friend FriendName HomeTown

	
- BestFriend FriendName HomeTown FavoriteSong

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

4
Acquaintance Jaden
Friend Jake Florida
BestFriend Ryan Utah Dangerous
Friend David Texas
```

Sample Output

Jaden is just an acquaintance.
Jake is a friend and he is from Florida.
Ryan is my best friend. He is from Utah and his favorite song is Dangerous.
David is a friend and he is from Texas.

```

Sample Case 1

Sample Input

5
Acquaintance Roger
BestFriend Carson Boston Believer
Friend Oren Atlanta
BestFriend Ramon Miami Radioactive
Friend Tyson Denver
```

Sample Output

Roger is just an acquaintance.
Carson is my best friend. He is from Boston and his favorite song is Believer.
Oren is a friend and he is from Atlanta.
Ramon is my best friend. He is from Miami and his favorite song is Radioactive.
Tyson is a friend and he is from Denver.

```

## Sample Input/Output

## Preview

This task involves defining different levels of friendship using Java classes.
