# Puppet: HackerBoard Credentials Setup

## Metadata

- **ID:** 1324119
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Puppet, DevOps, Medium, File, Facts, Embedded Puppet
- **Skills:** Puppet (Intermediate)

## Summary

This DevOps question evaluates Puppet, file management, and access control concepts, ideal for mid-level roles. The problem requires completing a manifest to set up application configuration, including file creation, ownership, and permissions based on specific facts.

## Problem Statement

While working on "HackerBoard" software deployment instructions, you decide to implement an application configuration file setup logic as a separate manifest.

 

Complete the file stub "/home/ubuntu/1324119-puppet-hackerboard-credentials-setup/manifest.pp" with one or more steps that do the following.

	
- Using an existing "/home/ubuntu/1324119-puppet-hackerboard-credentials-setup/credentials.ini.epp" template:
	
		
- Install a new file named "credentials.ini" at the path defined in the hackerboard_dir fact, then:

		
			
- set hackerboard:hackercompany ownership (USER AND GROUP CREATION IS REQUIRED!)
			
- set read and write permissions for the hackerboard user
			
- set read-only permissions for the hackercompany group
			
- restrict access for all other groups
		
		
		
- substitute the access_key parameter inside "credentials.ini" with the corresponding value from the hackerboard_access_key fact
	
	

The modules are managed using "r10k" and the  "/home/ubuntu/1324119-puppet-hackerboard-credentials-setup/Puppetfile" declaration, which can be modified if necessary.

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "manifest.pp" FILE IN "/home/ubuntu/1324119-puppet-hackerboard-credentials-setup" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.

## Preview

While working on "HackerBoard" software deployment instructions, you decide to i
