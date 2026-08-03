# Android(Kotlin): Array filters

## Metadata

- **ID:** 1701042
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Android, Kotlin, Filtering, RecyclerView, Dialog, Event Handling, Easy
- **Skills:** Android (Basic)

## Summary

This mobile development question evaluates filtering, event handling, and data management concepts, ideal for junior-level roles. The problem requires implementing a filtering system for employee data based on salary and name criteria within an Android application.

## Problem Statement

The app's main purpose is to show the list of employees depending on the applied filter parameters.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

 

You can set different parameters in the app. First, you can add a new employee.

Also, you can remove an employee from the list.

Finally, you can set minimum and maximum salary to a filter parameters and apply it to the list of employees.

You have to make a filter to the name or part of the name and comparison with the salary.

Sorting button is added to AppBar that sorts employees by salary level in ascending and descending order.

There are two array lists which are fullEmployeeArrayList and filterEmployeeArrayList. fullEmployeeArrayList means all the employees in the app. filterEmployeeArrayList shows the employees' list after the filter parameters are applied.

filterEmployeeArrayList shall contain filtered fullEmployeeArrayList after the following methods execution:

 

	
- "getEmployeeSalaryLessThanAndMoreThan" shall contain the list of employees who have the salary that is more than a specified minimum value and less than a specified maximum value
	
- "getEmployeeEqualNameLessThan" shall contain the list of employees with the exact specified name and who have the salary less than a specified maximum value
	
- "getEmployeeEqualNameMoreThan" shall contain the list of employees with the exact specified name and who have the salary more than a specified minimum value
	
- "getEmployeeEqualNameLessThanAndMoreThan" shall contain the list of employees with the exact specified name and who have the salary that is more than a specified minimum value and less than a specified maximum value
	
- 
"getEmployeeContainsPartNameLessThan"  shall contain the list of employees with part of the specified name and who have the salary less than a specified maximum value

	
- "getEmployeeContainsPartNameMoreThan" shall contain the list of employees with part of the specified name and who have the salary more than a specified minimum value
	
- "getEmployeeContainsPartNameLessThanAndMoreThan" shall contain the list of employees with part of the specified name and who have the salary that is more than a specified minimum value and less than a specified maximum value

 

	
- "chooseOption" method applies filter parameters. Add the appropriate filtering method to switch case statement

 

	
- "sortSalaryMaxToMin" shall contain the list of employees sorted from minimum to maximum salary
	
- "sortSalaryMinToMax" shall contain the list of employees sorted from maximum to minimum salary

## Preview

The app's main purpose is to show the list of employees depending on the applied
