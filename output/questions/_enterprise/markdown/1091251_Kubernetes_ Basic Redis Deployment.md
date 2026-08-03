# Kubernetes: Basic Redis Deployment

## Metadata

- **ID:** 1091251
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, DevOps, Kubernetes
- **Skills:** Kubernetes (Basic)

## Summary

This DevOps question evaluates Kubernetes, deployment configurations, and namespace management concepts, ideal for junior-level roles. The problem requires completing a YAML file to deploy a Redis application with specific configurations in a Kubernetes environment.

## Problem Statement

A company wants to deploy a web application has built on Kubernetes.  As part of that process, complete a file stub "/home/ubuntu/1091251-kubernetes-basic-redis-deployment/definition.yml" with one or more steps that do the following:

 

	
- Creates a new namespace "hacker-company".
	
- Deploys a new "134148934511.dkr.ecr.us-east-1.amazonaws.com/hr/redis" image on the "latest" tag as "redis" deployment, in the "hacker-company" namespace.
	
- Increases the pods number of the "redis" deployment up to 2 replicas.
	
- Exposes "6379" port of the "redis" containers.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/1091251-kubernetes-basic-redis-deployment" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- You have sudo access.

## Preview

A company wants to deploy a web application has built on Kubernetes.  As part of
