# Ansible: HackerBoard configuration

## Metadata

- **ID:** 1306065
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Ansible, Medium, DevOps, Get_url, ini File
- **Skills:** Ansible (Intermediate)

## Summary

This DevOps question evaluates Ansible, environment variable management, and file permissions concepts, ideal for mid-level roles. The problem requires completing a playbook to configure an application setup dynamically based on environment variables and specific file permissions.

## Problem Statement

While working on "HackerBoard" software deployment instructions, you have decided to implement an application configuration file setup logic as a separate playbook.

Complete the file stub "/home/ubuntu/1306065-ansible-hackerboard-configuration/playbook.yml" with one or more steps that do the following.

	
- Using an existing remote "https://raw.githubusercontent.com/ProblemSetters/devops-inventory/1306065-ansible/config.ini" template:

	
		
- install a new file named "config.ini" at the path defined in the HACKERBOARD_DIR environment variable, then:
		
- set hackerboard:hackercompany ownership (USER AND GROUP CREATION IS REQUIRED)
		
- set read and write permissions for the hackerboard user
		
- set read only permissions for the hackercompany group
		
- set read only permissions for everyone else
		
			
- substitute the instance_id variable inside "config.ini" with the corresponding value from AWS_INSTANCE_ID environment variable
			
- change the mode option in the global section of "config.ini" to "debug"
			
- change the hostname option in the network section of "config.ini" to the current hostname (THIS OPERATION SHOULD BE DYNAMIC AND MUST NOT BE HARDCODED!)
			
- change the fingerprint option in the network section of "config.ini" to the MD5 hash of the current hostname (THIS OPERATION SHOULD BE DYNAMIC AND MUST NOT BE HARDCODED!)
			
- remove the is_primary option in the replica section of "config.ini" completely
		
		
	
	

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "playbook.yml" FILE IN "/home/ubuntu/1306065-ansible-hackerboard-configuration" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.

## Preview

While working on "HackerBoard" software deployment instructions, you have decide
