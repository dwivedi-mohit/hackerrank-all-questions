# Kubernetes: Liveness Probe

## Metadata

- **ID:** 932257
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, DevOps, Kubernetes
- **Skills:** Kubernetes (Intermediate)

## Summary

This DevOps question evaluates Kubernetes, deployment, and liveness probes concepts, ideal for mid-level roles. The problem requires deploying an nginx container with a liveness probe in a specified namespace using a YAML definition file.

## Problem Statement

A web application built on Kubernetes must be deployed. Complete the file stub "/home/ubuntu/932257-kubernetes-liveness-probe/definition.yml" with one or more steps that do the following:

	
- Create a new namespace "hacker-company".
	
- Deploy a new "nginx" image (from Dockerhub) as "nginx" container on the "stable" tag as "frontend" pod, in the "hacker-company" namespace.
	
- Create a new liveness probe on "nginx" container that executes "nginx -t" command every "60" seconds.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/932257-kubernetes-liveness-probe" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- You have sudo access.

 

Grading

	
- The execution result of "sudo solve" invoked from the question directory solves the task.

## Preview

A web application built on Kubernetes must be deployed. Complete the file stub "
