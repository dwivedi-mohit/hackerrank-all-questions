# RBAC: Cluster Wide Role

## Metadata

- **ID:** 1163414
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** DevOps, Medium, Security, RBAC, Kubernetes
- **Skills:** Kubernetes Security

## Summary

This DevOps question evaluates Kubernetes Security, RBAC, and Cluster Role concepts, ideal for mid-level roles. The problem requires completing a Kubernetes definition file to create a Service Account, Cluster Role, and Cluster Role Binding for access control.

## Problem Statement

Complete the Kubernetes definition file stub "/home/ubuntu/1163414-kubernetes-rbac-cluster-wide-role/definition.yml" with one or more steps that do the following:

	
- creates a new Service Account named "administrator"
	
- creates a new Cluster Role named "supervisor", applies on all possible API groups, resources and verbs
	
- creates a new Cluster Role Binding named "administrator-supervisor", bounds a recently created Service Account "administrator" and Cluster Role "supervisor"

 

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "definition.yml" FILE IN "/home/ubuntu/1163414-kubernetes-rbac-cluster-wide-role" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.
	
- You have sudo privileges, if needed.

## Preview

Complete the Kubernetes definition file stub "/home/ubuntu/1163414-kubernetes-rb
