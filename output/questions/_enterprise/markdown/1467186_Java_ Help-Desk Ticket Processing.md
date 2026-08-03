# Java: Help-Desk Ticket Processing

## Metadata

- **ID:** 1467186
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Java, Inheritance, Hard, Classes, Interfaces
- **Skills:** Java (Advanced)
- **Languages:** j, a, v, a, 1, 5, ,, j, a, v

## Summary

This coding question evaluates Java, inheritance, and class design concepts, ideal for senior-level roles. The problem requires implementing a help desk ticketing system with specific classes and methods to manage employee tickets and their completion status.

## Problem Statement

Implement a help desk ticketing system to manage help requests and support personnel. Help requests are categorized, and personnel respond according to their point levels.

 

Available categories (enum structure):

	
- InformationTechnologies
	
- HumanResources
	
- Accounting
	
- Sales
	
- Marketing
	
- Legal

Implement the following classes:

	
- 
Employee class

	
		
- Properties: FullName (string), PointLevel (int), AssignedCategories (List)

		
- Constructor to initialize all properties
	
	
	
- 
Ticket class
	
		
- Properties: Id (int), Name (string), Category (Category), Point (int), AssignedEmployee (string), IsCompleted (bool)
		
- The constructor initializes the first 4 properties
	
	
	
- 
HelpDesk class
	
		
- Properties: Employees (List), Tickets (List)

		
- Methods:
		
			
- 
AddTicket: Add a ticket to the Tickets list
			
- 
AddEmployee: Add an employee to the Employees list
			
- 
CompleteTicket: Mark a ticket as completed if conditions are met
			
- 
GetWaitingTicketCount: Return the count of incomplete tickets
			
- 
GetCompletedTicketsTotalPoint: Return sum of points for completed tickets
			
- 
GetTicketsTotalPointByCategory: Return list of (category, total points) tuples
			
- 
GetTicketsTotalPointByEmployee: Return list of (employee name, total points) tuples
		
		
	
	

Example

Employees:

	
- John Doe (point level 2)
	
- Jane Roe (point level 5)

Tickets:

	
- InformationTechnologies, 3 points
	
- HumanResources, 1 point
	
- Legal, 3 points
	
- Sales, 10 points
	
- InformationTechnologies, 1 point

Queries:

	
- John Doe, Ticket 1: Not completed (point level too low)
	
- John Doe, Ticket 2: Completed
	
- Jane Roe, Ticket 3: Completed
	
- John Doe, Ticket 5: Completed

Output:

WaitingTicketCount:2
CompletedTicketsTotalPoint:5
TicketsTotalPointByCategory:
InformationTechnologies:4
HumanResources:1
Accounting:0
Sales:10
Marketing:0
Legal:3
TicketsTotalPointByEmployee:
John Doe:2
Jane Roe:3

```

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of employees.

Each of the next n lines contains the employee information (FullName, PointLevel, AssignedCategories).

The next line contains an integer m, the number of tickets.

Each of the next m lines contains the ticket information (Id, Name, Category, Point).

The next line contains an integer k, the number of CompleteTicket calls.

Each of the next k lines contains the process for ticket completion (Employee FullName, Ticket Id).

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

`2
John Doe,1,HumanResources InformationTechnologies
Jane Cherry,6,Legal InformationTechnologies
3
1,Ticket1,InformationTechnologies,1
2,Ticket2,HumanResources,5
3,Ticket3,Legal,2
4
John Doe,3
John Doe,1
Jane Cherry,2
Jane Cherry,3`
```

Sample Output

`WaitingTicketCount:1
CompletedTicketsTotalPoint:3
TicketsTotalPointByCategory:
InformationTechnologies:1
HumanResources:5
Accounting:0
Sales:0
Marketing:0
Legal:2
TicketsTotalPointByEmployee:
John Doe:1
Jane Cherry:2`
```

Explanation

John Doe,1,Legal Sales -> Employee full name, PointLevel, and AssignedCategories, comma-separated. The categories are separated by a space.

2,Ticket1,HumanResources,7 -> Ticket Id, name, category, and points separated by a comma.

John Doe,4 -> Employee full name and ticket id separated by a comma.

There are 2 employees and 3 tickets.

	
- John Doe is shown tickets 3 and 1. Ticket 3 is for Legal, and he does not cover that department. Ticket1 is from a department he covers, and he has enough points.
	
- Jane Cherry sees tickets 2 and 3. Ticket2 is for HumanResources, and she does not cover that department. Ticket3 is from Legal, a department she covers, and she has enough points.
	
- Ticket2 remains unaddressed.

Sample Case 1

Sample Input For Custom Testing

`2
John Doe,9,Accounting Marketing
Jane Cherry,5,Accounting Sales
3
1,Ticket1,Accounting,5
2,Ticket2,HumanResources,9
3,Ticket3,Accounting,4
4
John Doe,2
John Doe,3
Jane Cherry,1
Jane Cherry,1`
```

Sample Output

`WaitingTicketCount:1
CompletedTicketsTotalPoint:9
TicketsTotalPointByCategory:
InformationTechnologies:0
HumanResources:9
Accounting:9
Sales:0
Marketing:0
Legal:0
TicketsTotalPointByEmployee:
John Doe:4
Jane Cherry:5`
```

Explanation

	
- John Doe handles Ticket3 because he has enough points and covers that department.
	
- Jane Cherry handles Ticket1. It was reopened, and she handled it again, but only received points for the first time.
	
- Ticket2 is waiting.

## Sample Input/Output

## Preview

Implement a help desk ticketing system to manage help requests and support per
