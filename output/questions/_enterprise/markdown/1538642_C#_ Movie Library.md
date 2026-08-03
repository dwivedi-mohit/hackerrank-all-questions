# C#: Movie Library

## Metadata

- **ID:** 1538642
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Coding, Inheritance, Easy, Interfaces, C#
- **Skills:** C# (Basic)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates C#, inheritance, and interfaces concepts, ideal for junior-level roles. The problem requires implementing classes for managing a movie library, including methods for adding, removing, and searching films.

## Problem Statement

A movie library application is being developed with methods to manage movie listings, including adding movies, removing movies, and searching for movies.

 

Create a new class called Film and implement the IFilm interface.

	
- Inside the Film class, define the following properties:

	
		
- 
Title (string): the title of the film
		
- 
Director (string): the director of the film
		
- 
Year (integer): the year the film was released
	
	

 

Create another class called FilmLibrary and implement the IFilmLibrary interface.

	
- Inside the FilmLibrary class, declare a private field called _films of type List<IFilm> to store the films.
	
- Add the following methods to the FilmLibrary class:
	
		
- 
AddFilm(IFilm film): adds a film to the film library. It takes an IFilm object as a parameter and adds it to the _films list
		
- 
RemoveFilm(string title): removes a film from the film library based on its title if it is in the _films

		
- 
GetFilms(): returns a list of all films in the film library
		
- 
SearchFilms(string query): searches for films in the film library based on a query string. It returns a list of films whose title or director contains the query
		
- 
GetTotalFilmCount(): returns the total number of films in the film library
	
	

 

Example

There are 2 Film objects, with Title Director Year:

HarryPotter DavidYates 2007

TheLordOfTheRings PeterJackson 2001

 

Add them to the list and determine the word to search from the movie list.

DavidYates

 

Finally, select the movie to be removed from the movie list.

TheLordOfTheRings

 

Output:

Total Film Count: 2

Search Results for DavidYates:

HarryPotter (DavidYates, 2007)

Removed Film: TheLordOfTheRings (PeterJackson, 2001)

All Films:

HarryPotter (DavidYates, 2007)

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer n, the number of films.

Each of the next n lines contains the films separated by space (Title Director Year.).

The next line contains the string m, which is the films to group.

Each of the next m lines contains the Director (Director).

The next line contains the string m, which is the movie to be deleted.

Each of the next m lines contains the Title (Title).

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

A movie library application is being developed with methods to manage movie li
