# Git: Feature Branch Push

## Metadata

- **ID:** 1326053
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Git, DevOps, Medium, Git Branch, Git Push
- **Skills:** Git (Intermediate)

## Summary

This DevOps question evaluates Git branching, commit management, and repository manipulation concepts, ideal for mid-level roles. The problem requires creating a feature branch from the master branch, committing changes, and ensuring the master branch remains intact.

## Problem Statement

A team uses the "feature branch" strategy for software development. There is an initial commit in the "master" branch that contains the currently deployed code base. There are also changes that have not been committed to "master". Copy the current code base to a "feature" branch where additional development can be managed without affecting the version in the "master" branch.

Using the existing Git repository "/home/ubuntu/1326053-git-feature-branch-push":

	
- Implement functionality that
	
		
- moves the current changes in the "master" Git branch to the new "feature" Git

		  branch
		
- commits with a "New feature" message
		
- pushes them to the "origin/feature" Git origin.
	
	
	
- Reset all the changes in the "master" Git branch to the state of HEAD.

The "master" Git branch

	
- should remain intact and look like this:
	
		
- "Initialize" (first commit)
	
	
	
- should have nothing to commit
	
- the working tree should be clean

The "feature" Git branch should look like this:

	
- "New feature" (last commit)
	
- "Initialize" (first commit)

 

The first commit in both Git branches must be identical.

Note:

	
- The completed solution will be evaluated in a new, clean environment. ONLY CHANGES IN "/home/ubuntu/1326053-git-feature-branch-push" WILL BE CARRIED TO THE NEW ENVIRONMENT. ALL CHANGES OUTSIDE THIS DIRECTORY WILL BE LOST.

## Preview

A team uses the "feature branch" strategy for software development. There is an
