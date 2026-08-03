# Docker: Volume Mounting

## Metadata

- **ID:** 835979
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** DevOps, Medium, Docker, Docker CLI, Docker Storage
- **Skills:** Docker (Intermediate)

## Summary

This DevOps question evaluates Docker, container management, and volume mounting concepts, ideal for mid-level roles. The task requires completing a script to run Docker containers with specific volume mount configurations and permissions.

## Problem Statement

The task is to complete a file stub "/home/ubuntu/835979-docker-volume-mounting/script.sh" with one or more steps that do the following:

	
- Runs a new Docker container "my-container-rw" from the "public.ecr.aws/docker/library/busybox" image (latest tag) in interactive background mode, without pseudo-TTY allocation.
	
- Runs a new Docker container "my-container-ro" from the "public.ecr.aws/docker/library/busybox" image (latest tag) in interactive background mode, without pseudo-TTY allocation.
	
- Mounts an existing volume "/home/ubuntu/835979-docker-volume-mounting" at "/mnt" of the "my-container-rw" container in "read-write" mode.
	
- Mounts an existing volume "/home/ubuntu/835979-docker-volume-mounting" at "/mnt" of the "my-container-ro" container in "read-only" mode.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/835979-docker-volume-mounting" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- Docker is already installed.
	
- You have sudo access.

 

Grading

	
- The execution result of "docker exec my-container-ro rm /mnt/my-file.txt" outputs a "read-only file system" error.
	
- The execution result of "docker exec my-container-rw rm /mnt/my-file.txt" removes the file from both the host and all the containers.

## Preview

The task is to complete a file stub "/home/ubuntu/835979-docker-volume-mounting/
