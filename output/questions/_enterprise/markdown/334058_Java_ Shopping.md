# Java: Shopping

## Metadata

- **ID:** 334058
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Maven, Hibernate, Back-End Development, Medium, SQLite
- **Skills:** Java (Intermediate)

## Summary

This back-end development question evaluates Hibernate, Java, and database access concepts, ideal for mid-level roles. The problem requires completing a Java class using Hibernate to interact with a SQLite database containing inventory details.

## Problem Statement

Use Hibernate to complete a Java class that accesses a database.

The Java project in the editor below provides the following completed implementations:

	
- A SQLite3 database named `inventory.db` that holds the details for each item in a table named `Inventory`. The table has the following six columns:

	
		
			
				Name
				Type
				Description
			
			
				barcode
				string
				The items's 128-C (numeric only) barcode. This field is a primary key.
			
			
				item
				string
				The item's name.
			
			
				category
				string
				The item's category.
			
			
				price
				float
				The item's price given in dollars. This value is in the inclusive range [50, 5000].
			
			
				discount
				integer
				The percent discount applied to the item. This value is in the inclusive range [5, 20].
			
			
				available
				integer
				This is a flag denoting whether or not the item is available. A value of 1 indicates the item is available and a value of 0 indicates it is not.
			
		
	
	
	
- The `persistent.Item` class is the `Inventory` table's DAO (Data Access Object).
	
- The `hackerrank.HibernateSessionHelper` class is the helper for managing Hibernate sessions.
	
- The `hackerrank.HibernateQueryRunner` class is the helper for executing Hibernate queries.
	
- The `org.hibernate.dialect.SQLiteDialect` class defines a third party Hibernate SQLite3 dialect.

Complete the `hackerrank.Purchase` class so that the project passes all of the unit tests.

## Preview

Use Hibernate to complete a Java class that accesses a database.
