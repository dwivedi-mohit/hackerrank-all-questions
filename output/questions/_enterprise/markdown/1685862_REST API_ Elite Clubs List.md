# REST API: Elite Clubs List

## Metadata

- **ID:** 1685862
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** REST API, Medium, JSON
- **Skills:** REST API (Intermediate)
- **Languages:** c, p, p, ,, c, s, h, a, r, p

## Summary

This coding question evaluates REST API, data processing, and sorting concepts, ideal for mid-level roles. The problem requires gathering elite football clubs from a paginated API based on valuation and league titles won, then sorting the results accordingly.

## Problem Statement

Gather a list of elite football clubs in a specific nation by accessing a database via HTTP GET requests. The database is available at the URL https://jsonmock.hackerrank.com/api/football_teams?nation={nation_name}, where {nation_name} is the nation to search.

 

The database is paginated and can be accessed by appending &page={num} to the URL, where {num} is the page number.

 

The query response includes these fields:

	
- 
page: current page
	
- 
per_page: maximum results per page
	
- 
total: total number of records
	
- 
total_pages: total number of pages
	
- 
data: array of club information

Each object in the data array contains:

	
- 
name: club name
	
- 
nation: club's nation
	
- 
estimated_value_numeric: club's monetary value
	
- 
number_of_league_titles_won: number of league titles won
	
- other details not relevant to this task

 

For example, the record for Arsenal FC is:

{
  "name": "Arsenal FC",
  "captain": "Pierre-Emerick Aubameyang",
  "vice_captain": "Alexandre Lacazette",
  "goalkeeper": "Bernd Leno",
  "number_of_players": 25,
  "current_active_players": 22,
  "league": "English Premier League (EPL)",
  "nation": "England",
  "estimated_value": "$2 billion",
  "estimated_value_numeric": 2000000000,
  "number_of_league_titles_won": 13,
  "last_league_title_winning_year": 2003,
  "number_of_champions_league_won": 0,
  "last_champions_league_winning_year": null,
  "total_silverware_count": 30,
  "manager": "Mikel Arteta",
  "stadium_name": "Emirates Stadium",
  "stadium_capacity": 60355,
  "league_position_2021": 5,
  "league_top_three_finishes": 18,
  "number_of_runner_ups_in_champions_league": 0,
  "highest_goalscorer": "Thierry Henry",
  "highest_assist_provider": "Thierry Henry",
  "highest_clean_sheet_holder": "David Seaman",
  "most_capped_player": "Tony Adams",
  "appearances_most_capped_player": 669
}

```

Given a minimum valuation and minimum number of league titles, return an array of elite clubs in the specified nation. Sort the array in decreasing order of value. If multiple clubs have the same valuation, sort them in ascending alphabetical order.

 

Function Description

Complete the function eliteClubs in the editor with the following parameter(s):

   string nation: the nation's name

   int minValuation: the minimum valuation required to be considered an elite club

   int minTitlesWon: the minimum number of league titles won to be considered an elite club

 

Returns

    string[]: the name(s) of all the elite clubs in the nation

 

Note: Please review the header in the code stub to see available libraries for API requests in the selected language. Required libraries can be imported to solve the question. Check our full list of supported libraries at https://www.hackerrank.com/environment.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The first line contains a string, nation.

The second line contains an integer, minValuation.

The third line contains an integer, minTitlesWon.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

England
823472
2

```

Sample Output

Manchester United FC
Chelsea FC
Manchester City FC
Liverpool FC
Arsenal FC
Tottenham Hotspur FC
Everton FC
Wolverhampton Wanderers FC
Aston Villa FC
Burnley FC
Leeds United FC
Newcastle United FC
Fulham FC
Blackburn Rovers FC
Derby County FC
Birmingham City FC
Queens Park Rangers FC
Huddersfield Town AFC
Coventry City FC
Preston North End FC
Hull City AFC
Luton Town FC
Bolton Wanderers
Charlton Athletic

```

Explanation

There are 24 clubs with a minimum valuation of 823472 and a minimum of 2 league titles won in England.

 

Sample Case 1

Sample Input For Custom Testing

Wales
660905
1

```

Sample Output

Cardiff City FC

```

Explanation

Only Cardiff City FC meets the criteria for valuation (at least 660905) and titles won (at least 1) to be considered an elite club in Wales.

## Sample Input/Output

## Preview

Gather a list of elite football clubs in a specific nation by accessing a data
