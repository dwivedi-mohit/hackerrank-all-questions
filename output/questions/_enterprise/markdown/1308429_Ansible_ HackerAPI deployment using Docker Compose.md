# Ansible: HackerAPI deployment using Docker Compose

## Metadata

- **ID:** 1308429
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** DevOps, Docker Compose, Ansible, Hard, Apt, Git, Docker
- **Skills:** Ansible (Advanced)

## Summary

This DevOps question evaluates Ansible, Docker, and Git concepts, ideal for senior-level roles. The problem requires implementing a playbook to clone a Git repository, initialize a Docker container, and build a binary executable with specific environment variables.

## Problem Statement

As the main part of "HackerAPI" software deployment, you have decided to implement a binary compilation and build logic as a separate playbook.

Complete the file stub "/home/ubuntu/1308429-ansible-hackerapi-deployment-using-docker-compose/playbook.yml" with one or more steps that do the following.

	
- Using a builtin core "git" module (Git binary installation is required!):
	
		
- clone an existing Git repository
		
			
- using "https://github.com/ProblemSetters/devops-inventory.git" upstream
			
- at "1308429-ansible" branch
			
- to the directory defined in the "HACKERAPI_BUILD_DIR" environment variable
		
		
	
	
	
- Using a "docker_composer" module:
	
		
- initialize a new Docker container
		
			
- using "134148934511.dkr.ecr.us-east-1.amazonaws.com/hr/gcc" image
			
- at "latest" tag
		
		
		
- mount the host's directory, defined in the "HACKERAPI_BUILD_DIR" environment variable, inside the container
		
- execute "gcc -o hackerapi hackerapi.c" command inside to build a "hackerapi" binary
	
	

As the result, a new "hackerapi" callable binary should appear in the host's directory defined in the "HACKERAPI_BUILD_DIR" environment variable.

The result of dynamic execution of the "hackerapi" binary should be an access token comprised of the "HACKERAPI_SECURITY_TOKEN" environment variable value and the hostname, for example: "11111111-2222-3333-4444-555555555555@myhostname"

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "playbook.yml" FILE IN "/home/ubuntu/1308429-ansible-hackerapi-deployment-using-docker-compose" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- Run "sudo solve" in the same directory as the "playbook.yml" as a shortcut to execute the code and check for runtime errors. Judge the accuracy of the results manually

## Preview

As the main part of "HackerAPI" software deployment, you have decided to impleme
