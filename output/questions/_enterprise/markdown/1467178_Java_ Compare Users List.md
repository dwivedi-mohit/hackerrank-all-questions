# Java: Compare Users List

## Metadata

- **ID:** 1467178
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Arrays, Reflection, Medium, Java
- **Skills:** Java (Intermediate)
- **Languages:** j, a, v, a, 1, 5, ,, j, a, v

## Summary

This coding question evaluates arrays, reflection, and Java concepts, ideal for mid-level roles. The problem requires implementing a function to compare user records and determine which users need to be updated or inserted in a database.

## Problem Statement

Implement the backend side of a user management page for a company administrative portal. The admin can add new users, update current users, and save all changes by pressing the save button.

 

Given two user lists, one from the current database and another with possible changes:

	
- If the first value in a change record is 0, it is a new user to insert into the database.
	
- If the value is greater than 0, it is a user ID; compare all user attributes with what is in the database and update if there is any difference.

The implementation should return a two-dimensional list:

	
- First element: A list of records to update
	
- Second element: A list of records to insert

 

Example

Current users in the database, usersListInDB:

	
- 1 User1
	
- 2 User2

Users List from UI, newUsersList:

	
- 1 User4
	
- 0 User5
	
- 2 User2

User ID 1 changes username from 'User1' to 'User4'. The second line has user ID 0, creating a new user with username 'User5'. User ID 2 matches the database, so no changes are made.

 

Return two lists, the updated and added users: [['1 User1'] , ['0 User5']].

 

Function Description

Implement the CompareUsers function with the following parameters:

    List<User> usersListInDB: the current database

    List<User> newUsersList: the new transactions

 

Return

    List<User>[2]: [[updated], [inserted]]

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the count of users in the database.

Each of the next n lines contains the comma-separated user information of one user.

The next line contains an integer m, the number of users to compare.

Each of the next m lines contains the comma-separated user information to process.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

4
1,0,First0,Last0,40,1993.05.23,email0@gmail.com,Male,Country0,City0,Address0,ZipCode0,PhoneNumber0,Department0,Role0,2016.07.18,656,Active
2,7984,First1,Last1,50,1997.01.05,email1@gmail.com,Female,Country1,City1,Address1,ZipCode1,PhoneNumber1,Department1,Role1,2018.10.08,778,Inactive
3,5968,First2,Last2,0,1999.03.20,email2@gmail.com,Male,Country2,City2,Address2,ZipCode2,PhoneNumber2,Department2,Role2,2019.10.16,734,Active
4,3952,First3,Last3,10,1989.04.02,email3@gmail.com,Female,Country3,City3,Address3,ZipCode3,PhoneNumber3,Department3,Role3,2016.11.05,858,Inactive
2
1,0,First0,Last0,40,1993.05.09,email0@gmail.com,Male,Country0,City0,Address0,ZipCode0,PhoneNumber0,Department0,Role0,2017.02.24,176,Active
2,7984,First1,Last1,50,1997.01.05,email1@gmail.com,Female,Country1,City1,Address1,ZipCode1,PhoneNumber1,Department1,Role1,2018.10.08,778,Inactive

```

Sample Output

Updated Users:1
Inserted Users:0

```

Explanation

There are 4 users in the database initially, and there are 2 users to compare.

	
- The date value "1993.05.23" is updated to "1993.05.09" in the first line. Add the record to the updated list.
	
- The user in the second line matches the user in the database, so no update or insertion occurs.

Sample Case 1

Sample Input For Custom Testing

4
1,0,First0,Last0,40,2019.01.26,email0@gmail.com,Male,Country0,City0,Address0,ZipCode0,PhoneNumber0,Department0,Role0,2018.11.01,637,Active
2,7984,First1,Last1,50,1996.08.22,email1@gmail.com,Female,Country1,City1,Address1,ZipCode1,PhoneNumber1,Department1,Role1,2015.02.14,846,Inactive
3,5968,First2,Last2,0,1989.08.24,email2@gmail.com,Male,Country2,City2,Address2,ZipCode2,PhoneNumber2,Department2,Role2,2016.09.17,508,Active
4,3952,First3,Last3,10,1994.07.14,email3@gmail.com,Female,Country3,City3,Address3,ZipCode3,PhoneNumber3,Department3,Role3,2021.07.02,974,Inactive
2
0,0,First0,Last0,40,2003.01.07,email0@gmail.com,Male,Country0,City0,Address0,ZipCode0,PhoneNumber0,Department0,Role0,2015.01.11,989,Active
0,9760,First15,Last15,10,1996.04.11,email15@gmail.com,Female,Country15,City15,Address15,ZipCode15,PhoneNumber15,Department15,Role15,2017.01.13,606,Inactive

```

Sample Output

Updated Users:0
Inserted Users:2

```

Explanation

 

The two zero ID user records are inserted. Add both to the inserted list.

## Sample Input/Output

## Preview

Implement the backend side of a user management page for a company administrat
