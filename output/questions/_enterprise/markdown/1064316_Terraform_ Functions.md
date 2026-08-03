# Terraform: Functions

## Metadata

- **ID:** 1064316
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** DevOps, HashiCorp Configuration Language, Easy, Terraform, List Manipulation
- **Skills:** Terraform (Basic)

## Summary

This DevOps question evaluates Terraform, HCL functions, and list manipulation concepts, ideal for junior-level roles. The problem requires deploying a web application using Terraform to declare a variable and output the count, minimum, and maximum of a list of ports.

## Problem Statement

A web application must be deployed using Terraform.

 

Complete a file stub "/home/ubuntu/1064316-terraform-functions/main.tf" using HCL with one or more steps that do the following:

	
- Declare the variable “ports”, with type “list” of “numbers”. The value is passed via an environment variable when running “sudo solve”. 
	
- Using corresponding HCL functions and "output" block with the name "ports_count", find and output a total number of all the ports in the "ports" variable.
	
- Using corresponding HCL functions and "output" block with the name "ports_min", find and output the minimum port number from all the ports in the "ports" variable.
	
- Using corresponding HCL functions and "output" block with the name "ports_max", find and output the maximum port number from all the ports in the "ports" variable.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/1064316-terraform-functions" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- You have sudo access.

 

Grading

	
- The execution result of "sudo solve" invoked from the question directory solves the task.

## Preview

A web application must be deployed using Terraform.
