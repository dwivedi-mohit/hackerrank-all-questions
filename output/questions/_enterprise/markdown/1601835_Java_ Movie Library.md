# Java: Movie Library

## Metadata

- **ID:** 1601835
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Coding, Java, Inheritance, Easy, Interfaces
- **Skills:** Java (Basic)
- **Languages:** j, a, v, a, ,, j, a, v, a, 1

## Summary

This coding question evaluates Java, inheritance, and interfaces concepts, ideal for junior-level roles. The problem requires implementing a movie library application with functionalities to add, remove, and search for films using specified classes and interfaces.

## Problem Statement

Implement a movie library application with functionality to add, remove, and search for movies.

 

Create a Film class implementing the IFilm interface with these properties:

	
- 
title (String): the movie title
	
- 
director (String): the movie director
	
- 
year (int): the release year

Create a FilmLibrary class implementing the IFilmLibrary interface with these methods:

	
- 
addFilm(IFilm film): adds a film to the library
	
- 
removeFilm(String title): removes a film by title if present
	
- 
getFilms(): returns a list of all films in the library
	
- 
searchFilms(String query): returns films whose title or director contains the query
	
- 
getTotalFilmCount(): returns the total number of films in the library

 

Example

Given 2 Film objects:

	
- "HarryPotter", "DavidYates", 2007
	
- "TheLordOfTheRings", "PeterJackson", 2001

After adding both films to the library, searching for "DavidYates", and removing "TheLordOfTheRings", the output is:

Total Film Count: 2
Search Results for DavidYates:
HarryPotter (DavidYates, 2007)
Removed Film: TheLordOfTheRings (PeterJackson, 2001)
All Films:
HarryPotter (DavidYates, 2007)

```

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of films.

Each of the next n lines contains the film information separated by single spaces (Title Director Year).

The next line contains a string, the Title or Director to search.

The next line contains a string, the Title to delete.

 DO NOT REMOVE THIS LINE-->

Sample Case 1

Sample Input For Custom Testing

STDIN                    Function
-----                    --------
4                        number of films n = 4
Film-1 Director-2 2004   first film Title = 'Film-1', Director = 'Director-2', 'Year' = 2004
Film-2 Director-1 2018   second film...
Film-3 Director-1 2001
Film-4 Director-3 2017
Director-1               Title or Director to search for = 'Director-1'
Film-1                   Title to delete = 'Film-1'

```

Sample Output

Total Film Count: 4
Search Results for Director-1:
Film-2 (Director-1, 2018)
Film-3 (Director-1, 2001)
Removed Film: Film-1 (Director-2, 2004)
All Films:
Film-2 (Director-1, 2018)
Film-3 (Director-1, 2001)
Film-4 (Director-3, 2017)

```

Explanation

There are 4 films to add. The code stub reads the data, makes the method calls, and generates results.

Sample Case 2

Sample Input For Custom Testing

4
Film-1 Director-4 2014
Film-2 Director-3 2016
Film-3 Director-4 2012
Film-4 Director-3 2003
Director-3
Film-4

```

Sample Output

Total Film Count: 4
Search Results for Director-3:
Film-2 (Director-3, 2016)
Film-4 (Director-3, 2003)
Removed Film: Film-4 (Director-3, 2003)
All Films:
Film-1 (Director-4, 2014)
Film-2 (Director-3, 2016)
Film-3 (Director-4, 2012)

```

Explanation

There are 4 films to add. The code stub reads the data, makes the method calls, and generates results.

## Sample Input/Output

## Preview

Implement a movie library application with functionality to add, remove, and s
