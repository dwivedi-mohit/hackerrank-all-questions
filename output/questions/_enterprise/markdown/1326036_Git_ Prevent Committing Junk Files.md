# Git: Prevent Committing Junk Files

## Metadata

- **ID:** 1326036
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Git, DevOps, Hard, Git Config, Git Hook
- **Skills:** Git (Advanced)

## Summary

This DevOps question evaluates Git configuration, branch protection, and commit hooks concepts, ideal for senior-level roles. The problem requires setting up repository-specific user details and implementing a commit rejection mechanism for certain file types.

## Problem Statement

You are working on the application development process and need to protect all Git branches from any commits that try to add "junk" files of certain extensions.

Using the existing Git repository "/home/ubuntu/1326036-git-prevent-committing-junk-files":

	
- Set up a Git username at the repository level (not globally!), set it to "Hacker Developer".
	
- Set up a Git email address at the repository level (not globally!), set it to "hacker.developer@hackercompany.com".
	
- Implement functionality that rejects commits with a "Junk files are not allowed" message for any of the Git branches. if they try to add "junk" files with the following extensions:
	
		
- *.tmp
		
- *.swp
	
	

"Junk" files must still be allowed to be modified or deleted!

Note:

	
- The completed solution will be evaluated in a new, clean environment. ONLY CHANGES IN "/home/ubuntu/1326036-git-prevent-committing-junk-files" WILL BE CARRIED TO THE NEW ENVIRONMENT. ALL CHANGES OUTSIDE THIS DIRECTORY WILL BE LOST.

## Preview

You are working on the application development process and need to protect all G
