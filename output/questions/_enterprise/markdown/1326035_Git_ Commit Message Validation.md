# Git: Commit Message Validation

## Metadata

- **ID:** 1326035
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** DevOps, Hard, Git, Git Config, Git Hook
- **Skills:** Git (Advanced)

## Summary

This DevOps question evaluates Git configuration, commit validation, and branch protection concepts, ideal for senior-level roles. The problem requires setting up repository-level Git user details and implementing commit message validation against a Jira issue key format.

## Problem Statement

You are creating an application development process and need to protect all Git branches from any commits that are not related to a Jira issue.

 

Using the existing Git repository "/home/ubuntu/1326035-git-commit-message-validation":

	
- Set up a Git username at the repository level (not globally!), set it to "Hacker Developer".
	
- Set up a Git email address at the repository level (not globally!), set it to "hacker.developer@hackercompany.com".
	
- Implement functionality that rejects commits to any of the Git branches if they do not mention a Jira Issue Key with the message "Invalid commit message".

The Jira Issue Key has the following format: "[ABC-123]" (open square bracket followed by one or more letters in capital letters, then a hyphen, then one or more numbers, then a closing square bracket). For example: "[HACKERSOFT-15]" , "[IAM-395]"

Note:

	
- The completed solution will be evaluated in a new, clean environment. ONLY CHANGES IN "/home/ubuntu/1326035-git-commit-message-validation" WILL BE CARRIED TO THE NEW ENVIRONMENT. ALL CHANGES OUTSIDE THIS DIRECTORY WILL BE LOST.

## Preview

You are creating an application development process and need to protect all Git
