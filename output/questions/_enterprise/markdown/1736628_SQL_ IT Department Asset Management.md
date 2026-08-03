# SQL: IT Department Asset Management

## Metadata

- **ID:** 1736628
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Database, Medium, SQL, Merging, Conditional Logic
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, merging, and conditional logic concepts, ideal for mid-level roles. The problem requires creating a query to merge inventory data from separate tables for hardware and software assets, including their allocation status to employees.

## Problem Statement

An IT department aims to merge its inventory data, encompassing both hardware and software assets. Currently, these assets are recorded in separate tables. The task is to create a query that provides a comprehensive list of all assets, combining hardware and software, and includes information on their allocation to employees. It should also highlight assets that are not presently assigned to any employee.

 

The result should have the following columns: asset_id | asset_type | asset_name | employee_email.

	
- 
asset_id - the unique identifier for the asset.
	
- 
asset_type - the derived column that shows either `Hardware` or `Software` indicating the type of the asset.
	
- 
asset_name - the name of the asset.
	
- 
employee_email - the email address of the employee to whom the asset is assigned, or `Unassigned` if the asset is not currently assigned to any employee.

 

The result should be sorted in ascending, natural order by asset_id.

 

Note:

	
- Assets should be listed even if they are not assigned to any employee.
	
- Only active assets should be included in the report.

 

Schema

	employees
	
		
			Name
			Type
			Constraints
			Description
		
		
			id
			INT
			PRIMARY KEY
			The identifier of the employee
		
		
			email
			VARCHAR(255)
			 
			The employee email address
		
	

	hardware_assets
	
		
			Name
			Type
			Constraints
			Description
		
		
			id
			VARCHAR(255)
			PRIMARY KEY
			The identifier of the asset
		
		
			name
			VARCHAR(255)
			 
			The name of the asset
		
		
			is_active
			BOOLEAN
			 
			The activity status of the asset
		
		
			employee_id
			INT
			FOREIGN KEY(employee_id => employees.id)
			The reference to the employee
		
	

	software_assets
	
		
			Name
			Type
			Constraints
			Description
		
		
			id
			VARCHAR(255)
			PRIMARY KEY
			The identifier of the asset
		
		
			name
			VARCHAR(255)
			 
			The name of the asset
		
		
			is_active
			BOOLEAN
			 
			The activity status of the asset
		
		
			employee_id
			INT
			FOREIGN KEY(employee_id => employees.id)
			The reference to the employee
		
	

Sample Data Tables

	employees
	
		
			id
			email
		
		
			1
			alipson0@xinhuanet.com
		
		
			2
			tbortolotti1@soundcloud.com
		
		
			3
			kaisman2@google.com.br
		
	

 

	hardware_assets
	
		
			id
			name
			is_active
			employee_id
		
		
			HARD#1
			Printer
			1
			null
		
		
			HARD#2
			Tablet
			0
			3
		
		
			HARD#3
			Smartphone
			0
			2
		
		
			HARD#4
			Printer
			1
			null
		
		
			HARD#5
			Mouse
			1
			2
		
		
			HARD#6
			Printer
			0
			1
		
		
			HARD#7
			Switch
			1
			3
		
		
			HARD#8
			Printer
			1
			2
		
		
			HARD#9
			Router
			0
			3
		
		
			HARD#10
			Mouse
			1
			null
		
	

 

	software_assets
	
		
			id
			name
			is_active
			employee_id
		
		
			SOFT#1
			Design Software
			1
			null
		
		
			SOFT#2
			Communication Software
			1
			2
		
		
			SOFT#3
			Accounting Software
			1
			3
		
		
			SOFT#4
			Database Software
			1
			3
		
		
			SOFT#5
			Database Software
			0
			null
		
		
			SOFT#6
			Media Editing Software
			1
			2
		
		
			SOFT#7
			Security Software
			1
			2
		
		
			SOFT#8
			Design Software
			1
			3
		
		
			SOFT#9
			Security Software
			1
			2
		
		
			SOFT#10
			Operating System
			1
			3
		
	

Sample Output

+--------+----------+----------------------+---------------------------+
|asset_id|asset_type|asset_name            |employee_email             |
+--------+----------+----------------------+---------------------------+
|HARD#1  |Hardware  |Printer               |Unassigned                 |
|HARD#4  |Hardware  |Printer               |Unassigned                 |
|HARD#5  |Hardware  |Mouse                 |tbortolotti1@soundcloud.com|
|HARD#7  |Hardware  |Switch                |kaisman2@google.com.br     |
|HARD#8  |Hardware  |Printer               |tbortolotti1@soundcloud.com|
|HARD#10 |Hardware  |Mouse                 |Unassigned                 |
|SOFT#1  |Software  |Design Software       |Unassigned                 |
|SOFT#2  |Software  |Communication Software|tbortolotti1@soundcloud.com|
|SOFT#3  |Software  |Accounting Software   |kaisman2@google.com.br     |
|SOFT#4  |Software  |Database Software     |kaisman2@google.com.br     |
|SOFT#6  |Software  |Media Editing Software|tbortolotti1@soundcloud.com|
|SOFT#7  |Software  |Security Software     |tbortolotti1@soundcloud.com|
|SOFT#8  |Software  |Design Software       |kaisman2@google.com.br     |
|SOFT#9  |Software  |Security Software     |tbortolotti1@soundcloud.com|
|SOFT#10 |Software  |Operating System      |kaisman2@google.com.br     |
+--------+----------+----------------------+---------------------------+

```

## Sample Input/Output

## Preview

An IT department aims to merge its inventory data, encompassing both hardware
