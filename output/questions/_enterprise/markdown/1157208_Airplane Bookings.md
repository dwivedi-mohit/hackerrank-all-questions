# Airplane Bookings

## Metadata

- **ID:** 1157208
- **Type:** database
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Windowing, SQL, Aggregation, Hard, Database, Interviewer Guidelines
- **Skills:** SQL (Advanced)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, windowing functions, and aggregation concepts, ideal for senior-level roles. The problem requires calculating the average number of empty seats for airlines and identifying airplanes closest to this average.

## Problem Statement

You are provided with data of airplane bookings which contain total seats in an airplane and the bookings done. Every airplane has some seats that are not booked. Find out the average number of seats that go without booking for every airline and fetch the airplanes for each airline whose number of empty seats is closest to the average number of seats that remain empty.

 

In case there are more than one airplane with same number of empty seats fetch them in order of airplane_id separated by comma. Also order the result by airline_id.

 

Schema

You are provided 2 tables: `airlines_detail`, `bookings`.

	
		
			airlines_detail
		
		
			Name
			Type
			Description
		
		
			airplane_id
			int
			Unique id of the airplane.
		
		
			airline_id
			int
			Unique id of the airline that owns airplane.
		
		
			total_seats
			int
			Total number of seats available to book.
		
	

	
		
			bookings
		
		
			Name
			Type
			Description
		
		
			airplane_id
			int
			Id of the airplane referring to airlines_detail table.
		
		
			booked
			int
			Number of seats booked in a timeperiod.
		
	

Sample Data Tables

	
		
			airlines_detail
		
		
			airplane_id
			airline_id
			total_seats
		
		
			2187
			425
			260
		
		
			4361
			747
			290
		
		
			3478
			747
			270
		
		
			7292
			425
			250
		
		
			5833
			425
			310
		
		
			3472
			425
			300
		
		
			4472
			747
			290
		
		
			2624
			425
			320
		
	

	
		
			bookings
		
		
			airplane_id
			booked
		
		
			2187
			40
		
		
			4361
			30
		
		
			4361
			10
		
		
			5833
			30
		
		
			4361
			30
		
		
			2624
			30
		
		
			4472
			40
		
		
			4472
			40
		
		
			2624
			10
		
		
			7292
			20
		
		
			2187
			20
		
		
			4472
			30
		
		
			3478
			20
		
		
			3472
			40
		
		
			4472
			30
		
		
			4472
			10
		
		
			4361
			20
		
		
			3478
			30
		
		
			2187
			30
		
		
			2187
			10
		
	

 

	
		
			OUTPUT
		
		
			airline_id
			airplanes
		
		
			425
			7292
		
		
			747
			4361
		
	

 

 

	
		
			Explanation
		
		
			airplane_id
			airline_id
			empty_seats
		
		
			2187
			425
			160
		
		
			7292
			425
			230
		
		
			5833
			425
			280
		
		
			3472
			425
			260
		
		
			2624
			425
			280
		
	

 

For airline with id 425 the average number of empty seats are 242. Therefore the airplane which closest to this average is 7292.

## Sample Input/Output

## Preview

You are provided with data of airplane bookings which contain total seats in a
