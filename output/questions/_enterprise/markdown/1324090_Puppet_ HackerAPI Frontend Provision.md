# Puppet: HackerAPI Frontend Provision

## Metadata

- **ID:** 1324090
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Puppet, DevOps, Easy, Package
- **Skills:** Puppet (Basic)

## Summary

This DevOps question evaluates Puppet, package management, and configuration management concepts, ideal for junior-level roles. The problem requires completing a Puppet manifest to remove an obsolete package and install a new one in a clean environment.

## Problem Statement

While working on the initial production deployment of the "HackerAPI" software stack, you decide to implement frontend provision logic as a separate manifest.

 

Complete the file stub "/home/ubuntu/1324090-puppet-hackerapi-frontend-provision/manifest.pp" with one or more steps that do the following.

	
- Using a built-in "package" resource type:
	
		
- remove an obsolete "apache2" package
		
			
- with all the dependencies
			
- with purging of configuration files
		
		
		
- install a new "nginx" package at latest available version
	
	

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "manifest.pp" FILE IN "/home/ubuntu/1324090-puppet-hackerapi-frontend-provision" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.

## Preview

While working on the initial production deployment of the "HackerAPI" software s
