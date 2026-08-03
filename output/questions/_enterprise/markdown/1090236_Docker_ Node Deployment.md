# Docker: Node Deployment

## Metadata

- **ID:** 1090236
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Docker, DevOps
- **Skills:** Docker (Basic)

## Summary

This DevOps question evaluates Docker, application deployment, and containerization concepts, ideal for junior-level roles. The problem requires completing a Dockerfile to deploy a web application using specific instructions for image inheritance, file copying, and command execution.

## Problem Statement

You want to deploy a web application using Docker.  As part of the process, complete a file stub "/home/ubuntu/1090236-docker-node-deployment/Dockerfile" with one or more steps that do the following:

	
- Inherit a "public.ecr.aws/docker/library/node" image (from ECR) on the "12-alpine" tag.
	
- Copy the "application" folder with all contents to the "/application" path.
	
- Change the working directory context to "/application"
	
- Execute the "npm install" command.
	
- Override "CMD" (in "exec" form) to run the "node" executable with "application.js" as its parameter.
	
- Expose port "8000" to the outside.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/1090236-docker-node-deployment" folder.
	
- Run "solve" in the same directory as the Dockerfile as a shortcut to execute the code and check for runtime errors. Judge the accuracy of the results manually.

 

Grading

	
- The execution result of "solve" invoked from the question directory solves the task.
	
- The execution result of "wget -qO- http://localhost:8000/api/token" shows a valid JSON output.

## Preview

You want to deploy a web application using Docker.  As part of the process, comp
