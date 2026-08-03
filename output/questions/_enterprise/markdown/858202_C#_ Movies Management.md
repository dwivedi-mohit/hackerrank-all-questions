# C#: Movies Management

## Metadata

- **ID:** 858202
- **Type:** code
- **Difficulty:** 7.5
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** C#, LINQ, Easy
- **Skills:** C# (Basic)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates LINQ, C# methods, and data management concepts, ideal for junior-level roles. The problem requires implementing methods to analyze movie ratings and genres using LINQ in a class structure.

## Problem Statement

Implement four methods using LINQ in a class that manages movie data:

	
- 
HighestRating - returns the highest rating in the movie list
	
- 
LowestRating - returns the lowest rating in the movie list
	
- 
AverageRating - returns the average rating of all movies in the list, rounded to the nearest whole number
	
- 
HighestRatingForEachGenre - calculates the highest rating for each unique genre and returns the results as a Dictionary<string, Movie> sorted by key, where Key[string] is a unique genre, and Value[Movie] is the movie with the highest rating in this genre

The Movie class has these properties:

	
- 
Title [string] - the title of the movie
	
- 
Genre [string] - the genre of the movie
	
- 
Rating [int] - the rating of the movie

Your implementation will be tested by stubbed code on several input files. The input file contains parameters for function calls. The functions will be called with those parameters, and their execution results will be printed to the standard output.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains an integer, n, denoting the number of movies on which operations have to be performed.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains space-separated strings, such that the first of them is the movie title, the second is the genre, and the third is the rating of the movie, respectively.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

12
The_Godfather Action 96
The_Dark_Knight Drama 24
Cleopatra Comedy 61
Sabotage Action 88
Inception Drama 86
The_Matrix Comedy 14
Life_is_Beautiful Drama 19
City_of_God Horror 12
Raven Comedy 30
Breaking_Wind Comedy 59
City_Lights Documentary 46
Born_Wild Drama 55
```

Sample Output

Highest rating is 96
Lowest rating is 12
Average rating is 49
The highest rating for genre Action is 96. Movie's title is The_Godfather
The highest rating for genre Comedy is 61. Movie's title is Cleopatra
The highest rating for genre Documentary is 46. Movie's title is City_Lights
The highest rating for genre Drama is 86. Movie's title is Inception
The highest rating for genre Horror is 12. Movie's title is City_of_God

```

Explanation

Here, 12 movies are presented with their details (title, genre, and rating). Then, based on that data, the 4 methods are called: HighestRating, LowestRating, AverageRating, and HighestRatingForEachGenre. The result obtained from these 4 function calls is printed to the standard output.

Sample Case 1

Sample Input For Custom Testing

12
The_Godfather Drama 41
The_Referee Comedy 92
Black_Swan Drama 34
Sabotage Drama 53
The_Hunters Adventure 76
Inception Comedy 54
Life_is_Beautiful Drama 46
Human_Bondage Drama 26
Raven Documentary 90
City_of_God Documentary 79
Son Drama 63
Born_Wild Comedy 44

```

Sample Output

Highest rating is 92
Lowest rating is 26
Average rating is 58
The highest rating for genre Adventure is 76. Movie's title is The_Hunters
The highest rating for genre Comedy is 92. Movie's title is The_Referee
The highest rating for genre Documentary is 90. Movie's title is Raven
The highest rating for genre Drama is 63. Movie's title is Son

```

Explanation

Here, 12 movies are presented with their details (title, genre, and rating). Then, based on that data, the 4 methods are called: HighestRating, LowestRating, AverageRating, and HighestRatingForEachGenre. The result obtained from these 4 function calls is printed to the standard output.

## Sample Input/Output

## Preview

Implement four methods using LINQ in a class that manages movie data:
