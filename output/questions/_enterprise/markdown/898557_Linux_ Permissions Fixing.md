# Linux: Permissions Fixing

## Metadata

- **ID:** 898557
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, DevOps, Linux
- **Skills:** Linux (Intermediate)

## Summary

This DevOps question evaluates Linux permissions, file extraction, and ownership concepts, ideal for mid-level roles. The problem requires writing a script to extract files, set permissions, change ownership, and create a new archive in a specified directory.

## Problem Statement

Complete the file stub "/home/ubuntu/898557-linux-permissions-fixing/script.sh" with one or more steps that do the following:

	
- Extract the archive "/home/ubuntu/898557-linux-permissions-fixing/archive.tar.gz".
	
- Set permission "0664" for all the extracted files.
	
- Set permission "0775" for all the extracted folders.
	
- Set the owner to "nobody" and the group to "nogroup" for all the extracted files and folders.
	
- From all the fixed files and folders, create a new archive named "/tmp/archive.tar.gz".

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/898557-linux-permissions-fixing" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- You have sudo access.

 

Grading

	
- The execution result of "sudo solve" invoked from the question directory solves the task.

## Preview

Complete the file stub "/home/ubuntu/898557-linux-permissions-fixing/script.sh"
