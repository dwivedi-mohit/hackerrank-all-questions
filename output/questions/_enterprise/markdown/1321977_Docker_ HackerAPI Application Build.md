# Docker: HackerAPI Application Build

## Metadata

- **ID:** 1321977
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Dockerfile, Docker, Hard, DevOps
- **Skills:** Docker (Advanced)

## Summary

This DevOps question evaluates Docker, Dockerfile, and environment variable configuration concepts, ideal for senior-level roles. The problem requires defining a Docker image with specific instructions to compile a C program and manage environment variables.

## Problem Statement

You are working on Docker image of the "HackerAPI" software.

 

Complete the file stub "/home/ubuntu/1321977-docker-hackerapi-application-build/Dockerfile" with one or more steps that do the following.

	
- Define a Docker image that inherits from "134148934511.dkr.ecr.us-east-1.amazonaws.com/hr/gcc" at the "latest" tag with instructions to:
	
		
- specify the "HACKERAPI_TOKEN" environment variable with an empty value
		
- specify the "/bin" path as a working directory
		
- pass the file "/home/ubuntu/1321977-docker-hackerapi-application-build/hackerapi.c" inside the image, for example at "/tmp/hackerapi.c" path, then compile it with the command "gcc -o hackerapi /tmp/hackerapi.c"
	
	

 

As the result, the directory "/build" should contain an executable binary named "hackerapi".

 

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "Dockerfile" FILE IN "/home/ubuntu/1321977-docker-hackerapi-application-build" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- Run "solve" in the same directory as the Dockerfile as a shortcut to execute the code and check for runtime errors. Judge the accuracy of the results manually.

## Preview

You are working on Docker image of the "HackerAPI" software.
