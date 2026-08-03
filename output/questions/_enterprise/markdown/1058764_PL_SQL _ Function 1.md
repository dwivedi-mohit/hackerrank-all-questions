# PL/SQL : Function 1

## Metadata

- **ID:** 1058764
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** PL/SQL, Hard
- **Skills:** PL/SQL (Advanced)

## Summary

This multiple choice question evaluates PL/SQL, function return values, and SQL queries concepts, ideal for senior-level roles. The problem requires determining the output of a function that retrieves a region name based on a given region ID.

## Problem Statement

There is a regions table in HR schema. A function is created to return Region_Name when it is called. 

	
		
			REGION_ID
			
			
REGION_NAME

			
		
		
			1
			Europe
		
		
			2
			America
		
		
			3
			Asia
		
		
			4
			Middle East and Africa
		
	

 

`Create or replace function Get_region_name(p_region_id Number) return varchar2 as
v_region_name varchar2(50);
v_region_id number;
Begin
    select Region_name Into v_region_name From Hr.regions Where Region_Id = p_region_id;
    Return v_region_name;
    return p_region_id;
 
End Get_region_name;
`
```

 

What will the function return?

## Preview

There is a regions table in HR schema. A function is created to return Region
