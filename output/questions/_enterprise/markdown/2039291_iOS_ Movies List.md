# iOS: Movies List

## Metadata

- **ID:** 2039291
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Pagination, Data Sorting, Data Filtering, iOS, Swift, Easy, UIkit
- **Skills:** iOS (Basic)

## Summary

This mobile development question evaluates pagination, data sorting, and data filtering concepts, ideal for junior-level roles. The problem requires creating a movie listing application that fetches data, implements sorting and filtering, and handles pagination.

## Problem Statement

Create a movie listing application as shown below. The application requirements are listed below, and the finished application must pass the unit tests.

Hide animation Show animation

Functionality Requirements

Complete the implementation of the app according to the following requirements:

	
- To access the list of movies, perform an HTTP GET request using the built-in fetch library to https://jsonmock.hackerrank.com/api/moviesdata.
	
- The response to such a request is a JSON with the following fields:
	
		
- 
page: The current page of the results.
		
- 
per_page: The maximum number of records returned per page.
		
- 
total: The total number of records in the database.
		
- 
total_pages: The total number of pages with results.
		
- 
data: An array of movie objects. Each object has the following schema:
		
			
- 
Title: movie name [STRING]
			
- 
Year: the movie's release year [INTEGER]
			
- 
imdbID: the IMDB ID [STRING]
		
		
	
	
	
- When the data is loading, the ActivityIndicator component should be rendered.
	
- Once the data is successfully loaded, remove the indicator and display the Header and UITableView.
	
- The UITableView takes an array of movies as a prop. Each element of this array denotes a single movie and is in the shape mentioned above.
	
- In the UITableView, use the UITableView component of iOS to render a list of movies. Each movie in the array must be rendered as a UITableViewCell component.
	
- Complete the UITableViewCell component by providing the title, year, and imdbID of each movie.
	
- In the search bar, filter the movie list based on movie names.
	
- Enable sorting of movies by name or year in ascending or descending order upon tapping the sort button.
	
- In the sorting container:
	
		
- 
Sort By: Display options to sort movies by name or release year.
		
- 
Order: Display options to sort data in ascending or descending order.
		
- 
Clear Sort: Remove sorting.
	
	
	
- Implement pagination to load more movies when scrolling down to the last page of results.

Testing Requirements

Initially, the file is filled with boilerplate code. Note the following:

	
- Each movie item must have accessibilityIdentifier="movies-item".
	
- Each movie name must be rendered as a UILabel element with accessibilityIdentifier="name".
	
- Each movie year must be rendered as a UILabel element with accessibilityIdentifier="year".
	
- Each movie imdbID must be rendered as a UILabel element with accessibilityIdentifier="imdb".
	
- The SearchInput must be rendered as a UISearchBar element with accessibilityIdentifier="search-input".
	
- MovieList must be rendered as a UITableView element with accessibilityIdentifier="movie-list".
	
- The header must be rendered as a UILabel element with accessibilityIdentifier="header-title".
	
- In the MovieList component, the RenderFooter ActivityIndicator must be rendered as an ActivityIndicator element with accessibilityIdentifier="load-more-progress".
	
- In the Sort Container, the sort button must be rendered as a UIButton element with accessibilityIdentifier="sortToggleButton".
	
- In the Sort Container, the sort order must be rendered as a UIButton element with accessibilityIdentifier="orderToggleButton".
	
- In the Sort Container, the clear sort must be rendered as a UIButton element with accessibilityIdentifier="clearSortButton".

The component has these testID attributes for test cases and certain classes and IDs for rendering purposes. They should not be changed.

## Preview

Create a movie listing application as shown below. The application requirement
