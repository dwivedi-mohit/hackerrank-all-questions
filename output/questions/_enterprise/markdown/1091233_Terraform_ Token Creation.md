# Terraform: Token Creation

## Metadata

- **ID:** 1091233
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** DevOps, Easy, Terraform
- **Skills:** Terraform (Basic)

## Summary

This DevOps question evaluates Terraform, variable declaration, and resource management concepts, ideal for junior-level roles. The problem requires completing a Terraform file to declare a variable and output its value to a specified file using a null resource.

## Problem Statement

A company wants to deploy a web application using Terraform.  As part of that process, complete a file stub "/home/ubuntu/1091233-terraform-token-creation/main.tf" using HCL with one or more steps that do the following:

 

	
- Declares variable "token" that already passed to the apply target, with a reference environment variable as value.
	
- Using a "null_resource" resource and "local-exec" provisioner, outputs the value of the "token" variable, followed by a trailing newline, to the "/secret/token" file.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/1091233-terraform-token-creation" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- You have sudo access.

 

Grading

	
- The execution result of "sudo solve" invoked from the question directory solves the task.

## Preview

A company wants to deploy a web application using Terraform.  As part of that pr
