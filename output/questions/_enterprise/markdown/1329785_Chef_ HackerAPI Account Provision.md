# Chef: HackerAPI Account Provision

## Metadata

- **ID:** 1329785
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Chef, DevOps, Easy, User
- **Skills:** Chef (Basic)

## Summary

This DevOps question evaluates Chef, user management, and automation concepts, ideal for junior-level roles. The problem requires implementing a recipe to create a user account with specific attributes in a Chef environment.

## Problem Statement

While working on the initial production deployment of the "HackerAPI" software stack, you decide to implement account provision logic as a separate recipe.

 

Complete the file stub "/home/ubuntu/1329785-chef-hackerapi-account-provision/recipe.rb" with one or more steps that do the following.

	
- Using a built-in "user" Infra Resource Type, create a new user account "hackerapi", having:
	
		
- a membership of the existing "backup" group
		
- an automatically created home directory at "/home/hackerapi"
		
- the "/bin/ash" user shell
	
	

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "recipe.rb" FILE IN "/home/ubuntu/1329785-chef-hackerapi-account-provision" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve" invoked from the question directory should solve the task.

## Preview

While working on the initial production deployment of the "HackerAPI" software s
