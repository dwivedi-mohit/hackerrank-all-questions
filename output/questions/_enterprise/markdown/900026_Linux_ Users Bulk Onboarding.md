# Linux: Users Bulk Onboarding

## Metadata

- **ID:** 900026
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Linux, DevOps
- **Skills:** Linux (Intermediate)

## Summary

This DevOps question evaluates Linux user management, file handling, and scripting concepts, ideal for mid-level roles. The problem requires creating a script to onboard users based on a provided list, ensuring proper login formats and group assignments.

## Problem Statement

Complete the file stub "/home/ubuntu/900026-linux-users-bulk-onboarding/script.sh" with one or more steps that do the following:

	
- Read the list of first and last names of employers to onboard from "/home/ubuntu/900026-linux-users-bulk-onboarding/onboard.txt".
	
- Create the users with logins in the format "f_lastname", where "f" is the lowercase first letter of the first name.
	
- Put all the created users in the "onboarding" group.
	
- Force all created users to update their passwords at the next login.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/900026-linux-users-bulk-onboarding" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- You have sudo access.

 

Grading

	
- The execution result of "sudo solve" invoked from the question directory solves the task.

## Preview

Complete the file stub "/home/ubuntu/900026-linux-users-bulk-onboarding/script.s
