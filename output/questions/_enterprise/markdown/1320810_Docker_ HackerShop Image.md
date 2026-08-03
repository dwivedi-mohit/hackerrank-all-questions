# Docker: HackerShop Image

## Metadata

- **ID:** 1320810
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** DevOps, Docker, Medium, Dockerfile, Ports, Apt
- **Skills:** Docker (Intermediate)

## Summary

This DevOps question evaluates Docker, Dockerfile, and port exposure concepts, ideal for mid-level roles. The problem requires defining a Docker image that exposes specific ports and installs a package using an Nginx parent image.

## Problem Statement

You are working on Docker image of the "HackerShop" software.

 

Complete the file stub "/home/ubuntu/1320810-docker-hackershop-image-port-exposing/Dockerfile" with one or more steps that do the following.

	
- Define a Docker image
	
		
- with instructions to expose a ports "8910", "80", and "443" 
		
- that has an "public.ecr.aws/docker/library/nginx" image with the "1.20" tag as the parent image
		
- that has instructions to install an APT package of common CA certificates ("ca-certificates")
	
	

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "Dockerfile" FILE IN "/home/ubuntu/1320810-docker-hackershop-image-port-exposing" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.

## Preview

You are working on Docker image of the "HackerShop" software.
