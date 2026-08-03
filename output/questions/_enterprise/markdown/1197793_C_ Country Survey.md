# C: Country Survey

## Metadata

- **ID:** 1197793
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Structures, Arrays, Hard, Functions, Union
- **Skills:** C (Advanced)
- **Languages:** c

## Summary

This coding question evaluates data structures, arrays, and functions concepts, ideal for senior-level roles. The problem requires implementing query functions to analyze census data based on age, city, and salary criteria.

## Problem Statement

Implement three query functions to analyze census data:

	
- 
Age_More_than_k

	
		
- Input: Information about individuals, total number of people, age threshold k

		
- Output: Number of people older than k

	
	
	
- 
Persons_from_city_c
	
		
- Input: Information about individuals, total number of people, city c

		
- Output: Number of people who reside in city c

	
	
	
- 
Salary_between
	
		
- Input: Information about individuals, total number of people, minimum salary, maximum salary
		
- Output: Number of people earning within the salary range [minimum, maximum]

	
	

 

Constraints

	
- 1 ≤ n ≤ 100
	
- 1 ≤ q ≤10
	
- 2 ≤ |city| ≤ 50
	
- 1 ≤ age ≤ 100
	
- 1 ≤ salary ≤ 105
	
- 1 ≤ |name| ≤ 50

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

 

The first line contains two space-separated integers n (the number of people) and q (the number of queries).

The second line contains the n space-separated strings which are the people's names.

The third line contains n space-separated integers which are the people's ages.

The fourth line consists of n space-separated strings which are the cities that the people belong to.

The fifth line consists of n space-separated integers which are the people's salaries.

The next q lines represent the government's queries.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

1 1      
Tourist  
18
AB
10000
1 19
```

Sample Output

0
```

Explanation

There is nobody older than 19 years.

Sample Case 1

Sample Input For Custom Testing

2 3
Leo Eve
20 21
ABC DEF 
50000 60000
1 20
2 DEF
3 40000 50000
```

Sample Output

1 1 1
```

Explanation

Only one person, Eve, is older than 20.

Only one person, Eve, lives in DEF.

Only one person, Leo, has a salary between 40,000 and 50,000.

## Sample Input/Output

## Preview

Implement three query functions to analyze census data:
